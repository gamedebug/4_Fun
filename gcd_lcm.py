#!/usr/bin/env python

def gcd(a, b):

    if a%b == 0: return b
    return gcd(b, a%b)

def lcm(a, b):

    if a > b:
        greater = a
    else:
        greater = b

    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

while True:
    a = input("Input a number: ")
    if isinstance(a, int):
        break
    else:
        print "Input ERROR!!!"

while True:
    b = input("Input another number: ")
    if isinstance(b, int):
        break
    else:
        print "Input ERROR!!!"
print "The GCD is %s" %gcd(a, b)
print "The LCM is %s" %lcm(a, b)
