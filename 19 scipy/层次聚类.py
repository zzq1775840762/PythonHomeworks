import numpy as np
import matplotlib.pyplot as mpl
from scipy.spatial.distance import pdist, squareform
import scipy.cluster.hierarchy as hy

def group(data, index):
    number = np.unique(index)
    groups = []
    for i in number:
        groups.append(data[index == i])
    return groups

def clusters(number=60, cnumber=4, csize=15):
    #聚类服从高斯分布
    rnum = np.random.rand(cnumber, 2)
    rn = rnum[:, 0] * number
    rn = rn.astype(int)
    rn[np.where(rn < 5)] = 5
    rn[np.where(rn > number / 2.)] = round(number / 2., 0)
    ra = rnum[:, 1] * 2.9
    ra[np.where(ra < 1.5)] = 1.5
    cls = np.random.randn(number, 3) * csize
    # Random multipliers for central point of cluster
    rxyz = np.random.randn(cnumber - 1, 3)
    for i in range(cnumber - 1):
        tmp = np.random.randn(rn[i + 1], 3)
    x = tmp[:, 0] + (rxyz[i, 0] * csize)
    y = tmp[:, 1] + (rxyz[i, 1] * csize)
    z = tmp[:, 2] + (rxyz[i, 2] * csize)
    tmp = np.column_stack([x, y, z])
    cls = np.vstack([cls, tmp])
    return cls

# 创建数据
cls = clusters()
# 计算kinkage 矩阵
Y = hy.linkage(cls[:,0:2], method='complete')
# 从层次数据结构中, 用fcluster 函数将层次结构的数据转为flat clusters
cutoff = 0.3 * np.max(Y[:, 2])
index = hy.fcluster(Y, cutoff, 'distance')
# 使用grooup 函数将数据划分类别
groups = group(cls, index)
# 绘制数据点
fig = mpl.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
colors = ['r', 'c', 'b', 'g', 'orange', 'k', 'y', 'gray']
for i, g in enumerate(groups):
    i = np.mod(i, len(colors))
    ax.scatter(g[:, 0], g[:, 1], c=colors[i], edgecolor='none', s=50)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

fig.savefig('cluster_hy_f02.pdf', bbox = 'tight')
mpl.show()

