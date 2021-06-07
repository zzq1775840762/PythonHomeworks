def subArrary(arrary):
    '''
    如果列表长度大于2，则返回前两个
    :param arrary:待处理列表
    :return:切割后的数组
    '''
    if(len(arrary) > 2):
        arrary = arrary[:2]
    return arrary

res = subArrary([1 , 2 , 3 , "abc"])
print(res)