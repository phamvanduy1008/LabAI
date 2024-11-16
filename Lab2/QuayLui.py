
def color_map(graph, colors, node, color_assignment):
    if node == len(graph):
        return True

    # Duyệt qua từng màu
    for color in range(len(colors)):
        if is_safe(graph, node, color, color_assignment):
            color_assignment[node] = color
            # gọi đêj quy để tô node tiếp theo có được k
            if color_map(graph, colors, node + 1, color_assignment):
                return True
            # Quay lui
            color_assignment[node] = None

    return False

# kiểm tra các tô màu này cho node được k
def is_safe(graph, node, color, color_assignment):
    # Kiểm tra tất cả các nút kề, đảm bảo không có nút kề nào có màu giống
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True


# Hàm chính để tô màu bản đồ
def solve_map_coloring(graph, colors):
    color_assignment = [None] * len(graph)  # Tạo 1 list để lưu màu cho từng node ban đầu vùng chưa có màu

    if color_map(graph, colors, 0, color_assignment):
        return color_assignment
    else:
        return None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
colors = ["xanh", "đỏ", "vàng"]

color_assignment = solve_map_coloring(graph, colors)
if color_assignment:
    print("Kết quả tô màu:", [colors[color] for color in color_assignment])
else:
    print("Không tìm được cách tô màu hợp lệ.")
