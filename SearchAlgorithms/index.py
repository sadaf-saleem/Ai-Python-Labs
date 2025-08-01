



import random
import heapq
from collections import deque

def open_list_search(initial_node, target_node, get_child_nodes):
    open_list = [initial_node]
    closed_list = set()

    while open_list:
        x = open_list.pop(0)
        if x == target_node:
            return "Success"
        closed_list.add(x)
        S = get_child_nodes(x)
        for x_prime in S:
            if x_prime not in closed_list:
                open_list.append(x_prime)
    return "Failure"


def uniform_cost_search(initial_node, target_node, get_child_nodes, get_cost):
    open_list = [(0, initial_node, [])]
    closed_list = set()

    while open_list:
        cost, x, path = heapq.heappop(open_list)
        if x == target_node:
            return "Success", path + [x]
        if x not in closed_list:
            closed_list.add(x)
            S = get_child_nodes(x)
            for x_prime in S:
                if x_prime not in closed_list:
                    new_cost = cost + get_cost(x, x_prime)
                    heapq.heappush(open_list, (new_cost, x_prime, path + [x]))
    return "Failure", []


def random_search(initial_node, target_node, get_child_nodes, max_attempts=10):
    for _ in range(max_attempts):
        x = initial_node
        visited = set()
        path = [x]

        while x != target_node:
            visited.add(x)
            S = get_child_nodes(x)
            if not S:
                break
            unvisited_nodes = [node for node in S if node not in visited]
            if not unvisited_nodes:
                break
            x = random.choice(unvisited_nodes)
            path.append(x)

        if x == target_node:
            return "Success", path

    return "Failure", []


def closed_list_search(initial_node, target_node, get_child_nodes):
    queue = deque([(initial_node, [initial_node])])
    closed_list = set()

    while queue:
        x, path = queue.popleft()
        if x == target_node:
            return "Success", path
        closed_list.add(x)
        S = get_child_nodes(x)
        for x_prime in S:
            if x_prime not in closed_list:
                queue.append((x_prime, path + [x_prime]))
    return "Failure", []


def dfs(initial_node, target_node, get_child_nodes):
    stack = [(initial_node, [initial_node])]
    visited = set()

    while stack:
        x, path = stack.pop()
        if x == target_node:
            return "Success", path
        visited.add(x)
        for x_prime in reversed(get_child_nodes(x)):
            if x_prime not in visited:
                stack.append((x_prime, path + [x_prime]))
    return "Failure", []


def greedy_best_first_search(initial_node, target_node, get_child_nodes, heuristic):
    open_list = [(heuristic(initial_node), initial_node, [])]
    closed_list = set()

    while open_list:
        _, x, path = heapq.heappop(open_list)
        if x == target_node:
            return "Success", path + [x]
        if x not in closed_list:
            closed_list.add(x)
            for x_prime in get_child_nodes(x):
                if x_prime not in closed_list:
                    heapq.heappush(open_list, (heuristic(x_prime), x_prime, path + [x]))
    return "Failure", []


def best_first_search(initial_node, target_node, get_child_nodes, heuristic):
    return greedy_best_first_search(initial_node, target_node, get_child_nodes, heuristic)


def a_star_search(initial_node, target_node, get_child_nodes, heuristic, get_cost):
    open_list = [(heuristic(initial_node), 0, initial_node, [])]
    closed_list = set()

    while open_list:
        f, g, x, path = heapq.heappop(open_list)
        if x == target_node:
            return "Success", path + [x]
        if x not in closed_list:
            closed_list.add(x)
            for x_prime in get_child_nodes(x):
                if x_prime not in closed_list:
                    new_g = g + get_cost(x, x_prime)
                    new_f = new_g + heuristic(x_prime)
                    heapq.heappush(open_list, (new_f, new_g, x_prime, path + [x]))
    return "Failure", []


def create_graph():
    graph = {}
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        connections = input(f"Enter connections for node {node} (comma-separated): ").split(',')
        connections = [c.strip() for c in connections if c.strip()]
        graph[node] = connections
    return graph


def create_costs(graph):
    costs = {}
    for node in graph:
        for neighbor in graph[node]:
            cost = input(f"Enter the cost from {node} to {neighbor}: ")
            costs[(node, neighbor)] = int(cost)
    return costs


def create_heuristics(graph):
    heuristics = {}
    for node in graph:
        h = input(f"Enter heuristic value for {node}: ")
        heuristics[node] = int(h)
    return heuristics


graph = create_graph()
costs = create_costs(graph)
heuristics = create_heuristics(graph)

initial_node = input("Enter the initial node: ")
target_node = input("Enter the target node: ")

def get_child_nodes(node):
    return graph.get(node, [])

def get_cost(node1, node2):
    return costs.get((node1, node2), float('inf'))

def heuristic(node):
    return heuristics.get(node, 0)

while True:
    print("\n--- Choose Search Algorithm ---")
    print("1. Closed List Search (BFS)")
    print("2. Open List Search")
    print("3. Uniform Cost Search")
    print("4. Random Search")
    print("5. DFS")
    print("6. Greedy Best First Search")
    print("7. Best First Search")
    print("8. A* Search")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        result, path = closed_list_search(initial_node, target_node, get_child_nodes)
        print("Closed List Search Result:", result)
        print("Path:", path)

    elif choice == '2':
        result = open_list_search(initial_node, target_node, get_child_nodes)
        print("Open List Search Result:", result)

    elif choice == '3':
        result, path = uniform_cost_search(initial_node, target_node, get_child_nodes, get_cost)
        print("Uniform Cost Search Result:", result)
        print("Path:", path)

    elif choice == '4':
        result, path = random_search(initial_node, target_node, get_child_nodes)
        print("Random Search Result:", result)
        print("Path:", path)

    elif choice == '5':
        result, path = dfs(initial_node, target_node, get_child_nodes)
        print("DFS Result:", result)
        print("Path:", path)

    elif choice == '6':
        result, path = greedy_best_first_search(initial_node, target_node, get_child_nodes, heuristic)
        print("Greedy Best First Search Result:", result)
        print("Path:", path)

    elif choice == '7':
        result, path = best_first_search(initial_node, target_node, get_child_nodes, heuristic)
        print("Best First Search Result:", result)
        print("Path:", path)

    elif choice == '8':
        result, path = a_star_search(initial_node, target_node, get_child_nodes, heuristic, get_cost)
        print("A* Search Result:", result)
        print("Path:", path)

    elif choice == '9':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option (1-9).")