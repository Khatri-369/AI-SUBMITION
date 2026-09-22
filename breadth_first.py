from collections import deque
from city_map import road_network

def calculate_cost(route):
    total_dist = 0
    for k in range(len(route) - 1):
        for adj_city, dist in road_network[route[k]]:
            if adj_city == route[k + 1]:
                total_dist += dist
                break
    return total_dist

def bfs(source, destination):
    frontier = deque([[source]])
    explored = set()
    nodes_explored = 0
    max_stored = len(frontier)

    while frontier:
        route = frontier.popleft()
        current_node = route[-1]

        if current_node == destination:
            print("Path :", " -> ".join(route))
            print("Cost :", calculate_cost(route))
            print("Nodes Explored (Time Complexity) :", nodes_explored)
            print("Max Nodes Stored (Space Complexity) :", max_stored)
            return

        if current_node not in explored:
            explored.add(current_node)
            nodes_explored += 1

            for adj_city, dist in road_network[current_node]:
                extended_route = route + [adj_city]
                frontier.append(extended_route)

            if len(frontier) > max_stored:
                max_stored = len(frontier)

if __name__ == "__main__":
    source = input("Start City : ")
    destination = input("Goal City : ")
    bfs(source, destination)
