# coding=utf-8
import os

courses = ['语文','数学','英语','物理','化学','地理','历史','政治','体育','音乐','画画']

grades = ['初一' , '初二' , '初三']

def UnitTest(year , grade , term , subject):

    now = os.getcwd()
    t = '上学期' if term == 0 else '下学期'
    path = '\\UnitTestData\\' + year.__str__() + '级\\' + grades[grade - 1] + '\\' + t + '\\' + subject
    os.makedirs(now + path)


if __name__ == '__main__':
    UnitTest(2016 , 2 , 1 , '化学')