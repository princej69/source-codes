# IncreaseBackAndForthWithMax.py
# This file shows how to increase the specified number back and forth with the max.
# By PJ Satur
# On July 9, 2022

import random

def checkifmaxisgreaterthanmin():
    if max >= min:
        return True
    else:
        return False

min = int(input("Enter Minimum: "))
max = int(input("Enter Maximum: "))
stp = int(input("Stop When At "))
sp  = input("Enter Starting Point: (0) ")

if sp == "":
    sp = 0
else:
    sp = int(sp)

val = sp

if checkifmaxisgreaterthanmin():
    count=1
    while val < stp:
        increase = random.randint(min,max)
        val+=increase
        print(str(count) + ": " + str(val) + " (+" + str(increase) + ")")
        count+=1
else:
    print("ERROR!")
    print("--------------")
    print("Min is greater than Max.")