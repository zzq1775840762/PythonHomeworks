# coding=utf-8
import numpy as np
import pandas as pd
from mysqlHelper import *


def queryAllResult():
    sql = 'select uid, name, tid, score from test,user where test.uid = user.id'
    return select(sql)

def getDataFrame(results):
    lists = []
    for row in results:
        list = [row[0], row[1], row[2], row[3]]
        lists.append(list)
    return pd.DataFrame(lists)

if __name__ == '__main__':
    results = queryAllResult()
    df = getDataFrame(results)
    print(df)

