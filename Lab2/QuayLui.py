def color_map(graph, colors, node, color_assignment):
    # Nếu tất cả các nút đã được tô màu hợp lệ, trả về True
    if node == len(graph):
        return True

    # Duyệt qua từng màu và thử tô màu cho nút hiện tại
    for color in range(len(colors)):
        if is_safe(graph, node, color, color_assignment):
            color_assignment[node] = color  # Tô màu cho nút
            # Thử tô màu cho các nút tiếp theo
            if color_map(graph, colors, node + 1, color_assignment):
                return True
            # Quay lui nếu không tìm được màu hợp lệ
            color_assignment[node] = None

    return False  # Không tìm được cách tô màu hợp lệ


# Hàm kiểm tra xem màu sắc có hợp lệ không
def is_safe(graph, node, color, color_assignment):
    # Kiểm tra tất cả các nút kề, đảm bảo không có nút kề nào có màu giống
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True


# Hàm chính để tô màu bản đồ
def solve_map_coloring(graph, colors):
    color_assignment = [None] * len(graph)  # Khởi tạo màu cho các nút

    if color_map(graph, colors, 0, color_assignment):
        return color_assignment  # Trả về kết quả tô màu
    else:
        return None  # Không tìm được cách tô màu


# Ví dụ đồ thị mô tả bản đồ
# Mỗi vùng là một nút, và các cạnh đại diện cho các biên giới
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Các màu để sử dụng
colors = ["xanh", "đỏ", "vàng"]

# Giải bài toán tô màu bản đồ
color_assignment = solve_map_coloring(graph, colors)
if color_assignment:
    print("Kết quả tô màu:", [colors[color] for color in color_assignment])
else:
    print("Không tìm được cách tô màu hợp lệ.")
