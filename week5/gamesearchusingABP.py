import math

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-----")

    def is_winner(self, player):
        # Rows
        for i in range(0, 9, 3):
            if all(self.board[j] == player for j in range(i, i + 3)):
                return True
        # Columns
        for i in range(3):
            if all(self.board[j] == player for j in range(i, 9, 3)):
                return True
        # Diagonals
        if all(self.board[i] == player for i in [0, 4, 8]):
            return True
        if all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def get_available_moves(self):
        return [i for i, v in enumerate(self.board) if v == ' ']

    def make_move(self, move, player):
        self.board[move] = player

    def undo_move(self, move):
        self.board[move] = ' '

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if board.is_winner('X'):
        return -10 + depth
    elif board.is_winner('O'):
        return 10 - depth
    elif board.is_full():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, depth + 1, False, alpha, beta)
            board.undo_move(move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, depth + 1, True, alpha, beta)
            board.undo_move(move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move, 'O')
        eval = minimax(board, 0, False, -math.inf, math.inf)
        board.undo_move(move)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# =======================
# Play the Game
# =======================
game = TicTacToe()
while True:
    game.print_board()
    if game.is_winner('X'):
        print("You win!")
        break
    elif game.is_winner('O'):
        print("AI wins!")
        break
    elif game.is_full():
        print("It's a draw!")
        break

    if game.current_player == 'X':
        move = int(input("Enter your move (0-8): "))
        if move not in game.get_available_moves():
            print("Invalid move!")
            continue
        game.make_move(move, 'X')
        game.current_player = 'O'
    else:
        print("AI is thinking...")
        move = get_best_move(game)
        game.make_move(move, 'O')
        game.current_player = 'X'
