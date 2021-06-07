def lenOfString(string):
    '''
    遍历计算字符串的长度
    :param string:待计算的字符串
    :return: 字符串长度
    '''
    cnt = 0
    for x in string:
        cnt += 1
    return cnt

print(lenOfString("123456"))