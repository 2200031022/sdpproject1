import heapq

def astar(graph, start, goal, heuristic):
    # Priority queue to store (priority, node, path)
    priority_queue = [(0 + heuristic[start], start, [start])]
    visited = set()

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_cost + cost + heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # If the goal is not reachable from the start node

# Define the graph with weighted edges
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (3, 2), (4, 5)],
    2: [(0, 3), (5, 4)],
    3: [(1, 2), (6, 1)],
    4: [(1, 5), (7, 3)],
    5: [(2, 4)],
    6: [(3, 1)],
    7: [(4, 3)]
}

# Define the heuristic function (for simplicity, using a predefined heuristic here)
heuristic = {0: 6, 1: 5, 2: 4, 3: 3, 4: 4, 5: 2, 6: 2, 7: 0}

# Find the path from node 0 to 7 using A* search
start_node = 0
goal_node = 7
path = astar(graph, start_node, goal_node, heuristic)

if path:
    print(f"A* Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
