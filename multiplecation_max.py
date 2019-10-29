#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import numpy as np

list = []
n = 1
while True:
    list_len = input("请设置数组长度： ")
    try:
        while n <= int(list_len):
            print("请输入第" + str(n) + "个元素： ", end="")
            number = input()
            try:
                list.append(eval(number))
                n += 1
            except Exception:
                print("元素类型错误！")
            print(list)
    except Exception:
        print("长度数据错误！")
    flag = input("再玩一次？(yes|no)")
    if flag == "yes":
        continue
    else:
        break
        