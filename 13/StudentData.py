# coding=utf-8
import random as rm
import xlwings as xw
import os

teacherCount = 150

classesCount = 10

classesCountMin , classesCountMax = 55 , 65

teacherCourseCount = [15, 15, 15, 10, 5, 15, 15, 15, 15, 15, 15]

class Student:
    def __init__(self , id , name , sex , age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.isGoodStudent = True if rm.random() < 0.8 else False
        self.isWeekMath = False
        self.isWeekChinese = False

    def __repr__(self):
        return "id = {0}, name = {1} , sex = {2} , age = {3}".format(self.id , self.name , self.sex , self.age)

def radomName():
    '''
    生成随机姓名
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

def randomStudentId(grade):
    return 200000000 + grade * 10000 + rm.randint(0 , 9999)

def randomStudentIdList(grade):
    sidList = []
    while True:
        sidList.append(randomStudentId(grade))
        setList = list(set(sidList))    #set去重

        if len(setList) == teacherCount:
            setList.sort()
            return setList

def randomSingalStudent(*args):
    grade = args[0]
    sex = '男' if rm.random() > 0.5 else '女'
    if len(args) > 1:
        sex = args[1]
    student = Student(randomStudentId(grade) , radomName() , sex , 2032 - grade - rm.randint(-1 , 1))
    #print(student)
    return student

def randomSeriesStudent(first):
    while(True):
        classes = []
        stuCount = []
        sum = 0
        for i in range(10):
            num = rm.randint(classesCountMin , classesCountMax)
            stuCount.append(num)
            sum += num
            classes.append(num)
        if sum % 100 != 0:
            continue

        boysCount , girlsCount = sum * 0.49 , sum * 0.51
        ids = []
        Students = []
        while boysCount > 0:
            temp = randomSingalStudent(first , '男')
            if(ids.count(temp.id) > 0):
                continue
            ids.append(temp.id)
            Students.append(temp)
            boysCount -= 1

        while girlsCount > 0:
            temp = randomSingalStudent(first , '女')
            if(ids.count(temp.id) > 0):
                continue
            ids.append(temp.id)
            Students.append(temp)
            girlsCount -= 1

        Students.sort(key=lambda s: (s.id))      #根据学号排序

        SeriesStudents = []
        l , r = 0 , 0
        for i in range(len(stuCount)):          #分班级
            r += stuCount[i]
            temp = Students[l:r]
            SeriesStudents.append(temp)
            l = r
        print(SeriesStudents)
        return SeriesStudents

def randomNineSeriesStudent(first):
    Students = []
    for i in range(9):
        Students.append(randomSeriesStudent(first + i))
    return Students

def printToExcel(Students , first):
    for i in range(9):
        app = xw.App(visible=True, add_book=False)
        wb = app.books.add()

        for j in range(10):
            wb.sheets.add((first + i).__str__() + '级' + (j + 1).__str__() + '班')
            sheet = wb.sheets[(first + i).__str__() + '级' + (j + 1).__str__() + '班']
            sheet.range('A1').value = '学生编号'
            sheet.range('B1').value = '学生姓名'
            sheet.range('C1').value = '学生性别'
            sheet.range('D1').value = '学生年龄'
            sheet.range('E1').value = '是否是好学生'
            sheet.range('F1').value = '是否数学弱'
            sheet.range('G1').value = '是否语文弱'


            for x in range(2, len(Students[i][j]) + 2):
                sheet.range('A' + x.__str__()).value = Students[i][j][x - 2].id
                sheet.range('B' + x.__str__()).value = Students[i][j][x - 2].name
                sheet.range('C' + x.__str__()).value = Students[i][j][x - 2].sex
                sheet.range('D' + x.__str__()).value = Students[i][j][x - 2].age
                sheet.range('E' + x.__str__()).value = '是' if Students[i][j][x - 2].isGoodStudent else '否'
                sheet.range('F' + x.__str__()).value = '是' if Students[i][j][x - 2].isWeekMath else '否'
                sheet.range('G' + x.__str__()).value = '是' if Students[i][j][x - 2].isWeekChinese else '否'

            sheet.range("A:G").autofit()

        sheet = wb.sheets['Sheet1']
        sheet.delete()

        a = os.path.exists("StudentData")
        if not a:
            b = os.getcwd()
            os.mkdir(b + '\\StudentData')

        wbName = 'StudentData/' + (first + i).__str__() + '级学生数据.xlsx'
        wb.save(wbName)
        wb.close()
        app.quit()

if __name__ == "__main__":
    student = randomSingalStudent(2018)
    Students = randomNineSeriesStudent(2012)
    printToExcel(Students , 2012)

