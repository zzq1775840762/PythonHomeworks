import os
import sys

a = 2
b = 3
for i in range(123456 - 1):
  x , y = a , b
  a = 2 * x - 3 * y
  b = 3 * x + 2 * y

if b > 0:
  print(a , '+' , b , 'i' , sep = '')
else:
  print(a , b , 'i' , sep = '')
