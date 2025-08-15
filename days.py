#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

date1 = raw_input("请输入起始日期（Y/M/D）：")
date2 = raw_input("请输入结束日期（Y/M/D）：")

d1 = datetime.datetime(int(date1.split('/')[0]), 
                       int(date1.split('/')[1]), 
                       int(date1.split('/')[2]))
d2 = datetime.datetime(int(date2.split('/')[0]), 
                       int(date2.split('/')[1]), 
                       int(date2.split('/')[2]))
print("总天数为: " + str((d2-d1).days))
