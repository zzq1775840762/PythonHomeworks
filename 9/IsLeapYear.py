def isLeapYear(year):
    '''
    判断是否是闰年
    :param year:年份
    :return:判断结果
    '''
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = (int)(input())
print(isLeapYear(year))