import random
import tkinter as tk

# 游戏板块的大小
ROW, COL = 10, 10
# 雷的数量
MINES_NUM = 10

# 游戏板块的状态
HIDDEN = -1
MINE = -2
EMPTY = 0

# 游戏状态
PLAYING = 0
WIN = 1
LOSE = -1

# 初始化游戏板块
board = [[HIDDEN for i in range(COL)] for j in range(ROW)]

# 随机生成雷的位置
mines = random.sample(range(ROW * COL), MINES_NUM)
for idx in mines:
    row, col = divmod(idx, COL)
    board[row][col] = MINE

# 计算每个格子周围雷的数量
for i in range(ROW):
    for j in range(COL):
        if board[i][j] == MINE:
            continue
        count = 0
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < ROW and 0 <= nj < COL and board[ni][nj] == MINE:
                    count += 1
        board[i][j] = count

# 创建主窗口
root = tk.Tk()
root.title('扫雷游戏')

# 创建游戏板块
board_frame = tk.Frame(root)
board_frame.pack()

# 创建按钮
buttons = []
for i in range(ROW):
    row = []
    for j in range(COL):
        button = tk.Button(board_frame, text=' ', width=2, height=1)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# 游戏状态
state = PLAYING

# 翻开格子函数
def reveal(x, y):
    global state
    if board[x][y] == MINE:
        state = LOSE
        buttons[x][y].config(text='*', bg='red')
        # 显示所有雷的位置
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == MINE:
                    buttons[i][j].config(text='*', bg='red')
    else:
        buttons[x][y].config(text=board[x][y])
        board[x][y] = EMPTY
        if board[x][y] == 0:
            # 翻开周围8个格子
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = x + di, y + dj
                    if 0 <= ni < ROW and 0 <= nj < COL and board[ni][nj] != MINE and buttons[ni][nj]['state'] != 'disabled':
                        reveal(ni, nj)

    # 判断是否胜利
    if all(all(cell == EMPTY or cell == MINE for cell in row) for row in board):
        state = WIN
        # 显示所有雷的位置
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == MINE:
                    buttons[i][j].config(text='*', bg='green')

# 点击按钮的事件处理函数
def button_click(x, y):
    if state == PLAYING:
        buttons[x][y].config(state='disabled')
        reveal(x, y)
        if state == LOSE:
            print('你输了！')
        elif state == WIN:
            print('你赢了！')

# 绑定按钮事件
for i in range(ROW):
    for j in range(COL):
        buttons[i][j].config(command=lambda x=i, y=j: button_click(x, y))

# 运行主循环
root.mainloop()
