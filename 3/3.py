#coding=utf-8
# matrix.py
import random

LENGTH = 3

def createMatrix():
    '''
    create a matrix
    :return:a matrix
    '''
    a = [[0 for i in range(LENGTH)] for i in range(LENGTH)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = random.randint(0, 9)
    return a


def printMatrix(a):
    '''
    :param a: a Matrix
    :return:
    '''
    for i in range(len(a)):
        print(a[i])

def Add(a , b):
    '''
    矩阵相加
    :param a:
    :param b:
    :return:
    '''
    c = [[0 for i in range(LENGTH)] for i in range(LENGTH)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def Sub(a , b):
    '''
    矩阵相减
    :param a:
    :param b:
    :return:
    '''
    c = [[0 for i in range(LENGTH)] for i in range(LENGTH)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] - b[i][j]
    return c

def PointMult(a , b):
    '''
    矩阵点乘
    :param a:
    :param b:
    :return:
    '''
    c = [[0 for i in range(LENGTH)] for i in range(LENGTH)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] * b[i][j]
    return c

def MatrixMult(a , b):
    '''
    矩阵乘
    :param a:
    :param b:
    :return:
    '''
    c = [[0 for i in range(LENGTH)] for i in range(LENGTH)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            sum = 0
            for x in range(len(a[i])):
                sum += a[i][x] * b[x][j]
            c[i][j] = sum
    return c

if __name__ == '__main__':
    a = createMatrix()
    b = createMatrix()
    # printMatrix(Add(a , b))
    # printMatrix(Sub(a , b))
    printMatrix(a)
    printMatrix(b)
    printMatrix(MatrixMult(a, b))