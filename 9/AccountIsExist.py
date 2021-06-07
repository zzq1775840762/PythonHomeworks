# coding=utf-8
def deco(judge):
    def warpper(account , password):
        judge(account , password)
        if account == "ch" and password == "123456":
            print(account + "欢迎登陆")
        else:
            print("account is not exist")
    return warpper

@deco
def judge(account , password):
    print("这是测试函数")
    return ;

account = input("请输入你的名字>>: ")
password = input("请输入你的密码>>: ")
judge(account , password)