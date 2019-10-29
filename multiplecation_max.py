#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import numpy as np

list = []
n = 1
while True:
    list_len = input("请设置数组长度：")
    try:
        while n <= int(list_len):
            number = input("请输入一个数字: ")
            try:
                list.append(eval(number))
                n += 1
            except Exception:
                print("输入错误！")
            print(list)
    except Exception:
        print("输入错误！")
    flag = input("再玩一次？(yes|no)")
    if flag == "yes":
        continue
    else:
        break
        