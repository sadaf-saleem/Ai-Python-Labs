import tkinter as tk

N = 8  # You can change this to any number >= 4

class NQueensGUI:
    def __init__(self, root, size):
        self.root = root
        self.size = size
        self.cell_size = 60
        self.canvas = tk.Canvas(root, width=self.size * self.cell_size, height=self.size * self.cell_size)
        self.canvas.pack()
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.solve(0)
        self.draw_board()

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i]:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        return True

    def solve(self, col):
        if col >= self.size:
            return True

        for i in range(self.size):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                if self.solve(col + 1):
                    return True
                self.board[i][col] = 0  # Backtrack

        return False

    def draw_board(self):
        for i in range(self.size):
            for j in range(self.size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                if self.board[i][j] == 1:
                    self.canvas.create_text(x1 + self.cell_size // 2,
                                            y1 + self.cell_size // 2,
                                            text="♛", font=("Arial", 28), fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    root.title(f"{N}-Queens Solution")
    app = NQueensGUI(root, N)
    root.mainloop() 
