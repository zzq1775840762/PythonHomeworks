import numpy as np
import random as rm
import pandas as pd
import matplotlib.pyplot as plt
from dataAnalysis import analysis


def geteigValue(MatrixMPR):
    '''
    求矩阵得最大特征值
    :param MatrixMPR:
    :return:
    '''
    MatrixMPR=np.array(MatrixMPR)
    eigvalue,eigvector=np.linalg.eig(MatrixMPR)
    maxvalue=max(eigvalue)
    return maxvalue

def getMatrixCI(MatrixMPR):
    maxvalue=geteigValue(MatrixMPR)
    n=len(MatrixMPR)
    CI=(maxvalue-n)/(n-1)
    return CI

constlist=[1/9,1/8,1/7,1/6,1/5,1/4,1/3,1/2,1,2,3,4,5,6,7,8,9]

def getRandomMatrixMPR(n):
    '''
    构造随机的MPR矩阵
    :param n:
    :return:
    '''
    if(n<2):
        return None
    i=0
    MatrixMPR=[]
    while i<n:
        line=[]
        j = 0
        while j<n:
            if(i<j):  #上三角
                k=rm.randrange(0,17)  #从1/9，...，9中取数数据，然后放入判断矩阵中
                #print(k)
                rij = constlist[k]
                line.append(rij)
                j = j + 1
            if(i==j):#添加对角元素,为了程序的规范，这里补全
               line.append(1)
               j=j+1
            if(i>j):#这里默认为0，实际上算完上三角可以快速得到下三角，为了程序的规范，这里补全
                line.append(0)
                j=j+1
        MatrixMPR.append(line)
        i=i+1
    #构造下三角矩阵的
    N=n
    for i in range(N):
        for j in range(N):
            if(i>j):
                MatrixMPR[i][j]=1/MatrixMPR[j][i]

    return MatrixMPR


def getGCI(n,matrix,w):
    '''
    几何一致性指数用来判断MPR的一致性,Row Geometric Mean Method
    Geometric Consistency Index
    :param n:对象个数
    :param matrix:原矩阵
    :param w:所求优先向量
    :return:
    '''
    sum=0
    for i in range(n):
        for j in range(n):
            if(i<j):
                temp=0
                temp=matrix[i][j]*(w[j]/w[i])
                temp=np.log10(temp)
                temp=temp*temp
                sum=sum+temp
    sum=2*sum/((n-2)*(n-1))
    return sum

def RGMM(MPR):
    '''
    几何平均求权重
    :param MPR:
    :return:
    '''
    Weight=[]
    length=len(MPR)
    for i in range(length):
        sumj=1
        for j in range(length):
            sumj = sumj * MPR[i][j]
        sumj=pow(sumj,1/length)
        Weight.append(sumj)
    total=sum(Weight)
    for i in range(length):
        Weight[i]=Weight[i]/total

    return Weight

if __name__=="__main__":
    m=0
    numb=100000
    list1=['CI','GCI']
    for i in range(m+3,m+5):
        sum1=0
        ls=[]
        for j in range(numb):
            ls1=[]
            matrix = getRandomMatrixMPR(i)
            CI = getMatrixCI(matrix)
            W = RGMM(matrix)
            length = len(matrix)
            GCI = getGCI(length, matrix, W)
            ls1.append(float(CI))
            ls1.append(GCI)
            ls.append(ls1)

        analysis(list1, ls, i)