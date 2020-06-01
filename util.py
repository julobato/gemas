import random
random.seed(0)

def criar (num_linhas, num_colunas):
    raise NotImplementedError
    
def exibir (tabuleiro):
    raise NotImplementedError

def eliminar (tabuleiro):
    raise NotImplementedError

def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    raise NotImplementedError

def identificar_cadeias_horizontais (tabuleiro):
    raise NotImplementedError

def identificar_cadeias_verticais (tabuleiro):
    raise NotImplementedError
    
def eliminar_cadeia (tabuleiro, cadeia):
    raise NotImplementedError

def deslocar (tabuleiro):
    raise NotImplementedError

def deslocar_coluna ( tabuleiro, i ):
    raise NotImplementedError

def existem_movimentos_validos (tabuleiro):
    raise NotImplementedError

# ======================================================================
#
#   M A I N
#
# ======================================================================
def main():
    '''
    Esta é a função principal. Contém os comandos que
    obtêm os parâmetros necessários para criação do jogo (número de linhas,
    colunas e cores), e executa o laço principlal do jogo: ler comando,
    testar sua validade e executar comando.

    '''
    
    [' ', 'B', 'D', 'F', 'G', 'D', 'B', 'C'], 
    ['B', 'D', 'C', 'F', 'A', 'A', 'E', 'C'], 
    ['A', 'F', 'G', 'D', 'G', 'A', 'G', ' '], 
    ['G', ' ', ' ', 'G', 'B', 'B', 'A', ' '], 
    ['B', 'D', 'A', 'D', 'F', 'D', 'A', ' '], 
    ['G', 'D', 'E', 'C', 'D', 'B', 'G', 'G'], 
    ['E', 'C', 'B', 'A', 'D', 'G', 'A', 'E'], 
    ['A', 'C', 'A', 'E', 'E', 'A', 'F', 'F']
    
    
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()
    pontos = 0
    # lê parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o número de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuração inicial
    try:
        tabuleiro = criar (num_linhas, num_colunas)
    except NotImplementedError:
        print("\n!!! Função 'criar' ainda não foi implementada.\n")
        return
    except:
        print("Erro ao executar função 'criar'")
        raise
    try:
        completar (tabuleiro, num_cores)
    except e:
        print(e)
    try:
        num_gemas = eliminar (tabuleiro)
    except NotImplementedError:
        print("\n!!!Função 'eliminar' ainda não foi implementada.\n")
        return
    except:
        print("\n!!!Erro ao executar função 'eliminar'\n")
        raise

    while num_gemas > 0:
        try:
            deslocar (tabuleiro)
        except NotImplementedError:
            print("\n!!!Função 'deslocar' ainda não foi implementada.\n")
            return
        except:
            print("\n!!!Erro ao executar função 'deslocar'\n")
            raise
        completar (tabuleiro, num_cores)
        try:
            num_gemas = eliminar (tabuleiro)
        except:
            print("\n!!!Erro ao executar função 'eliminar'\n")
            raise
    # laço principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos válidos...
        try:
            exibir (tabuleiro)
        except NotImplementedError:
            print("\n!!!Função 'exibir' ainda não foi implementada.\n")
            return
        except:
            print("\n!!!Erro ao executar função 'exibir'\n")
            raise
            
        entrada = input("Digite um comando (ex.: ajuda): ").split()
        comando = entrada[0]
        args = entrada[1:]
        if comando == "perm" and len(args) == 4:
            linha1 = int(args[0]) #int(input("Digite a linha da primeira gema: "))
            coluna1 = int(args[1]) #int(input("Digite a coluna da primeira gema: "))
            linha2 = int(args[2]) #int(input("Digite a linha da segunda gema: "))
            coluna2 = int(args[3]) #int(input("Digite a coluna da segunda gema: "))
            print ()
            try:
                valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            except NotImplementedError:
                print("\n!!!Função 'trocar' ainda não foi implementada.\n")
                return
            except:
                print("\n!!!Erro ao executar função 'trocar'\n")
                raise
            
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    #print(f"Nesta rodada: {num_gemas} gemas destruidas!")
                    #exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print (f"*** Você destruiu {total_gemas} gemas! ***")
                print ()
            else:
                print ()
                print ("*** Movimento inválido! ***")
                print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
================ Ajuda =====================
perm l1 c1 l2 c2  
    permuta gemas nas posicoes l1,c1 e l2,c2
sair  
    termina o jogo
=============================================
                  """)
        else:
            print ()
            print ("*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print ()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print ("Você destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro:list, num_cores:int):
    ''' 
    Preenche espaços vazios com novas gemas geradas aleatoriamente.

    As gemas são representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]
