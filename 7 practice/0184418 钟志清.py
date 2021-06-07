import random as rm
import matplotlib.pyplot as plt
import numpy as np

'''
团队类 编号，得分，成员
'''
class Team:
    def __init__(self , id , score , members):
        self.id = id
        self.score = score
        self.members = members

    def __repr__(self):
        return "{0} , {1}".format(self.id , self.score) + str(self.members) + "\n"

'''
返回一个随机姓名
'''
def radomName():
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"

    lastName = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'

    name = firstName[rm.randint(0, len(firstName) - 1)] + lastName[rm.randint(0, len(lastName) - 1)]
    if rm.random() > 0.5:
        name += lastName[rm.randint(0, len(lastName) - 1)]
    return name

'''
返回符合得分区间个数的50个分数并随机打乱
'''
def rodomScore():
    num = [i * 10 for i in range(5, 10)]
    count = [50 - 20 - 10 - 5 - 2, 20, 10, 5 , 2]

    score = []
    for i in range(len(count)):
        for j in range(count[i]):
            score.append(num[i] + rm.randint(0, 10))
    #print(score)
    rm.shuffle(score)
    return score

'''
返回符合总人数的队伍各人数数组
'''
def rondomMembersCount():
    while True:
        sum = 0
        num = []
        for i in range(50):
            rmint = rm.randint(3 , 5)
            num.append(rmint)
            sum += rmint

            if sum > 185:
                break
        if sum == 185:
            return num

'''
将各属性合并成Team类，并返回teams数组
'''
def combination():
    num = rondomMembersCount()
    score = rodomScore()
    teams = []
    for i in range(50):
        name = []
        for j in range(num[i]):
            name.append(radomName())
        teams.append(Team(i + 1 , score[i] , name))
    rm.shuffle(teams)
    return teams

'''
并线输出???
'''
def printTeams(teams):
    for i in range(len(teams)):
        print("队伍编号:{0}\t队伍得分:{1}\t队伍人数:{2}\t队伍成员:{3}"
              .format(teams[i].id , teams[i].score , len(teams[i].members) , teams[i].members))


'''
输出统计各分数段的人数折线图
'''
def printLineChart(teams):
    label = ['[50,60)', '[60,70)', '[70,80)', '[80,90)', '[90,100]']
    count = [0 for i in range(5)]
    for i in range(len(teams)):
        score = teams[i].score
        if score >= 50 and score < 60:
            count[0] += 1
        elif score >= 60 and score < 70:
            count[1] += 1
        elif score >= 70 and score < 80:
            count[2] += 1
        elif score >= 80 and score < 90:
            count[3] += 1
        else:
            count[4] += 1

    # print("123")
    fig, ax = plt.subplots()
    ax.plot(label, count)

    ax.set(xlabel='Different categories', ylabel='Count of people',
           title='Count of people in different categories')
    ax.grid()

    #print(count)

    #fig.savefig("test1.png")
    plt.show()

'''
输出统计各分数段总成绩的柱状图
'''
def printBarChart(teams):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    label = ['[50,60)', '[60,70)', '[70,80)', '[80,90)', '[90,100]']
    y_pos = np.arange(len(label))
    sum = [0 for i in range(5)]
    for i in range(len(teams)):
        score = teams[i].score
        if score >= 50 and score < 60:
            sum[0] += score
        elif score >= 60 and score < 70:
            sum[1] += score
        elif score >= 70 and score < 80:
            sum[2] += score
        elif score >= 80 and score < 90:
            sum[3] += score
        else:
            sum[4] += score

    ax.barh(y_pos, sum, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(label)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Sum of score')
    ax.set_title('Count sum of score in different categories')

    plt.show()

'''
计算各队伍成绩的平均分
'''
def calculateAverage(teams):
    sum = 0
    for i in range(len(teams)):
        sum += teams[i].score
    print("Teams average score is {0}".format(float(sum) / len(teams)))


if __name__ == "__main__":
    teams = combination()
    printTeams(teams)
    printLineChart(teams)
    printBarChart(teams)
    calculateAverage(teams)
