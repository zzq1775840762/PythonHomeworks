def subOddElement(array):
    '''
    返回所有奇数位索引对应的元素
    :param array:待处理列表
    :return:处理后列表
    '''
    list = []
    for i in range(len(array)):
        if i % 2:
            list.append(array[i])
    return list

res = subOddElement([1 , 4 , "dd" , 5 , "s"])
print(res)