from collections import deque
from city_map import road_network
from random_states import test_pairs

def calculate_cost(route):
    total_dist = 0
    for k in range(len(route) - 1):
        for adj_city, dist in road_network[route[k]]:
            if adj_city == route[k + 1]:
                total_dist += dist
                break
    return total_dist

def bfs(source, destination, verbose=True):
    frontier = deque([[source]])
    explored = set()
    nodes_explored = 0
    max_stored = len(frontier)

    while frontier:
        route = frontier.popleft()
        current_node = route[-1]

        if current_node == destination:
            cost = calculate_cost(route)
            if verbose:
                print("Path :", " -> ".join(route))
                print("Cost :", cost)
                print("Nodes Explored (Time Complexity) :", nodes_explored)
                print("Max Nodes Stored (Space Complexity) :", max_stored)
            return route, cost, nodes_explored, max_stored

        if current_node not in explored:
            explored.add(current_node)
            nodes_explored += 1

            for adj_city, dist in road_network[current_node]:
                extended_route = route + [adj_city]
                frontier.append(extended_route)

            if len(frontier) > max_stored:
                max_stored = len(frontier)

    return None, 0, nodes_explored, max_stored

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        source, destination = sys.argv[1], sys.argv[2]
        print(f"Start City : {source}")
        print(f"Goal City  : {destination}")
        bfs(source, destination)
    else:
        print("=" * 70)
        print(" BREADTH FIRST SEARCH (BFS) - 15 RANDOM INITIAL & FINAL STATES")
        print("=" * 70)
        for idx, (source, destination) in enumerate(test_pairs, 1):
            print(f"\n[Case {idx}] Start: {source} | Goal: {destination}")
            bfs(source, destination)
