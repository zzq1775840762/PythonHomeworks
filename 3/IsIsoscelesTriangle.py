a = int(input())
b = int(input())
c = int(input())

num = [a , b , c]
num.sort()

if num[0] + num[1] > num[2]:
    if a == b or b == c or a == c:
        print("Is Isosceles Triangle")
    else:
        print("Not Isosceles Triangle")
else:
    print("Not Triangle")