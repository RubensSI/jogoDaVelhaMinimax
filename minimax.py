from jogo import *

def movimento_ia(board, jogador):
    # Verificar todas as possibilidades
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None

    # Considerando a melhor possibilidade para ganhar o jogo
    # Vamos descobrir o melhor movimento
    # pesquisando em todas as possibilidades
    for possibilidade in possibilidades:
        # O tabuleiro irá sofrer uma mudança
        # Acessando assim a nova lista de posições
        # Setando temporariamente assim a 'O' ou 'X'
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        # Retornano o valor do miniMax que é o '0', '1' e o '-1'
        valor = minimax(board, jogador)
        # Limpando o tabuleiro
        board[possibilidade[0]][possibilidade[1]] = ini
        print(possibilidade, valor)

        # Verificando se existe um melhor valor já setado na variavel
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
            # Aqui a 'O' quer sempre o maior valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif( jogador == 1):
            # Aqui o 'X' quer sempre o menor valor
            if(valor < melhor_valor):
                valor = melhor_valor
                melhor_movimento = possibilidade
    print("Probabilidade de vitoria:", melhor_valor * 100, "%")
    # Acessando a lista de possibilidade da variável posições
    # Retornar o melhor movimento
    return melhor_movimento[0], melhor_movimento[1]

# O getPosicoes pega todas as posições vazias
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
    # Aqui ele recebe o resultado  False ou True se houver um ganhador
    ganhador = verifica_ganhador(board)
    if (ganhador):
        # Se existir um ganhador
        # pontos recebe o ganhador e logo depois vai acessar o
        # dicionario de dados contendo chave e valor
        # pegando  o valor referente aquela chave 'X' , 'O' ou 'EMPATE'.
        return pontos[ganhador]
    # Troco os jogadores
    jogador = (jogador + 1) % 2

    # A maquina vai testar as possibilidade, ou seja, as  jogadas do oponete
    possibilidades = getPosicoes(board)
    melhor_valor = None

    for possibilidade in possibilidades:
        # O tabuleiro irá sofrer uma mudança
        # Acessando assim a nova lista de posições
        # Setando assim a 'O' ou 'X
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        # Retornano o valor do minimax que pode ser '0', '1' e o '-1'
        valor = minimax(board, jogador)
        # limpando o tabuleiro
        board[possibilidade[0]][possibilidade[1]] = ini

        # Verificando se existe um melhor valor já setado na variavel
        if (melhor_valor is None):
            melhor_valor = valor
            # Aqui a 'O' quer sempre o maior valor
            # Vai verificar se o jagador é a vez da máquina
        elif (jogador == 0):
            if (valor > melhor_valor):
                melhor_valor = valor
        # Aqui o 'X' quer sempre o menor valor
        # Vai verificar se o jagador é o jogador é o X
        elif (jogador == 1):
            if (valor < melhor_valor):
                melhor_valor = valor

    # Retorna o melhor valor caso ele não entre em nenhuma destas condições
    return melhor_valor
