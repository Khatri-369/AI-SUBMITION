# steepest_hill.py
import random
from nqueens_utils import count_conflicts, generate_neighbors, create_random_board, show_summary

def steepest_climb(board, verbose=False):
    iterations = 0
    evaluations = 0
    current_h = count_conflicts(board)

    while current_h > 0:
        optimal = board
        optimal_h = current_h

        for neighbor in generate_neighbors(board):
            neighbor_h = count_conflicts(neighbor)
            evaluations += 1
            if neighbor_h < optimal_h:
                optimal = neighbor
                optimal_h = neighbor_h

        # No improvement means we hit a plateau or local minimum
        if optimal_h >= current_h:
            break

        board = optimal
        current_h = optimal_h
        iterations += 1
        if verbose:
            print("step", iterations, ":", board, " h =", current_h)

    return board, current_h, iterations, evaluations

if __name__ == "__main__":
    random.seed(23)
    initial = create_random_board()
    print("Steepest Ascent Hill Climbing")
    print("Start board :", initial, " h =", count_conflicts(initial))
    final, h_val, iters, evals = steepest_climb(initial, verbose=True)
    show_summary("Steepest Ascent Hill Climbing", initial, final, h_val, iters, evals)
