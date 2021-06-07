import numpy as np
import random as rm
import pandas as pd
import matplotlib.pyplot as plt


matrix1=[[1,9,9,5],[1/9,1,7,1/6],[1/9,1/7,1,1/9],[1/5,6,9,1]]
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
                MatrixMPR[i][j]=round(1/MatrixMPR[j][i],3)

    return MatrixMPR

def getGMPR(MPR):
    '''
    得到中间矩阵G
    :param MPR:
    :return:
    '''
    length=len(MPR)
    G=[[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            sum=0
            for k in range(length):
                sum=sum+MPR[k][j]*MPR[k][j]
            g=MPR[i][j]/pow(sum,1/2)
            G[i][j]=round(g,4)
    return G


def CCI(G):
    '''
    根据R计算
    :param G:
    :return:
    '''
    n=len(G)
    sum=0
    for i in range(n):
        temsum=0
        for j in range(n):
            temsum=temsum+G[i][j]
        sum=sum+temsum*temsum
    CI=pow(sum,1/2)
    CI=CI/n
    return CI


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




def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__=="__main__":
    m = 0
    numb=10000
    list1=['CCI','CI']
    for i in range(m+3,m+16):
        sum1=0
        ls=[]
        for j in range(numb):
            ls1=[]
            matrix = getRandomMatrixMPR(i)
            G=getGMPR(matrix)
            Cci=CCI(G)
            ls1.append(str(Cci))
            CI=getMatrixCI(matrix)
            ls1.append(str(float(CI)))
            ls.append(ls1)

        df = pd.DataFrame(ls, columns=list1)
        df.to_excel('数据.xlsx')
        df = pd.read_excel('数据.xlsx')
        print('\n')
        print('n={}'.format(i))
        print(df.corr('spearman'))
        plt.title('n={}'.format(i))
        y= df[list1[0]]
        X = df[list1[1]]
        plt.scatter(y, X)
        plt.savefig('{}_{}({}).png'.format(list1[0],list1[1],i))
        plt.show()


