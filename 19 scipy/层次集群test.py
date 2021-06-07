#codeing=utf-8
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import xlwings as xw
import random as rn

def readData():
    path = 'LastTest.xlsx'
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(path)
    sheet = wb.sheets['总成绩']

    Students = []
    for i in range(60):
        temp = []
        for j in range(11):
            temp.append(sheet.range(chr(67 + j) + (i + 2).__str__()).value)
        Students.append(temp)

    wb.close()
    app.quit()
    rn.shuffle(Students)
    print(Students)
    return Students

if __name__ == '__main__':
    a = readData()
    X = linkage(a , method='ward')
    plt.figure(figsize=(50, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(X, leaf_rotation=90., leaf_font_size=8.)
    plt.savefig('test.png')
    plt.show()

