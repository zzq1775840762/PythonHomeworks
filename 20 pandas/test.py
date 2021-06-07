import numpy as np
import pandas as pd
# np.random.seed(10)
# a = np.random.randint(size = 1000, low = 1, high = 4)
# print(a)
# print(pd.unique(a),'\n') # 去重
# print(pd.value_counts(a)) # 水平统计


# np.random.seed(100)
# a = pd.Series(np.random.randint(size = 1000, low = 1, high = 101))
# print(a.describe())

import pandas as pd
population={'city':['Beijing','Shanghai','Guangzhou','Shenzhen','Hangzhou','Chongqing'],
            'year':[2016,2017,2016,2017,2016,2016],
            'population':[2100,2300,1000,700,500,500] }
population=pd.DataFrame(population)   ###
print(population)


