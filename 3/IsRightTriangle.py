import math
a = int(input())
b = int(input())
c = int(input())

num = [a , b , c]
num.sort()

if num[0] + num[1] > num[2]:
    if pow(num[0] , 2) + pow(num[1] , 2) == pow(num[2] , 2) :
        print("Is Right Triangle")
    else:
        print("Not Right Triangle")
else:
    print("Not Triangle")