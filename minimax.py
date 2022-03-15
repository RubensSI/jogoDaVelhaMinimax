from jogo import *

def movimento_ia(board, jogador):
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None

    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = ini

        if(melhor_valor is None):
            valor = melhor_valor
            melhor_movimento = possibilidade
        elif(jogador == 0):
            if(valor > melhor_valor):
                valor = melhor_valor
                melhor_movimento = possibilidade
        elif( jogador == 1):
            if(valor < melhor_valor):
                valor = melhor_valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ini):
                posicoes.append([i, j])
    return posicoes

pontos = {
    "Empate": 0,
    "X": 1,
    "O": -1
}


def minimax(board, jogador):
    ganhador = verifica_ganhador(board)
    if (ganhador):
        return pontos[ganhador]
    jogador = (jogador + 1) % 2

    possibilidades = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = ini

        if (melhor_valor is None):
            melhor_valor = valor
        elif (jogador == 0):
            if (valor > melhor_valor):
                melhor_valor = valor
        elif (jogador == 1):
            if (valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor
