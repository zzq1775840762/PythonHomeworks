# coding=utf-8
class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

if __name__ == '__main__':
    e1= Employee('test' , 3200)
    e1 = Employee('test', 3200)
    e1.displayCount()
    e1.displayEmployee()