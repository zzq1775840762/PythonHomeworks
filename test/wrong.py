import random as rm
import matplotlib.pyplot as plt
import numpy as np
class Student:
    def __init__ (self , id , sex , score):
        self.id = id
        self.sex = sex
        self.score = score

    def __repr__(self):
        return "{0} , {1} , {2}".format(self.id , self.sex ,  self.score) + "\n"

def random_id():
    num = []
    while True:
        num.append(202100 + rm.randint(0, 1819001))
        setList = list(set(num))

        if len(setList) == 70:
            setList.sort()
            return setList
def random_score(): #返回分数并打乱
    score = [i * 10 for i in range(6, 10)]
    count = random_count()
    s = [0, 0]
    for i in range(len(count)):
        for j in range(count[i]):
            rmint = rm.randint(0, 10)
            if rmint != 10:
                rmint +=0.5
            s.append(score[i] + rmint)
    rm.shuffle(s)
    return s

def random_count():#返回分数段人数
    min_num = [5,7,27,8]
    max_num = [13,15,38,17]
    while True:
        sum = 0
        num = []
        for i in range(0,4):
            number = rm.randint(min_num[i] , max_num[i])
            num.append(number)
            sum = sum + number

            if sum > 70 - 2:
                break
        if sum == 70 - 2:
            return num

def random_sex():#随机设定性别
    male = [True for i in range(52)]
    female = [False for i in range(18)]
    sex = female+male
    #print(sex)
    rm.shuffle(sex)
    return sex

def random_students():
    students = []
    id = random_id()
    sex = random_sex()
    score = random_score()
    for i in range(70):
        students.append(Student(id[i],sex[i],score[i]))
    return students
def printScoreTable(students):
    for i in range(len(students)):
        print("Student_id:{0} \tStudent_sex:{1}  \tStudent_score:{2}".
              format(students[i].id, "boy" if students[i].sex == True else "girl", students[i].score))

def printLineChart(teams):
    label = ['[0,60)', '[60,70)', '[70,80)', '[80,90)', '[90,100]']
    mscore = [0 for i in range(5)]
    for i in range(len(teams)):
        score = teams[i].score
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
def print_BarChart(students):
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
def calculateAverage(students):
    sum = 0
    for i in range(len(students)):
        sum += students[i].score
    print("Average score is {0}".format(float(sum) / len(students)))
def calculateMaxScore(students):
    mscore = 0
    for i in range(len(students)):
        mscore = max(mscore , students[i].score)
    print("Max score is {0}".format(mscore))
if __name__ == "__main__":
    students=random_students()
    printScoreTable(students)
    printLineChart(students)
    print_BarChart(students)
    calculateAverage(students)
    calculateMaxScore(students)