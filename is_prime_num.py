#!/usr/bin/env python3


number = input("Input a number: ")

try:
    if type(eval(number)) == int:
        count = 0
        if (int(number) > 1):
            for tmp in range(2, int(number)):
                if (int(number) % tmp) == 0:
                    count += 1
        else:
            print ("Your number isn't prime number.")

        if (count == 0):
            print ("Your number is prime number.")
        else:
            print ("Your number isn't prime number.")
    else:
        print ("Input error!!!")
except:
    print ("Input error!!!")
    pass

