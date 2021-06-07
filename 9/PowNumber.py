def powNumber(num):
    '''
    得出任意数的平方数，立方数
    :param num:待计算数字
    :return:平方数和立方数
    '''
    return num ** 2 , num ** 3

num = (int)(input())
nums = powNumber(num)
print("num^2 = {0} , num^3 = {1}".format(nums[0] , nums[1]))