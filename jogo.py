# sempre vai ter uma string vazia
ini = " "
token = ["X", "O"]

def criar_board():
    board = [
        [ini, ini, ini],
        [ini, ini, ini],
        [ini, ini, ini],
    ]
    return board

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if (i < 2 ):
            print("----------")
    print()

def get_input_valid(msg):
    try:
        n = int(input(msg))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("O número deve estar entre 1 e 3!")
            return get_input_valid(msg)
    except:
        print("numero não válido")
        return get_input_valid(msg)

def verifica_movimento(board, i, j):
    if(board[i][j] == ini):
        return True
    else:
        return False

def fazer_movimento(board, i, j, jogador):
    board[i][j] = token[jogador]

def verifica_ganhador(board):
     # horizontal
     for i in range(3):
         if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ini):
             return board[i][0]

     # vertical
     for i in range(3):
         if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ini):
             return board[0][i]

     # diagonal principal
     if (board[0][0] != ini and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

     # diagonal secundária
     if (board[0][2] != ini and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

     for i in range(3):
         for j in range(3):
             if(board[i][j] == ini):
                 return False

     return "Empate"