import random as rm
import matplotlib.pyplot as plt
import numpy as np

'''
学生类 学号，性别，得分
'''
class Student:
    def __init__(self , id , sex , score):
        '''
        构造函数
        :param id: 学号
        :param sex: 性别
        :param score: 得分
        '''
        self.id = id
        self.sex = sex
        self.score = score

    def __repr__(self):
        return "{0} , {1} , {2}".format(self.id , self.sex ,  self.score) + "\n"

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

def randomStudentCount():
    '''
    返回符合总人数的学生各人数数组
    :return: 各分数段人数数组
    '''
    minStu = [3 , 6 , 25 , 6]
    maxStu = [8 , 10 , 35 , 12]
    while True:
        sum = 0
        num = []
        for i in range(4):
            rmint = rm.randint(minStu[i] , maxStu[i])
            num.append(rmint)
            sum += rmint

            if sum > 60 - 2:
                break
        if sum == 60 - 2:
            return num

def radomScore():
    '''
    返回符合得分区间个数的50个分数并随机打乱
    :return: 得分数组
    '''
    score = [i * 10 for i in range(6, 10)]
    count = randomStudentCount()

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

def randamSex():
    '''
    返回一个随机的性别数组
    :return: 性别数组
    '''
    sex1 = [True for i in range(52)]
    sex2 = [False for i in range(8)]
    sex = sex1 + sex2
    #print(sex)
    rm.shuffle(sex)
    return sex

def randomStudents():
    '''
    返回一个随机的学生数组
    :return: 学生数组
    '''
    id = randomId()
    sex = randamSex()
    score = radomScore()
    students = []
    for i in range(60):
        students.append(Student(id[i] , sex[i] , score[i]))
    #rm.shuffle(students)
    #print(students)
    return students

def printScoreTable(students):
    '''
    格式输出各学生的学号，性别和分数
    :param students: 学生数组
    :return:
    '''
    for i in range(len(students)):
        print("Student_id:{0} \tStudent_sex:{1}  \tStudent_score:{2}".
              format(students[i].id , "boy" if students[i].sex == True else "girl" , students[i].score))

def printLineChart(students):
    '''
    输出统计各分数段的最高分的折线图
    :param students: 学生数组
    :return:
    '''
    label = ['[0,60)', '[60,70)', '[70,80)', '[80,90)', '[90,100]']
    mscore = [0 for i in range(5)]
    for i in range(len(students)):
        score = students[i].score
        if score < 60:
            mscore[0] = max(mscore[0] , score)
        elif score >= 60 and score < 70:
            mscore[1] = max(mscore[0] , score)
        elif score >= 70 and score < 80:
            mscore[2] = max(mscore[0] , score)
        elif score >= 80 and score < 90:
            mscore[3] = max(mscore[0] , score)
        else:
            mscore[4] = max(mscore[0] , score)

    fig, ax = plt.subplots()
    ax.plot(label, mscore)

    ax.set(xlabel='Different categories', ylabel='Max of score',
           title='Max of score in different categories')
    ax.grid()

    plt.show()

def printBarChart(students):
    '''
    输出统计各分数段人数的柱状图
    :param students: 学生数组
    :return:
    '''
    plt.rcdefaults()
    fig, ax = plt.subplots()

    label = ['[0,60)', '[60,70)', '[70,80)', '[80,90)', '[90,100]']
    y_pos = np.arange(len(label))
    sum = [0 for i in range(5)]
    for i in range(len(students)):
        score = students[i].score
        if  score < 60:
            sum[0] += 1
        elif score >= 60 and score < 70:
            sum[1] += 1
        elif score >= 70 and score < 80:
            sum[2] += 1
        elif score >= 80 and score < 90:
            sum[3] += 1
        else:
            sum[4] += 1

    ax.barh(y_pos, sum, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(label)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Count of students')
    ax.set_title('Count students of score in different categories')

    plt.show()

def calculateAverageScore(students):
    '''
    计算平均得分
    :param students: 学生数组
    :return: 学生的成绩平均分
    '''
    sum = 0
    for i in range(len(students)):
        sum += students[i].score
    print("Average score is {0}".format(float(sum) / len(students)))

def calculateMaxScore(students):
    '''
    计算最高得分
    :param students: 学生数组
    :return: 学生中的最高得分
    '''
    mscore = 0
    for i in range(len(students)):
        mscore = max(mscore , students[i].score)
    print("Max score is {0}".format(mscore))

if __name__ == "__main__":
    students = randomStudents()
    printScoreTable(students)
    printLineChart(students)
    printBarChart(students)
    calculateAverageScore(students)
    calculateMaxScore(students)
