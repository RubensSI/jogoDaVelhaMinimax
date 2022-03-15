from jogo import *
from minimax import *

# criar board
board = criar_board()

# variavel que vai receber o jogador atual
jogador = 0

# verifica ganhador passando o board
ganhador = verifica_ganhador(board)
while(not ganhador):
    print_board(board)

    if (jogador == 0):
        i,j = movimento_ia(board, jogador)
    else:
        i = get_input_valid("Digite a linha: ")
        j = get_input_valid("Digite a coluna: ")
    print()

    if (verifica_movimento(board, i, j)):
        fazer_movimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("Posição ocupada!")
        print()

    ganhador = verifica_ganhador(board)

print_board(board)
print("Ganhador: ", ganhador)