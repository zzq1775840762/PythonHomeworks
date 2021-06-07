# https://blog.csdn.net/weixin_44843629/article/details/115854232
from scipy.optimize import linprog
c = [-7, -5]    #加负号变标准
A = [[1,2], [4,1]]
b = [[28], [42]]
LB = [0,0]
UB = [None]*len(c)
bound = tuple(zip(LB,UB))
res = linprog(c,A,b,None,None,bound)
print(res.fun)
print(res.x)
