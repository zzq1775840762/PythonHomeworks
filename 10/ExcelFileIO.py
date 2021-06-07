import xlwings as xw
import random as rm

def randomId():
    '''
    返回随机的顺序学号数组
    :return: 学号数组
    '''
    num = []
    while True:
        num.append(201800 + rm.randint(0 , 100))
        setList = list(set(num))    #set去重

        if len(setList) == 60:
            setList.sort()
            return setList

def radomScore():
    '''
    返回符合得分区间个数的50个分数并随机打乱
    :return: 得分数组
    '''
    score = [i * 10 for i in range(6, 10)]
    count = [5 , 15 , 35 , 5]

    s = [0 , 0]
    for i in range(len(count)):
        for j in range(count[i]):
            rmint = rm.randint(0, 10)
            if rmint != 10 and rm.random() > 0.5:
                rmint += 0.5
            s.append(score[i] + rmint)
    #print(s)
    rm.shuffle(s)
    return s

def radomName():
    '''
    生成一个随机姓名
    :return: 随机姓名
    '''
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"

    lastName = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'

    name = firstName[rm.randint(0, len(firstName) - 1)] + lastName[rm.randint(0, len(lastName) - 1)]
    if rm.random() > 0.5:
        name += lastName[rm.randint(0, len(lastName) - 1)]
    return name

def writeExcel():

    app=xw.App(visible=True,add_book=False)
    wb=app.books.add()
    # wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值

    sheet = wb.sheets['sheet1']

    sheet.range('A1').value='学号'
    sheet.range('B1').value='姓名'
    sheet.range('C1').value='成绩'

    id = randomId()
    score = radomScore()
    for i in range(2 , 62):
        sheet.range('A' + i.__str__()).value = id[i - 2]
        sheet.range('B' + i.__str__()).value = radomName()
        sheet.range('C' + i.__str__()).value = score[i - 2]

    wb.save(r'test.xlsx')
    wb.close()
    app.quit()

if __name__ == "__main__":
    writeExcel()