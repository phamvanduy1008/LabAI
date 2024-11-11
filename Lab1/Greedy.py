def greedy_tsp(graph, start):
    # Danh sách các thành phố đã thăm
    visited = [start]
    # Điểm bắt đầu hiện tại
    current = start
    # Chi phí di chuyển
    cost = 0

    # Vòng lặp cho đến khi đã thăm hết các thành phố
    while len(visited) < len(graph):
        # Lấy danh sách các thành phố kề và chi phí đến từ thành phố hiện tại
        next_city, next_cost = min(
            (city, dist) for city, dist in graph[current].items() if city not in visited
        )
        # Di chuyển tới thành phố kế tiếp
        current = next_city
        # Cộng dồn chi phí di chuyển
        cost += next_cost
        # Đánh dấu thành phố đã thăm
        visited.append(current)

    # Quay trở lại thành phố bắt đầu để hoàn thành chu trình
    if start in graph[current]:
        cost += graph[current][start]
        visited.append(start)

    return visited, cost


# Ví dụ đồ thị các thành phố và khoảng cách giữa chúng
graph = {
    'A': {'B': 1, 'C': 4, 'D': 20},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'A': 20, 'B': 5, 'C': 1}
}

# Bắt đầu từ thành phố 'A'
path, total_cost = greedy_tsp(graph, 'A')
print("Đường đi Greedy:", path)
print("Chi phí Greedy:", total_cost)
