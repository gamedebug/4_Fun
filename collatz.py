#!/usr/bin/env python

count = 0
n = input("Enter a number: ")
while True:
    if n%2 == 0:
        n = n/2
    else:
        n = n*3+1
    count = count + 1
    if n == 1:
        break
print n
print count
