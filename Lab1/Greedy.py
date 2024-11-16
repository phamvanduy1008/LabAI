def greedy_tsp(graph, start): # tim chi phi ươc tinh nho nhat
    visited = [start]
    current = start
    cost = 0

    while len(visited) < len(graph):
        # Lấy thành phố kề và chi phí đến từ thành phố hiện tại
        next_city, next_cost = min(
            (city, dist) for city, dist in graph[current].items() if city not in visited
        )
        current = next_city
        cost += next_cost
        visited.append(current)

    if start in graph[current]: # kiem tra neu current quai lai start thì quay
        cost += graph[current][start]
        visited.append(start)

    return visited, cost

graph = {
    'A': {'B': 1, 'C': 4, 'D': 20},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'A': 20, 'B': 5, 'C': 1}
}
path, total_cost = greedy_tsp(graph, 'A')
print("Đường đi Greedy:", path)
print("Chi phí Greedy:", total_cost)
