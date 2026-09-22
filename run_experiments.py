# run_experiments.py
import random
from nqueens_utils import count_conflicts, create_random_board
from steepest_hill import steepest_climb
from first_choice_hc import first_choice_climb
from stochastic_hc import stochastic_climb
from restart_hill import restart_climb

NUM_TRIALS = 20

def benchmark_algorithm(algo_label, algo_fn, boards):
    """Run one algorithm on every board and print a per-run log. Returns aggregate stats for the summary table."""
    print()
    print("--- " + algo_label + " : " + str(NUM_TRIALS) + " runs ---")
    print("Run | Start h | Result  | Final h | Iters | Evals")
    wins = 0
    sum_iters = 0
    sum_evals = 0
    sum_h = 0

    for idx in range(NUM_TRIALS):
        test_board = boards[idx].copy()
        if algo_label == "Random Restart":
            final, h_val, iters, evals, _ = algo_fn(test_board)
        else:
            final, h_val, iters, evals = algo_fn(test_board)

        outcome = "Success" if h_val == 0 else "Failure"
        if h_val == 0:
            wins += 1
        sum_iters += iters
        sum_evals += evals
        sum_h += h_val

        print("%3d | %7d | %-7s | %7d | %5d | %6d"
              % (idx + 1, count_conflicts(boards[idx]), outcome, h_val, iters, evals))

    return wins, sum_iters / NUM_TRIALS, sum_evals / NUM_TRIALS, sum_h / NUM_TRIALS

if __name__ == "__main__":
    random.seed(21)
    boards = [create_random_board() for _ in range(NUM_TRIALS)]
    algorithms = [
        ("Steepest Ascent", steepest_climb),
        ("First-Choice", first_choice_climb),
        ("Stochastic", stochastic_climb),
        ("Random Restart", restart_climb),
    ]

    summary_rows = []
    for label, fn in algorithms:
        row = (label,) + benchmark_algorithm(label, fn, boards)
        summary_rows.append(row)

    print()
    print("============== OBSERVATION TABLE ==============")
    print("(seed = 21, " + str(NUM_TRIALS) + " runs per algorithm)")
    print()
    print("Algorithm        | Successes (20) | Avg Iterations | Avg Evaluations | Avg Final h")
    print("-" * 82)
    for label, wins, avg_it, avg_ev, avg_h in summary_rows:
        print("%-16s | %14d | %14.2f | %15.2f | %11.2f"
              % (label, wins, avg_it, avg_ev, avg_h))
