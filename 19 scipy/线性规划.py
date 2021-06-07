# min
# f = -2x0 + 4x1
# s.t.
# -3x0 +  x1 <= 6
#   x0 + 2x1 >= 4
#   x0 + 3x1  = 4
#         x1 >= -3

import numpy as np
from scipy.optimize import linprog
c = np.array([-2, 4])
a_ub = np.array([[-3, 1], [-1, -2]])
b_ub = np.array([6, -4])
a_ed = np.array([[1, 3]])
b_ed = np.array([4])

# 最小化式子，不等式(小于)系数，不等式常数，等式系数，等式常数，变量左边界，变量右边界
res = linprog(c, a_ub, b_ub, a_ed, b_ed, bounds=([None, None], [-3, None]))

print(res.x)

print(res.fun)
