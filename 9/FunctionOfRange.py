def range(*args):
    '''
    模拟range全功能
    :param args: 可能传入1-3个参数
    :return: range范围内所有数组成的列表
    '''
    list = []
    start = 0
    step = 1
    if len(args) == 1:
        end = args[0]
    elif len(args) >= 2:
        start = args[0]
        end = args[1]
        if len(args) == 3:
            step = args[2]
    while start < end:
        list.append(start)
        start += step
    return list

print(range(10))
print(range(3,10))
print(range(3,10,2))