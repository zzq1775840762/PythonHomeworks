# coding=utf-8
import pymysql
def connect_mysql():
    #  uer 用户名  passwd 密码  db 数据库名
    c = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456'
                        ,db='pypsychology',charset='utf8')

    return c


def insert(sql):
    c = connect_mysql() # 首先连接数据库
    cus = c.cursor() # 生成游标对象

    try:
        cus.execute(sql) # 执行SQL语句
        c.commit() # 如果执行成功就提交事务
    except Exception as e:
        c.rollback() # 如果执行失败就回滚事务
        raise e
    finally:
        c.close() # 最后记得关闭数据库连接


def insertList(sqls):
    c = connect_mysql()  # 首先连接数据库
    cus = c.cursor()  # 生成游标对象

    try:
        for sql in sqls:
            # print('sql')
            cus.execute(sql)  # 执行SQL语句
        c.commit()  # 如果执行成功就提交事务
    except Exception as e:
        c.rollback()  # 如果执行失败就回滚事务
        raise e
    finally:
        c.close()  # 最后记得关闭数据库连接


def select(sql):
    c = connect_mysql()  # 首先连接数据库
    cus = c.cursor()  # 生成游标对象

    try:
        cus.execute(sql) # 执行SQL语句
        c.commit() # 如果执行成功就提交事务
        return cus.fetchall()
    except Exception as e:
        c.rollback() # 如果执行失败就回滚事务
        raise e
    finally:
        c.close() # 最后记得关闭数据库连接

def update(sql):
    c = connect_mysql() # 首先连接数据库
    cus = c.cursor() # 生成游标对象

    try:
        cus.execute(sql) # 执行SQL语句
        c.commit() # 如果执行成功就提交事务
    except Exception as e:
        c.rollback() # 如果执行失败就回滚事务
        raise e
    finally:
        c.close() # 最后记得关闭数据库连接

def delete(sql):
    c = connect_mysql() # 首先连接数据库
    cus = c.cursor() # 生成游标对象

    try:
        cus.execute(sql) # 执行SQL语句
        c.commit() # 如果执行成功就提交事务
    except Exception as e:
        c.rollback() # 如果执行失败就回滚事务
        raise e
    finally:
        c.close() # 最后记得关闭数据库连接

# if __name__ == '__main__':
#     results = select('select * from t_student')
