# stochastic_hc.py
import random
from nqueens_utils import count_conflicts, generate_neighbors, create_random_board, show_summary

def stochastic_climb(board, verbose=False):
    iterations = 0
    evaluations = 0
    current_h = count_conflicts(board)

    while current_h > 0:
        improving = []
        for neighbor in generate_neighbors(board):
            neighbor_h = count_conflicts(neighbor)
            evaluations += 1
            if neighbor_h < current_h:
                improving.append(neighbor)

        if not improving:
            break

        board = random.choice(improving)
        current_h = count_conflicts(board)
        iterations += 1
        if verbose:
            print("step", iterations, ":", board, " h =", current_h,
                  " (picked from", len(improving), "better neighbours)")

    return board, current_h, iterations, evaluations

if __name__ == "__main__":
    random.seed(8)
    initial = create_random_board()
    print("Stochastic Hill Climbing")
    print("Start board :", initial, " h =", count_conflicts(initial))
    final, h_val, iters, evals = stochastic_climb(initial, verbose=True)
    show_summary("Stochastic Hill Climbing", initial, final, h_val, iters, evals)
