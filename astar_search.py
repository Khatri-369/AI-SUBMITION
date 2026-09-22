import heapq
from cities import graph

# Straight-line distance / heuristic table (defaults to 0 if not defined)
heuristics = {}

def find_cost(path):
    total = 0
    for i in range(len(path) - 1):
        if path[i] in graph:
            for neighbour, cost in graph[path[i]]:
                if neighbour == path[i + 1]:
                    total += cost
                    break
    return total

def a_star(start, goal):
    # Queue stores tuples of (f_cost, g_cost, path)
    # f_cost = g_cost + h_cost
    queue = [(0, 0, [start])]
    visited = []
    nodes_explored = 0
    max_stored = len(queue)

    while queue:
        f_cost, g_cost, path = heapq.heappop(queue)
        city = path[-1]

        if city == goal:
            print("Path :", " -> ".join(path))
            print("Cost :", find_cost(path))
            print("Nodes Explored (Time Complexity) :", nodes_explored)
            print("Max Nodes Stored (Space Complexity) :", max_stored)
            return

        if city not in visited:
            visited.append(city)
            nodes_explored += 1

            if city in graph:
                for neighbour, cost in graph[city]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    new_g_cost = g_cost + cost
                    h_cost = heuristics.get(neighbour, 0)
                    new_f_cost = new_g_cost + h_cost
                    heapq.heappush(queue, (new_f_cost, new_g_cost, new_path))

            if len(queue) > max_stored:
                max_stored = len(queue)

if __name__ == "__main__":
    start = input("Start City : ")
    goal = input("Goal City : ")
    a_star(start, goal)
