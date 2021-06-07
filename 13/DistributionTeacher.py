# coding=utf-8
import os
from TercherData import *
from queue import Queue

courses = ['语文','数学','英语','物理','化学','地理','历史','政治','体育','音乐','画画']

class Class:
    def __init__(self, year, id, grade):
        self.year = year
        self.id = id
        self.grade = grade
        self.tids = [0 for i in range(len(courses))]

def readTeacherExcel():
    a = os.path.exists('Terchers.xlsx')
    if not a:
        printToExcel(randomTercherList())

    app = xw.App(visible=True, add_book=False)
    wb = app.books.open('Terchers.xlsx')
    sheet = wb.sheets['sheet1']

    Teachers = []
    for i in range(2 , teacherCount + 2):
        tempTeacher = Teacher(int(sheet.range('A' + i.__str__()).value) ,
                              sheet.range('B' + i.__str__()).value ,
                              sheet.range('C' + i.__str__()).value )
        Teachers.append(tempTeacher)

    wb.close()
    app.quit()
    return Teachers

def classificationTeacher(Teachers):
    typeTeacher = []
    for i in range(len(courses)):
        temp = []
        for j in range(len(Teachers)):
            if courses.index(Teachers[j].course) == i:
                temp.append(Teachers[j])
        typeTeacher.append(temp)
    return typeTeacher

def findTeacherNameById(id):
    for t in Teachers:
        if t.id == id:
            return t.name

def distribtion():

    ids = []
    q = Queue(maxsize=30)

    for i in range(10):
        q.put(Class(2012 , i , 1))

    l = 1
    classes = []
    tempClasses = []
    while not q.empty():
        front = q.get()
        for i in range(len(courses)):
            if front.tids[i] != 0:
                continue
            if courses[i] == '物理' and front.grade < 2:
                continue
            if courses[i] == '化学' and front.grade < 3:
                continue

            while True:
                t = int(rm.choice(typeTeacher[i]).id)
                if ids.count(t) >= 2:
                    continue
                ids.append(t)
                front.tids[i] = t
                break

        if front.grade < 3:
            front.grade += 1
            q.put(front)
        else:
            tempClasses.append(front)
            classes.append(front)

            if front.id == 9 and l < 9:
                for t in tempClasses:
                    for i in range(len(courses)):
                        ids.remove(t.tids[i])
                tempClasses.clear()

                for i in range(10):
                    q.put(Class(2012 + l, i, 1))
                l += 1

    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()

    l = 0
    for i in range(9):
        wb.sheets.add((2012 + i).__str__() + '级')
        sheet = wb.sheets[(2012 + i).__str__() + '级']

        sheet.range('A1').value = '班级'
        for i in range(len(courses)):
            sheet.range(chr(66 + i) + '1').value = courses[i] + '老师'

        for i in range(10):
            t = classes[l]
            l += 1
            sheet.range('A' + (i + 2).__str__()).value = (t.id + 1).__str__() + '班'
            for j in range(len(courses)):
                sheet.range(chr(66 + j) + (i + 2).__str__()).value = t.tids[j].__str__() + " " + findTeacherNameById(t.tids[j])
        sheet.range("A:M").autofit()

    sheet = wb.sheets['Sheet1']
    sheet.delete()
    wb.save(r'TerchersDistribution.xlsx')
    wb.close()
    app.quit()

if __name__ == '__main__':
    Teachers = readTeacherExcel()
    typeTeacher = classificationTeacher(Teachers)
    distribtion()