import matplotlib.pyplot as plt
import pandas as pd

def analysis(list1,ls,i):

    df = pd.DataFrame(ls, columns=list1)
    df.to_excel('数据.xlsx')
    df = pd.read_excel('数据.xlsx')
    print('\n')
    print('n={}'.format(i))
    print(df.corr('spearman'))
    plt.title('n={}'.format(i))
    y = df[list1[0]]
    X = df[list1[1]]
    plt.scatter(y, X)
    plt.savefig('{}_{}({}).png'.format(list1[0], list1[1], i))
    plt.clf()