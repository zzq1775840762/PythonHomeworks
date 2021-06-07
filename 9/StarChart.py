def printStarChart(n):
    '''
    输出指定行的星星三角形
    :param n: 三角形行数
    :return: none
    '''
    for i in range(1 , n):
        print(" " * (n - i) , end="")
        print("*" * (2 * i - 1))

line = (int)(input())
printStarChart(line)