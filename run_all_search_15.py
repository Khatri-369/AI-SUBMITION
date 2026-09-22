# run_all_search_15.py
# Comprehensive benchmark running BFS, DFS, and A* on 15 Random State Pairs
from random_states import test_pairs
from breadth_first import bfs
from depth_first import dfs
from astar_search import a_star

def run_benchmarks():
    print("=" * 105)
    print("           BENCHMARK OF SEARCH ALGORITHMS (15 RANDOM INITIAL & FINAL STATES)")
    print("=" * 105)
    print(f"{'No.':<4} | {'Initial -> Final State':<32} | {'BFS (Cost / Exp / Max)':<20} | {'DFS (Cost / Exp / Max)':<20} | {'A* (Cost / Exp / Max)':<20}")
    print("-" * 105)

    bfs_costs, bfs_exps, bfs_maxs = [], [], []
    dfs_costs, dfs_exps, dfs_maxs = [], [], []
    ast_costs, ast_exps, ast_maxs = [], [], []

    for idx, (source, dest) in enumerate(test_pairs, 1):
        bp, bc, be, bm = bfs(source, dest, verbose=False)
        dp, dc, de, dm = dfs(source, dest, verbose=False)
        ap, ac, ae, am = a_star(source, dest, verbose=False)

        bfs_costs.append(bc); bfs_exps.append(be); bfs_maxs.append(bm)
        dfs_costs.append(dc); dfs_exps.append(de); dfs_maxs.append(dm)
        ast_costs.append(ac); ast_exps.append(ae); ast_maxs.append(am)

        pair_str = f"{source} -> {dest}"
        b_str = f"{bc} km / {be} / {bm}"
        d_str = f"{dc} km / {de} / {dm}"
        a_str = f"{ac} km / {ae} / {am}"
        print(f"{idx:<4} | {pair_str:<32} | {b_str:<20} | {d_str:<20} | {a_str:<20}")

    print("=" * 105)
    print("AVERAGE METRICS OVER 15 RUNS:")
    n = len(test_pairs)
    print(f"BFS  -> Avg Cost: {sum(bfs_costs)/n:.1f} km | Avg Nodes Explored (Time): {sum(bfs_exps)/n:.1f} | Avg Max Stored (Space): {sum(bfs_maxs)/n:.1f}")
    print(f"DFS  -> Avg Cost: {sum(dfs_costs)/n:.1f} km | Avg Nodes Explored (Time): {sum(dfs_exps)/n:.1f} | Avg Max Stored (Space): {sum(dfs_maxs)/n:.1f}")
    print(f"A*   -> Avg Cost: {sum(ast_costs)/n:.1f} km | Avg Nodes Explored (Time): {sum(ast_exps)/n:.1f} | Avg Max Stored (Space): {sum(ast_maxs)/n:.1f}")
    print("=" * 105)

if __name__ == "__main__":
    run_benchmarks()
