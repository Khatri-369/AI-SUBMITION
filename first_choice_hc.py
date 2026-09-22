# first_choice_hc.py
import random
from nqueens_utils import count_conflicts, generate_neighbors, create_random_board, show_summary

def first_choice_climb(board, verbose=False):
    iterations = 0
    evaluations = 0
    current_h = count_conflicts(board)

    while current_h > 0:
        candidates = generate_neighbors(board)
        random.shuffle(candidates)
        improved = False

        for neighbor in candidates:
            neighbor_h = count_conflicts(neighbor)
            evaluations += 1
            if neighbor_h < current_h:
                board = neighbor
                current_h = neighbor_h
                iterations += 1
                improved = True
                if verbose:
                    print("step", iterations, ":", board, " h =", current_h)
                break

        if not improved:
            break

    return board, current_h, iterations, evaluations

if __name__ == "__main__":
    random.seed(0)
    initial = create_random_board()
    print("First-Choice Hill Climbing")
    print("Start board :", initial, " h =", count_conflicts(initial))
    final, h_val, iters, evals = first_choice_climb(initial, verbose=True)
    show_summary("First-Choice Hill Climbing", initial, final, h_val, iters, evals)
