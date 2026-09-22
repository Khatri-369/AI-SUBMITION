import heapq
from cities import graph, straight_line_distance
from random_states import test_pairs

def find_cost(path):
    total = 0
    for i in range(len(path) - 1):
        if path[i] in graph:
            for neighbour, cost in graph[path[i]]:
                if neighbour == path[i + 1]:
                    total += cost
                    break
    return total

def a_star(start, goal, verbose=True):
    # Queue stores tuples of (f_cost, g_cost, path)
    # f_cost = g_cost + h_cost
    # Using straight-line distance to goal as admissible heuristic h(n)
    h_start = straight_line_distance(start, goal)
    queue = [(h_start, 0, [start])]
    visited = []
    nodes_explored = 0
    max_stored = len(queue)

    while queue:
        f_cost, g_cost, path = heapq.heappop(queue)
        city = path[-1]

        if city == goal:
            cost = find_cost(path)
            if verbose:
                print("Path :", " -> ".join(path))
                print("Cost :", cost)
                print("Nodes Explored (Time Complexity) :", nodes_explored)
                print("Max Nodes Stored (Space Complexity) :", max_stored)
            return path, cost, nodes_explored, max_stored

        if city not in visited:
            visited.append(city)
            nodes_explored += 1

            if city in graph:
                for neighbour, step_cost in graph[city]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    new_g_cost = g_cost + step_cost
                    h_cost = straight_line_distance(neighbour, goal)
                    new_f_cost = new_g_cost + h_cost
                    heapq.heappush(queue, (new_f_cost, new_g_cost, new_path))

            if len(queue) > max_stored:
                max_stored = len(queue)

    return None, 0, nodes_explored, max_stored

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        start, goal = sys.argv[1], sys.argv[2]
        print(f"Start City : {start}")
        print(f"Goal City  : {goal}")
        a_star(start, goal)
    else:
        print("=" * 70)
        print(" A* SEARCH ALGORITHM - 15 RANDOM INITIAL & FINAL STATES")
        print("=" * 70)
        for idx, (start, goal) in enumerate(test_pairs, 1):
            print(f"\n[Case {idx}] Start: {start} | Goal: {goal}")
            a_star(start, goal)
