import tkinter as tk
import random

# Các hằng số biểu thị người chơi
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


# Hàm kiểm tra thắng thua
def check_winner(board):
    # Kiểm tra các hàng, cột, và đường chéo
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:  # Kiểm tra hàng
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:  # Kiểm tra cột
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:  # Kiểm tra đường chéo chính
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:  # Kiểm tra đường chéo phụ
        return board[0][2]

    # Kiểm tra nếu không còn nước đi nào
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return 'Tie'  # Hòa

    return None  # Chưa kết thúc


# Hàm đánh giá trạng thái
def evaluate(board):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    else:
        return 0


# Hàm tìm tất cả các nước đi có thể
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


# Hàm Minimax
def minmax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1:  # Người chơi X thắng
        return score
    if score == -1:  # Người chơi O thắng
        return score
    if score == 0 and all(board[i][j] != EMPTY for i in range(3) for j in range(3)):  # Hòa
        return 0

    if is_maximizing:
        best = -float('inf')  # tạo biến bé nhất
        for move in get_available_moves(board): #duyệt các nước có thể đi
            i, j = move
            board[i][j] = PLAYER_X
            best = max(best, minmax(board, depth + 1, False)) # chọn ra điểm cao nhất
            board[i][j] = EMPTY
        return best
    else:
        best = float('inf')  # Tìm giá trị nhỏ nhất
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = PLAYER_O
            best = min(best, minmax(board, depth + 1, True))
            board[i][j] = EMPTY
        return best


# Hàm tìm nước đi tối ưu cho người chơi X (Max)
def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)

    for move in get_available_moves(board):
        i, j = move
        board[i][j] = PLAYER_X
        move_val = minmax(board, 0, False)
        board[i][j] = EMPTY

        if move_val > best_val:
            best_move = move
            best_val = move_val

    return best_move


# Giao diện Tkinter
class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Khởi tạo bảng trò chơi 3x3
        self.board = [[EMPTY] * 3 for _ in range(3)]
        self.buttons = [[None] * 3 for _ in range(3)]
        self.turn = PLAYER_O  # Bắt đầu với người chơi O
        self.game_over = False

        # Tạo các nút cho bảng trò chơi
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=EMPTY, font=("Arial", 24), width=5, height=2,command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        # Thêm nhãn cho trạng thái
        self.status_label = tk.Label(root, text="Lượt O", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def make_move(self, i, j):
        if self.board[i][j] == EMPTY and not self.game_over:
            # Cập nhật bảng trò chơi
            self.board[i][j] = self.turn
            self.buttons[i][j].config(text=self.turn)

            # Kiểm tra thắng thua
            winner = check_winner(self.board)
            if winner:
                self.game_over = True
                if winner == "Tie":
                    self.status_label.config(text="Hòa!")
                else:
                    self.status_label.config(text=f"{winner} thắng!")
            elif self.turn == PLAYER_O:  # Nếu là lượt của O, máy sẽ chơi
                self.turn = PLAYER_X
                self.root.after(500, self.machine_move)  # Để máy chơi sau một khoảng thời gian ngắn
            else:
                self.turn = PLAYER_O  # Chuyển lượt cho người chơi O

    def machine_move(self):
        if not self.game_over:
            # Máy chơi sẽ đưa ra nước đi tối ưu
            i, j = find_best_move(self.board)
            self.make_move(i, j)


# Tạo giao diện và chạy trò chơi
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
