#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np

x = int(raw_input("请输入取样空间: "))
for i in range(0,x):
    b = np.random.randint(1,33,5)
    if len(set(b)) == 1:
        print(str(b) + "高资！")
#    else:
#        print str(b) + "渣渣！"
