# nqueens_utils.py
import random

BOARD_SIZE = 8

def count_conflicts(board):
    """Return the number of pairs of queens that attack each other."""
    attacks = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            same_row = board[i] == board[j]
            same_diag = abs(board[i] - board[j]) == (j - i)
            if same_row or same_diag:
                attacks += 1
    return attacks

def generate_neighbors(board):
    """Produce every board reachable by moving a single queen to another row within its own column."""
    result = []
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            if row != board[col]:
                modified = board[:]
                modified[col] = row
                result.append(modified)
    return result

def create_random_board():
    """Generate a board with each queen placed on a random row."""
    return [random.randint(0, BOARD_SIZE - 1) for _ in range(BOARD_SIZE)]

def display_board(board):
    """Render the board to stdout. Q = queen, . = empty."""
    for r in range(BOARD_SIZE):
        row_str = ""
        for c in range(BOARD_SIZE):
            row_str += " Q" if board[c] == r else " ."
        print(row_str)

def show_summary(algo_name, initial, final, h_val, iters, evals):
    """Print a standardised result block used by every algorithm."""
    print()
    print("===== " + algo_name + " =====")
    print("Start board :", initial, " h =", count_conflicts(initial))
    print("Final board :", final, " h =", h_val)
    if h_val == 0:
        print("Result      : SUCCESS")
    else:
        print("Result      : FAILURE (stuck at a local optimum)")
    print("Iterations  :", iters)
    print("Neighbour evaluations :", evals)
    print()
    display_board(final)
