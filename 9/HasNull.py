def hasNull(lists):
    '''
    判断用户传入的对象（字符串、列表、元组）的值是否有空值
    :param lists:待判断数组
    :return:判断结果
    '''
    for x in lists:
        if len(x) == 0:
            return True
    return False

print(hasNull(["1","e","w"]))
print(hasNull(["1","e","w",""]))