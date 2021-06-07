#coding=Utf-8
import random as rm
import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

courses = ['语文','数学','英语','物理','化学','地理','历史','政治','体育','音乐','画画']
coursesMax = [120 , 120 , 120 , 70 , 70 , 50 , 50 , 100 , 70 , 30 , 30]

def writeExcel():
    path = 'LastTest.xlsx'
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(path)
    sheet = wb.sheets['总成绩']

    for i in range(60):
        x = rm.random()
        for j in range(11):
            sheet.range(chr(67 + j) + (i + 2).__str__()).value = int(x * coursesMax[j] + rm.randint(-1 , 10))

    wb.save('LastTest.xlsx')
    wb.close()
    app.quit()

def readSubjectData():
    df = pd.read_excel('LastTest.xlsx')  # 这个会直接默认读取到这个Excel的第一个表单
    data = df.values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
    print("读取指定行的数据：\n{0}".format(data))
    return df

def process(df):

    for i in range(0 , len(courses)):
        for j in range(i + 1 , len(courses)):
            x = courses[i]
            y = courses[j]

            # print(df[x + '成绩'])
            y1 = df[y + '成绩']
            X1 = df[x + '成绩']

            n = 60


            plt.scatter(y1, X1)
            plt.savefig('{}_{}.png'.format(x, y))
            plt.clf()



if __name__ == '__main__':
    df = readSubjectData()
    process(df)
    # writeExcel()