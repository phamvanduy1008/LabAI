import tkinter as tk
import math

# Hàm kiểm tra nếu người chơi chiến thắng
def check_winner(board, player):
    # Kiểm tra hàng, cột và hai đường chéo xem tất cả ô có cùng ký hiệu không
    return any(all(spot == player for spot in row) for row in board) or \
           any(all(board[r][c] == player for r in range(3)) for c in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

# Hàm kiểm tra nếu trò chơi hòa (không còn ô trống)
def is_draw(board):
    return all(spot != ' ' for row in board for spot in row)

# Thuật toán Minimax tính điểm cho mỗi trạng thái của bảng
def minimax(board, is_maximizing):
    if check_winner(board, 'O'): return 10  # Máy thắng trả về 10
    if check_winner(board, 'X'): return -10  # Người thắng trả về -10
    if is_draw(board): return 0  # Hòa trả về 0

    # Khởi tạo giá trị tốt nhất
    best_score = -math.inf if is_maximizing else math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # Nếu ô trống
                board[i][j] = 'O' if is_maximizing else 'X'  # Tạm thời đánh dấu nước đi
                score = minimax(board, not is_maximizing)  # Đệ quy Minimax
                board[i][j] = ' '  # Khôi phục ô trống sau khi đánh giá
                # Cập nhật điểm tốt nhất cho chế độ tối đa hóa hoặc tối thiểu hóa
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

# Tìm nước đi tốt nhất cho máy tính
def find_best_move(board):
    best_move, best_score = (-1, -1), -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # Tạm thời đánh dấu nước đi cho máy
                score = minimax(board, False)  # Tính điểm bằng Minimax
                board[i][j] = ' '  # Khôi phục ô trống sau khi đánh giá
                if score > best_score:  # Cập nhật nước đi tốt nhất nếu điểm cao hơn
                    best_score, best_move = score, (i, j)
    return best_move

# Hàm giới hạn nước đi: xóa nước đầu tiên khi người chơi có hơn 3 nước
def manage_moves(moves, board):
    if len(moves) > 3:
        x, y = moves.pop(0)  # Xóa nước đầu tiên khỏi danh sách
        board[x][y], buttons[x][y]["text"] = ' ', ' '  # Cập nhật bảng và giao diện

# Hàm khi người chơi nhấp vào một ô
def on_click(row, col):
    if board[row][col] == ' ' and not game_over:  # Kiểm tra ô trống và trò chơi chưa kết thúc
        board[row][col], buttons[row][col]["text"] = 'X', 'X'  # Đặt nước đi của người chơi
        player_moves.append((row, col))  # Lưu nước đi vào danh sách
        manage_moves(player_moves, board)  # Giới hạn nước đi của người chơi

        if check_winner(board, 'X'):  # Kiểm tra người chơi thắng
            status_label["text"] = "Bạn thắng!"
            end_game()
        elif is_draw(board):  # Kiểm tra nếu hòa
            status_label["text"] = "Hòa!"
            end_game()
        else:
            # Máy tính thực hiện nước đi
            x, y = find_best_move(board)
            if (x, y) != (-1, -1):
                board[x][y], buttons[x][y]["text"] = 'O', 'O'  # Đặt nước đi của máy
                computer_moves.append((x, y))  # Lưu nước đi vào danh sách
                manage_moves(computer_moves, board)  # Giới hạn nước đi của máy
                if check_winner(board, 'O'):  # Kiểm tra máy thắng
                    status_label["text"] = "Máy thắng!"
                    end_game()
                elif is_draw(board):  # Kiểm tra nếu hòa
                    status_label["text"] = "Hòa!"
                    end_game()

# Hàm kết thúc trò chơi: khóa tất cả các nút lại
def end_game():
    global game_over
    game_over = True
    for row in buttons:
        for button in row:
            button.config(state='disabled')  # Vô hiệu hóa nút khi trò chơi kết thúc

# Khởi tạo giao diện trò chơi
root = tk.Tk()
root.title("Tic Tac Toe")
board = [[' ' for _ in range(3)] for _ in range(3)]  # Bảng Tic Tac Toe 3x3
buttons = [[tk.Button(root, text=' ', font=('Arial', 24), width=5, height=2,
                      command=lambda r=i, c=j: on_click(r, c)) for j in range(3)] for i in range(3)]
# Đặt các nút trên giao diện
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

status_label = tk.Label(root, text="Lượt của bạn", font=('Arial', 14))
status_label.grid(row=3, column=0, columnspan=3)  # Hiển thị trạng thái trò chơi

game_over = False  # Biến trạng thái trò chơi
player_moves, computer_moves = [], []  # Danh sách lưu nước đi của người chơi và máy

root.mainloop()  # Bắt đầu vòng lặp giao diện
