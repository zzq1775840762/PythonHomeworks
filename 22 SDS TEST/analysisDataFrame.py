# coding=utf-8
import os
import numpy as np
import pandas as pd
import xlwings as xw
from toDataFrame import *
from mysqlHelper import *
import matplotlib.pyplot as plt

list = [0 for i in range(3)]
heavyList, meddleList = [], []
probelmList = [True,False,True,True,False,
               False,True,True,True,True,
               False,False,True,False,True,
               False,False,False,True,False]

class Student:
    def __init__(self, id, name, score):
        self.id = id;
        self.name = name
        self.score = score

    def __repr__(self):
        return 'id:{0}, name:{1}, score:{2}'.format(self.id, self.name, self.score)

def drawBarPicture():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    name_list = ['轻度抑郁', '中度抑郁', '重度抑郁']
    plt.bar(range(len(list)), list, tick_label=name_list)
    plt.show()

def saveStudentsInExcel():

    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()

    wb.sheets.add('中度学生')
    sheet = wb.sheets['中度学生']
    sheet.range('A1').value = '学号'
    sheet.range('B1').value = '姓名'
    sheet.range('C1').value = '得分'

    i = 1
    for s in meddleList:
        i += 1
        sheet.range('A' + i.__str__()).value = s.id
        sheet.range('B' + i.__str__()).value = s.name
        sheet.range('C' + i.__str__()).value = s.score
    sheet.range("A:C").autofit()

    wb.sheets.add('较重学生')
    sheet = wb.sheets['较重学生']
    sheet.range('A1').value = '学号'
    sheet.range('B1').value = '姓名'
    sheet.range('C1').value = '得分'

    i = 1
    for s in heavyList:
        i += 1
        sheet.range('A' + i.__str__()).value = s.id
        sheet.range('B' + i.__str__()).value = s.name
        sheet.range('C' + i.__str__()).value = s.score

    sheet.range("A:C").autofit()
    sheet = wb.sheets['sheet1']
    sheet.delete()
    wb.save('SeriusStudents.xlsx')
    wb.close()
    app.quit()


def getUidList():
    sql = 'select id from user'
    uidlist = []
    results = select(sql)
    for x in results:
        uidlist.append(x[0])
    return uidlist

def analysis(df):
    uidList = getUidList()
    i = 1

    for uid in uidList:
        sum = 0

        # print(df.iloc[i][2])
        while i < 2000 and uid == df.iloc[i][0]:
            if probelmList[df.iloc[i][2] - 1]:
                sum += df.iloc[i][3]
            else:
                sum += 5 - df.iloc[i][3]
            i += 1

        # print('sum: {0}'.format(sum))
        t = int(sum * 1.25)
        if t >= 53 and t <= 62:
            list[0] += 1
        elif t <= 72:
            list[1] += 1
        elif t >= 73:
            list[2] += 1
            meddleList.append((Student)(df.iloc[i - 1][0], df.iloc[i - 1][1], t))

    print(list)
    print('{0}%'.format(list[2] / 100 * 100))
    heavyList.sort(key=lambda s: (-s.score))
    meddleList.sort(key=lambda s: (-s.score))


if __name__ == '__main__':
    df = getDataFrame(queryAllResult())
    analysis(df)
    # saveStudentsInExcel()
    drawBarPicture()
