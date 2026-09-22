# restart_hill.py
import random
from nqueens_utils import count_conflicts, create_random_board, show_summary
from steepest_hill import steepest_climb

RESTART_LIMIT = 100

def restart_climb(board, verbose=False):
    cumulative_iters = 0
    cumulative_evals = 0
    restart_count = 0

    while True:
        solution, h_val, iters, evals = steepest_climb(board)
        cumulative_iters += iters
        cumulative_evals += evals

        if verbose:
            print("climb", restart_count, ": ended at", solution, " h =", h_val)

        if h_val == 0:
            break
        if restart_count >= RESTART_LIMIT:
            break

        restart_count += 1
        board = create_random_board()

    return solution, h_val, cumulative_iters, cumulative_evals, restart_count

if __name__ == "__main__":
    random.seed(9)
    initial = create_random_board()
    print("Random Restart Hill Climbing")
    print("Start board :", initial, " h =", count_conflicts(initial))
    final, h_val, iters, evals, restarts = restart_climb(initial, verbose=True)
    show_summary("Random Restart Hill Climbing", initial, final, h_val, iters, evals)
    print("Restarts used :", restarts)
