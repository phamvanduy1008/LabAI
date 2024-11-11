import heapq

def heuristic(city, unvisited, graph):
    """Hàm heuristic đơn giản: chọn cạnh có chi phí thấp nhất từ thành phố hiện tại đến bất kỳ thành phố chưa thăm."""
    if not unvisited:
        return 0  # Không còn thành phố để thăm, nên chi phí heuristic là 0
    return min(graph[city][next_city] for next_city in unvisited)

def a_star_tsp(graph, start):
    # Hàng đợi ưu tiên lưu trữ (chi phí ước tính, chi phí hiện tại, đường đi, các thành phố chưa thăm)
    frontier = [(0, 0, [start], set(graph.keys()) - {start})]

    while frontier:
        estimated_total_cost, current_cost, path, unvisited = heapq.heappop(frontier)

        # Kiểm tra nếu tất cả các thành phố đã thăm
        if not unvisited:
            # Thêm chi phí quay lại điểm bắt đầu
            total_cost = current_cost + graph[path[-1]][start]
            return path + [start], total_cost  # Trả về đường đi hoàn thành và tổng chi phí

        # Duyệt qua các thành phố chưa thăm
        for next_city in unvisited:
            new_path = path + [next_city]
            new_cost = current_cost + graph[path[-1]][next_city]
            new_unvisited = unvisited - {next_city}
            # Tính chi phí ước tính tổng cộng
            estimated_cost = new_cost + heuristic(next_city, new_unvisited, graph)
            # Đẩy vào hàng đợi ưu tiên
            heapq.heappush(frontier, (estimated_cost, new_cost, new_path, new_unvisited))

    return [], float('inf')  # Nếu không tìm thấy đường đi

# Ví dụ về đồ thị các thành phố và khoảng cách giữa chúng
graph = {
    'A': {'B': 1, 'C': 4, 'D': 20},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'A': 20, 'B': 5, 'C': 1}
}
# Bắt đầu từ thành phố 'A'
start_city = 'A'
path, total_cost = a_star_tsp(graph, start_city)
print("Đường đi A*:", path)
print("Chi phí A*:", total_cost)

