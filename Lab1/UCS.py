import heapq

def ucs_tsp(graph, start): # tim chi phi đường đi
    # hàng đợi lưu trữ (chi phí hiện tại, thành phố hiện tại, đường đi đã thăm)
    frontier = [(0, start, [start])]
    visited = set()  # lưu trữ các nơi đã đi

    while frontier:
        current_cost, current_city, path = heapq.heappop(frontier)

        # Nếu đã thăm tất cả các thành phố và quay trở lại điểm bắt đầu
        if len(path) == len(graph) + 1 and current_city == start:
            return (path, current_cost)

        # Duyệt qua các thành phố kề
        for neighbor, travel_cost in graph[current_city].items():
            if neighbor not in path or (len(path) == len(graph) and neighbor == start): # chưa đi hoặc đi 1 vòng xong quay về mà chưa đi hết
                # Tính toán chi phí
                new_cost = current_cost + travel_cost
                # path hiện tại + neighbor
                new_path = path + [neighbor]
                # Đẩy vào hàng đợi
                heapq.heappush(frontier, (new_cost, neighbor, new_path))

    return [], 0

graph = {
    'A': {'B': 1, 'C': 4, 'D': 20},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'A': 20, 'B': 5, 'C': 1}
}

path, total_cost = ucs_tsp(graph, 'A')
print("Đường đi UCS:", path)
print("Chi phí UCS:", total_cost)
