#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'细胞自动机'

__author__ = 'GameDebug'

import random
import threading
import time
import tkinter.messagebox
import functools
import tkinter as tk  # 使用Tkinter前需要先导入


def creatButtons(window, size):  # 创建按钮的方法
    length = 600 / size - 1
    buttons = []

    def setColor(i, j):  # 颜色转换的功能
        # print(i)
        if buttons[i][j]['bg'] == 'black':
            buttons[i][j]['bg'] = 'white'
        else:
            buttons[i][j]['bg'] = 'black'

    for i in range(size):
        buttons.append([])  # 使用数组管理
        for j in range(size):
            buttons[i].append(tk.Button(master=window, bitmap='gray12', width=length, height=length, bg='white',
                                        command=functools.partial(setColor, i=i, j=j)))
            # 此处内容填入了一个系统自带的位图，便于调节按钮的大小
            # 因为command参数为函数名，无法带参数，故此处借助偏函数，
            buttons[i][j].grid(row=i, column=j, )
            # 借助网格布局，布置出细胞网络
    return buttons


def creatMenu(window, buttons, lock):  # 创建菜单栏
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='选项', menu=filemenu)  # 选项菜单栏

    def start():  # 开始功能
        try:
            lock.release()
        except:
            pass

    def pause():  # 暂停功能
        lock.acquire()

    def reseat():  # 重置功能
        lock.acquire()
        for i in buttons:
            for j in i:
                j['bg'] = 'white'

    def quit():  # 退出功能
        CellLife.stop = True
        window.quit()

    def save():  # 保存功能

        with open('image.txt', 'w') as f:
            for x in range(len(buttons)):
                for y in range(len(buttons[x])):
                    if buttons[x][y]['bg'] == 'black':
                        f.write('[' + str(x) + ',' + str(y) + '],')

    # 将个项功能放在菜单栏中，就是装入那个容器中
    filemenu.add_command(label='开始', command=start)
    filemenu.add_command(label='暂停', command=pause)
    filemenu.add_command(label='重置', command=reseat)
    filemenu.add_command(label='保存', command=save)
    filemenu.add_command(label='退出', command=quit)
    setmenu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label='设置', menu=setmenu)

    speedmenu = tk.Menu()
    setmenu.add_cascade(label='变化速度', menu=speedmenu)

    # 将二级菜单添加到菜单中
    def setSpeed(newspeed):  # 调节速度
        CellLife.speed = newspeed

    # 将几个预设速度添加到二级菜单中，此处仍借助偏函数实现
    speedmenu.add_command(label='慢', command=functools.partial(setSpeed, newspeed=2))
    speedmenu.add_command(label='较慢', command=functools.partial(setSpeed, newspeed=1.5))
    speedmenu.add_command(label='中等', command=functools.partial(setSpeed, newspeed=1))
    speedmenu.add_command(label='快', command=functools.partial(setSpeed, newspeed=0.5))
    speedmenu.add_command(label='极快', command=functools.partial(setSpeed, newspeed=0.1))

    imgmenu = tk.Menu()
    setmenu.add_cascade(label='预设图案', menu=imgmenu)

    def setImg(locs):  # 修改初始图案
        for x in buttons:
            for y in x:
                y['bg'] = 'white'
        for l in locs:
            buttons[l[0]][l[1]]['bg'] = 'black'

    def randImg():  # 随机初始图案
        for x in buttons:
            for y in x:
                if random.choice((True, False)):
                    y['bg'] = 'black'
                else:
                    y['bg'] = 'white'

    # 几个预设的图案
    loc1 = [[3, 25], [3, 28], [4, 24], [5, 24], [5, 28], [6, 24], [6, 25], [6, 26], [6, 27], [12, 21], [12, 22],
            [13, 20], [13, 21], [13, 22], [13, 23], [14, 19], [14, 20], [14, 22], [14, 23], [15, 20], [15, 21],
            [20, 25], [20, 28], [21, 24], [22, 24], [22, 28], [23, 24], [23, 25], [23, 26], [23, 27]]
    loc2 = [[0, 6], [0, 14], [0, 22], [1, 1], [1, 2], [1, 3], [1, 6], [1, 9], [1, 10], [1, 11], [1, 14], [1, 17],
            [1, 18], [1, 19], [1, 22], [1, 25], [1, 26], [1, 27], [2, 6], [2, 14], [2, 22], [4, 2], [4, 10], [4, 18],
            [4, 26], [5, 2], [5, 5], [5, 6], [5, 7], [5, 10], [5, 13], [5, 14], [5, 15], [5, 18], [5, 21], [5, 22],
            [5, 23], [5, 26], [6, 2], [6, 10], [6, 18], [6, 26], [8, 6], [8, 14], [8, 22], [9, 1], [9, 2], [9, 3],
            [9, 6], [9, 9], [9, 10], [9, 11], [9, 14], [9, 17], [9, 18], [9, 19], [9, 22], [9, 25], [9, 26], [9, 27],
            [10, 6], [10, 14], [10, 22], [12, 2], [12, 10], [12, 18], [12, 26], [13, 2], [13, 5], [13, 6], [13, 7],
            [13, 10], [13, 13], [13, 14], [13, 15], [13, 18], [13, 21], [13, 22], [13, 23], [13, 26], [14, 2], [14, 10],
            [14, 18], [14, 26], [16, 6], [16, 14], [16, 22], [17, 1], [17, 2], [17, 3], [17, 6], [17, 9], [17, 10],
            [17, 11], [17, 14], [17, 17], [17, 18], [17, 19], [17, 22], [17, 25], [17, 26], [17, 27], [18, 6], [18, 14],
            [18, 22], [20, 2], [20, 10], [20, 18], [20, 26], [21, 2], [21, 5], [21, 6], [21, 7], [21, 10], [21, 13],
            [21, 14], [21, 15], [21, 18], [21, 21], [21, 22], [21, 23], [21, 26], [22, 2], [22, 10], [22, 18], [22, 26],
            [24, 6], [24, 14], [24, 22], [25, 1], [25, 2], [25, 3], [25, 6], [25, 9], [25, 10], [25, 11], [25, 14],
            [25, 17], [25, 18], [25, 19], [25, 22], [25, 25], [25, 26], [25, 27], [26, 6], [26, 14], [26, 22]]
    loc3 = [[0, 14], [1, 13], [1, 15], [2, 12], [2, 14], [2, 16], [3, 11], [3, 13], [3, 15], [3, 17], [4, 10], [4, 12],
            [4, 14], [4, 16], [4, 18], [5, 9], [5, 11], [5, 13], [5, 15], [5, 17], [5, 19], [6, 8], [6, 10], [6, 12],
            [6, 14], [6, 16], [6, 18], [6, 20], [7, 7], [7, 9], [7, 11], [7, 13], [7, 15], [7, 17], [7, 19], [7, 21],
            [8, 6], [8, 8], [8, 10], [8, 12], [8, 14], [8, 16], [8, 18], [8, 20], [8, 22], [9, 5], [9, 7], [9, 9],
            [9, 11], [9, 13], [9, 15], [9, 17], [9, 19], [9, 21], [9, 23]]
    # 将预设图案添加到二级菜单中
    imgmenu.add_command(label='太空舰队', command=functools.partial(setImg, locs=loc1))
    imgmenu.add_command(label='广场舞', command=functools.partial(setImg, locs=loc2))
    imgmenu.add_command(label='百变脸谱', command=functools.partial(setImg, locs=loc3))
    imgmenu.add_command(label='随机图案', command=randImg)

    def instruction():  # 添加说明
        tkinter.messagebox.showinfo(title='细胞自动机说明', message="细胞自动机介绍：\n"
                                                             "    细胞自动机（cellular automata）是为模拟包括自组织结构在内的复杂现象提供的一个强有力的方法，"
                                                             "也称为元胞自动机（Cellular Automaton）。细胞自动机模型的基本思想是：自然界里许多复杂结构和过程，"
                                                             "归根到底只是由大量基本组成单元的简单相互作用所引起。细胞自动机主要研究由小的计算机或部件，"
                                                             "按邻域连接方式连接成较大的、并行工作的计算机或部件的理论模型。它分为固定值型、周期型、混沌型"
                                                             "以及复杂型。（摘自百度百科）\n细胞自动机规则：\n    每一个小格代表一个细胞，灰色代表死亡，黑色"
                                                             "代表存活，一个细胞周围八个细胞中有2个细胞为存活状态时，细胞保持原状，当周围为3个存活细胞时，该细"
                                                             "胞变为或保持存活状态，其余情况均变为或保持死亡状态。\n操作说明：\n    初始状态下细胞全部为死亡状态，"
                                                             "点击任意细胞可改变其状态。细胞设置完成后点击选项→开始，即可开始运行。使用暂停功能时，细胞自动机暂停"
                                                             "到某一状态。点击重置可以使自动机重置为全部死亡状态。保存功能可将当前所有存活细胞的坐标保存到本地。\n    "
                                                             "设置选项下，可以调节细胞自动机的运行速度以及使用预设图案和随机图案。\n关于软件及作者："
                                                             "\n    软件开源，仅供读者交流学习之用。\n    作者LittleHuang，邮箱：2387143434@qq.com,欢迎来信交流。")

    menubar.add_command(label='说明', command=instruction)
    window.config(menu=menubar)


def dieOrLife(buttons, length, data):  # 判断每一步细胞生死的功能函数
    life = []
    die = []
    # print('running')
    for i in range(length):
        for j in range(length):
            if buttons[i][j]['bg'] == 'black':
                data[i][j] = 1
            else:
                data[i][j] = 0
    for i in range(length):
        for j in range(length):
            sum = 0
            for l in range(-1, 2):
                for m in range(-1, 2):
                    if l + i >= 0 and m + j >= 0 and l + i < length and m + j < length:
                        sum += data[i + l][j + m]
            sum -= data[i][j]
            # print(sum)
            if sum == 2 or sum == 3:
                if sum == 3:  # 繁殖
                    life.append([i, j])
            else:
                die.append([i, j])#死亡
    if len(life) == 0 and len(die) == 0:
        return
    if len(life) != 0:
        for l in life:
            buttons[l[0]][l[1]]['bg'] = 'black'
    if len(die) != 0:
        for d in die:
            buttons[d[0]][d[1]]['bg'] = 'white'


class CellLife():  # 由于需要调节速度，故借助类的属性实现
    speed = 1
    stop = False

    def __init__(self, buttons):
        self.length = len(buttons)
        self.data = [[0 for i in range(self.length)] for j in range(self.length)]

    def cellLife(self):
        while True:
            if self.stop:
                return
            lock.acquire()
            dieOrLife(buttons, self.length, self.data)
            lock.release()
            time.sleep(self.speed)


if __name__ == '__main__':
    window = tk.Tk()  # 创建窗口
    window.title('自动细胞机')  # 窗口标题
    window.geometry('754x754')  # 这里的乘是小x
    buttons = creatButtons(window, 29)  # 创建窗口并制定方格数目
    lock = threading.RLock()  # 借助线程锁机制实现暂停开始功能，防止用户失误多次申请，使用RLock
    lock.acquire()
    cellLife = CellLife(buttons)
    dataThread = threading.Thread(target=cellLife.cellLife)
    # 由于UI界面，必须需要一个线程循环，因此使用多线程，另开一线程进行计算细胞状态
    creatMenu(window, buttons, lock)  # 创建菜单
    dataThread.start()  # 先开启运算线程，由于信号量已经被申请，故不会直接运行而会等待用户按下开始
    # winThread=threading.Thread(target=window.mainloop)
    window.mainloop()  # 主窗口函数
    # winThread.run()
