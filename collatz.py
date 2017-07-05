#!/usr/bin/env python
# -*- coding: UTF-8 -*-

count = 0

while True:
    n = raw_input("请输入一个数字: ")
    if n.isdigit():
        while True:
            if int(n) % 2 == 0:
                n = int(n)/2
            else:
                n = int(n)*3+1
            count = count + 1
            if int(n) == 1:
                print ("经过%s次运算得到%s" % (count, n))
                break
    elif n == "exit":
        break
    else:
        print "输入错误，请重新输入!!!"

