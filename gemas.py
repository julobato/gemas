#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def criar (num_linhas:int, num_colunas:int):
    ''' 
    Cria matriz de representação do tabuleiro e a preenche com
    espaços vazios representados por ' '.

    Retorna a matriz criada.
    '''
    
    tabuleiro = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro


def exibir (tabuleiro:list):
    ''' 
    Exibe o tabuleiro.
    '''
    
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    string = "\n    "
    for i in range(num_colunas):
        string += str(i) + " "
    string+="\n  +"
    for i in range(num_colunas):
        string+="--"
    string+="-+\n"
    for linha in range(num_linhas):
        string+= str(linha) + " | "
        for coluna in range(num_colunas):
            string+= tabuleiro[linha][coluna] + " "
        string += "|\n"
    string+= "  +"
    for i in range(num_colunas):
        string+="--"
    string+="-+"
    print(string)

def trocar (linha1:int, coluna1:int, linha2:int, coluna2:int, tabuleiro:list) -> bool:
    ''' 
    Permuta gemas das posições (linha1, coluna1) e (linha2, coluna2) caso
    seja válida (isto é, gemas são adjacentes e geram cadeias), caso contrário
    não altera o tabuleiro.

    Retorna `True` se permutação é válida e `False` caso contrário.
    '''
    if linha1+1 != linha2:
        if linha1-1 != linha2:
            if coluna1+1 != coluna2:
                if coluna1-1 != coluna2:
                    return False
    novo_tabuleiro = clonar_matriz(tabuleiro)
    novo_tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
    novo_tabuleiro[linha2][coluna2] = tabuleiro[linha1][coluna1]
    if len(identificar_cadeias_horizontais(novo_tabuleiro)) >0:
        tabuleiro[linha1][coluna1] = novo_tabuleiro[linha1][coluna1]
        tabuleiro[linha2][coluna2] = novo_tabuleiro[linha2][coluna2]
        return True
    elif len(identificar_cadeias_verticais(novo_tabuleiro)) >0:
        tabuleiro[linha1][coluna1] = novo_tabuleiro[linha1][coluna1]
        tabuleiro[linha2][coluna2] = novo_tabuleiro[linha2][coluna2]
        return True
    return False


def identificar_cadeias_horizontais (tabuleiro:list) -> list:
    ''' 
    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o número da linha da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    igual= True
    coluna = 0
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for linha in range(num_linhas):
        while coluna < num_colunas-2:
            cont = 1
            while cont <num_colunas-coluna and igual:
                if tabuleiro[linha][coluna] != tabuleiro[linha][coluna+cont]:
                    if cont>=2:
                        break
                    igual= False
                else:
                    cont+=1
            if igual and cont>2:
                if tabuleiro[linha][coluna] != ' ':
                    cadeias.append([linha,coluna,linha,coluna+cont-1])
            igual = True
            coluna+=cont
        coluna = 0
    return cadeias


def identificar_cadeias_verticais (tabuleiro:list) -> list:
    ''' 
    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o número da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o número da coluna das gemas da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    igual= True
    linha = 0
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for coluna in range(num_colunas):
        while linha < num_colunas-2:
            cont = 1
            while cont <num_linhas-linha and igual:
                if tabuleiro[linha][coluna] != tabuleiro[linha+cont][coluna]:
                    if cont>=2:
                        break
                    igual= False
                else:
                    cont+=1
            if igual and cont>2:
                if tabuleiro[linha][coluna] != ' ':
                    cadeias.append([linha,coluna,linha+cont-1,coluna])
            igual = True
            linha+=cont
        linha = 0
    return cadeias


def eliminar_cadeia (tabuleiro:list, cadeia:list) -> int:
    ''' 
    Elimina (substitui pela string espaço `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o número da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Retorna o número de gemas eliminadas.
    '''
    gemas = 0
    if cadeia[0] == cadeia[2]:
        for i in range(cadeia[1],cadeia[3]+1):
            tabuleiro[cadeia[0]][i]= ' '
            gemas+=1
    else:
        for j in range(cadeia[0],cadeia[2]+1):
            tabuleiro[j][cadeia[1]] = ' '
            gemas+=1
    return gemas
    
def eliminar (tabuleiro:list) -> int:
    ''' 
    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaços (' ').

    Retorna número de gemas eliminadas.
    '''
    gemas = 0
    horizontais = identificar_cadeias_horizontais(tabuleiro)
    verticais = identificar_cadeias_verticais(tabuleiro)
    for h in horizontais:
        gemas+=eliminar_cadeia(tabuleiro,h)
    for v in verticais:
        gemas+=eliminar_cadeia(tabuleiro,v)

    return gemas
    
def deslocar_coluna ( tabuleiro:list, i:int ):
    ''' 
    Desloca as gemas na coluna i para baixo, ocupando espaços vazios.
    '''
    cont = 0
    linha = len(tabuleiro)-1
    while linha > 0:
        while (tabuleiro[linha][i] == ' ') and (linha-(cont+1)) > 0:
            cont+=1
            if tabuleiro[linha-cont][i] != ' ':
                tabuleiro[linha][i] = tabuleiro[linha-cont][i]
                tabuleiro[linha-cont][i] = ' '
        cont=0
        linha-=1
    
def deslocar (tabuleiro:list):
    ''' 
    Desloca gemas para baixo deixando apenas espaços vazios sem nenhuma gema acima.
    '''
    
    num_colunas = len(tabuleiro[0])
    for i in range(num_colunas):
        deslocar_coluna(tabuleiro,i)
    h = identificar_cadeias_horizontais(tabuleiro)
    v = identificar_cadeias_verticais(tabuleiro)
    if len(h)>0 or len(v)>0:
        eliminar(tabuleiro)
        deslocar(tabuleiro)

def existem_movimentos_validos (tabuleiro:list) -> bool:
    '''
    Retorna True se houver movimentos válidos, False caso contrário.
    '''
    
    clone = clonar_matriz(tabuleiro)
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for linha in range(num_linhas):
        if validos_horizontal(clone,linha):
            return True
    for coluna in range(num_colunas):
        if validos_vertical(clone,coluna):
            return True
    return False

def validos_horizontal(tabuleiro,linha):
    '''
    Retorna True se houver movimentos válidos na horizontal, False caso contrário.
    '''
    
    for coluna in range(len(tabuleiro[0])-1):
        if trocar(linha, coluna, linha, coluna+1, tabuleiro):
            return True
    return False
    
def validos_vertical(tabuleiro,coluna):
    '''
    Retorna True se houver movimentos válidos na vertical, False caso contrário.
    '''
    
    for linha in range(len(tabuleiro)-1):
        if trocar(linha, coluna, linha+1, coluna, tabuleiro):
            return True
    return False
    
def clonar_matriz(tabuleiro):
    '''
    Retorna uma cópia da matriz.
    '''
    novo = []
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    for lin in range(num_linhas):
        linha = []
        for col in range(num_colunas):
            linha.append(tabuleiro[lin][col])
        novo.append(linha)
    return novo



###############################################################################
### NÃO MODIFIQUE AS LINHAS ABAIXO ############################################
###############################################################################
import util                                                                   #
util.criar = criar                                                            #
util.exibir = exibir                                                          #
util.trocar = trocar                                                          #
util.identificar_cadeias_horizontais = identificar_cadeias_horizontais        #
util.identificar_cadeias_verticais = identificar_cadeias_verticais            #
util.eliminar = eliminar                                                      #
util.eliminar_cadeia = eliminar_cadeia                                        #
util.deslocar = deslocar                                                      #
util.deslocar_coluna = deslocar_coluna                                        #
util.existem_movimentos_validos = existem_movimentos_validos                  #
if __name__ == '__main__':                                                    #
    util.main()                                                               #
###############################################################################