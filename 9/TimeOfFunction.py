import time

def deco(tesePrint):
    startTime = time.time()
    tesePrint()
    endTime = time.time()
    print("执行时间是{0}".format((float)((endTime - startTime) * 1000) - 1000))

@deco
def testPrint():
    '''
    待测试函数
    :return:none
    '''
    time.sleep(1)
    print("你愁啥！")

testPrint