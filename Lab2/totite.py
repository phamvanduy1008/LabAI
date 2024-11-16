import tkinter as tk
import math

# Các biến toàn cục cho trò chơi
current_player = "X"  # Người chơi đi trước
board = [None] * 9  # Bàn cờ trống


# Hàm xác định các điều kiện thắng
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hàng dọc
        [0, 4, 8], [2, 4, 6]  # đường chéo
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != None:
            return board[combo[0]]
    return None


# Kiểm tra hòa
def is_draw():
    return all(cell is not None for cell in board)


# Đánh giá trạng thái của bàn cờ
def evaluate():
    winner = check_winner()
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0


# Thuật toán Max-Min
def max_min(is_maximizing):
    if check_winner() or is_draw():
        return evaluate()

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                max_eval = max(max_eval, max_min(False))
                board[i] = None
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                min_eval = min(min_eval, max_min(True))
                board[i] = None
        return min_eval

def find_best_move():
    best_move = None
    best_value = math.inf
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            move_value = max_min(True)
            board[i] = None
            if move_value < best_value:
                best_value = move_value
                best_move = i
    return best_move


# Xử lý sự kiện nhấn nút
def on_button_click(index):
    global current_player
    if board[index] is None and check_winner() is None:
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner() or is_draw():
            end_game()
            return

        # Đổi lượt chơi
        current_player = 'O' if current_player == 'X' else 'X'

        # Nếu là lượt của máy (O), tìm nước đi tốt nhất
        if current_player == 'O':
            best_move = find_best_move()
            if best_move is not None:
                board[best_move] = 'O'
                buttons[best_move].config(text='O')
                if check_winner() or is_draw():
                    end_game()
                current_player = 'X'


# Kết thúc trò chơi và hiển thị kết quả
def end_game():
    winner = check_winner()
    if winner:
        result_text.set(f"Người chơi {winner} thắng!")
    else:
        result_text.set("Hòa!")
    restart_button.grid(row=4, column=0, columnspan=3)  # Hiển thị nút restart


# Khởi động lại trò chơi
def restart_game():
    global board, current_player
    board = [None] * 9
    current_player = "X"
    result_text.set("")
    for button in buttons:
        button.config(text="")
    restart_button.grid_forget()  # Ẩn nút restart


# Tạo giao diện chính
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 16))
result_label.grid(row=3, column=0, columnspan=3)

# Tạo các nút cho các ô trong bàn cờ
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Tạo nút Restart và ẩn nó lúc đầu
restart_button = tk.Button(root, text="Restart", font=("Arial", 16), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)
restart_button.grid_forget()

# Chạy giao diện
root.mainloop()