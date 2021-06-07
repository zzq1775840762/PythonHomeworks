# coding=utf-8
import numpy as np
import random as rm
import time
from mysqlHelper import *

StudentCnt = 100
ProblemCnt = 90

'''
返回一个随机姓名
'''
def radomName():
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"

    lastName = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'

    name = rm.choice(firstName) + rm.choice(lastName)
    if rm.random() > 0.5:
        name += rm.choice(lastName)
    return name

def randomIdList():
    lists = np.random.randint(0 , 200 , StudentCnt).tolist()
    list = np.unique(lists)
    while len(list) < StudentCnt:
        lists.append(np.random.randint(0 , 200));
        list = np.unique(lists)
    return list.tolist()


def randomStudents():
    update('truncate TABLE test')  # 清空表
    delete('delete from user')  # 清空表
    idlist = randomIdList()
    # print(idlist)
    sqls = []
    for id in idlist:
        id += 2201804400
        sql = "insert into user values('{0}', '{1}')".format(id , radomName())
        sqls.append(sql)

    insertList(sqls)


def getUidList():
    sql = 'select id from user'
    uidlist = []
    results = select(sql)
    # print(results)
    for x in results:
        uidlist.append(x[0])
    return uidlist

def getNum():
    x = rm.random()
    if x < 0.5:
        x *= 2
    if x < 0.85:
        x *= 1.75
    elif x < 0.95:
        x *= 2.75
    else:
        x *= 3.75
    return x

def randomScores():
    begin = time.time()
    sqls = []
    update('truncate TABLE test')   #清空表
    uidlist = list(getUidList())
    for uid in uidlist:
        scores = []
        cnt = [0 for i in range(6)]

        t1, t2 = getNum(), rm.random() * 1.3
        while len(scores) < ProblemCnt:
            x = round(np.random.normal(t1, t2))
            if x <= 0 or x > 5:
                continue
            cnt[x] += 1
            scores.append(x)

        print(cnt)
        for tid in range(ProblemCnt):
            sql = "insert into test values(null, '{0}', {1}, {2});".format(uid, tid + 1, scores[tid])
            sqls.append(sql)

    # print(sqls)
    insertList(sqls)
    end = time.time()
    print(end - begin)


if __name__ == '__main__':
    randomStudents()
    randomScores()