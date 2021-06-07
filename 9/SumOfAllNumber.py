def sumOfAllNumer(*array):
    '''
    不定个数的数字，返回所有数字的和
    :param array:待处理列表
    :return:返回各个数字的和
    '''
    sum = 0
    for val in array:
        sum += val
    return sum

print(sumOfAllNumer(1,2,3))
print(sumOfAllNumer(1,2,3,4,5))