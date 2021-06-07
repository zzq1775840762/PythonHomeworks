import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from RandomStudent import *

labels = ['[60,70)', '[70,80)', '[80,90)', '[90,100]']

score_cnt = [0 for i in range(4)]

students = RodomStudents(60)

for i in range(len(students)):
    score = students[i]['score']
    standard = 70
    for j in range(4):
        if score < standard:
            score_cnt[j] += 1
            break;
        standard += 10
        if standard == 100:
            standard += 1;


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, score_cnt, width, label='cnt')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cnt')
ax.set_title('Cnt by group scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)

fig.tight_layout()

plt.show()

