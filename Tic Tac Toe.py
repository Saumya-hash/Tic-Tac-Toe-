import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print('-' * 5)

def check_winner(brd, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pos in win_positions:
        if all(brd[i] == player for i in pos):
            return True
    return False

def is_draw(brd):
    return ' ' not in brd

def get_valid_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

def minimax(brd, depth, is_maximizing, alpha, beta):
    if check_winner(brd, 'X'):
        return 10 - depth
    if check_winner(brd, 'O'):
        return depth - 10
    if is_draw(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_valid_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, False, alpha, beta)
            brd[move] = ' '
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_valid_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, True, alpha, beta)
            brd[move] = ' '
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_eval

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_valid_moves(board):
        board[move] = 'X'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'X'

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in get_valid_moves(board):
                board[move] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Enter a number between 1 and 9.")

def play_game():
    print("Welcome to Tic-Tac-Toe! You are O, AI is X.")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner(board, 'O'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner(board, 'X'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
