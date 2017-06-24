#!/usr/bin/env python

count = 0

while True:
    n = raw_input("Enter a number: ")
    if n.isdigit():
        break
    else:
        print "Fuck you!!! Enter again!!!"

while True:
    if int(n)%2 == 0:
        n = int(n)/2
    else:
        n = int(n)*3+1
    count = count + 1
    if int(n) == 1:
        break
print n
print count
