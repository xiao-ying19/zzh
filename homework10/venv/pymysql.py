"""
设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
"""
import pymysql


def add(note1, name1):
    db = pymysql.connect("localhost", "root", "2349zzh", "test")
    cursor = db.cursor()
    # sql="""insert into notebook (ID,NOTE,NAME,TIME,IS_DELETE) VALUES (%s,%s,%s,%s,%s) """
    # sql = sql % (0, Note, Name, CURRENT_TIME, 1)
    sql = """insert into notebook (ID,NOTE,NAME,TIME,IS_DELETE) VALUES (0,'"""+note1+"""','"""+name1+"""',"""+"""CURRENT_TIME ,1)"""
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def update(id1, note1):
    db = pymysql.connect("localhost", "root", "2349zzh", "test")
    cursor = db.cursor()
    sql = """update notebook set NOTE='"""+note1+"""'where ID="""+str(id1)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("修改成功！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def delete(id1):
    db = pymysql.connect("localhost", "root", "2349zzh", "test")
    cursor = db.cursor()
    sql = """update notebook set IS_DELETE =0 where ID ="""+id1
    try:
        cursor.execute(sql)
        db.commit()
        print("删除成功！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def search(id1):
    db = pymysql.connect("localhost", "root", "2349zzh", "test")
    cursor = db.cursor()
    sql = """select* from notebook where ID ="""+id1+""";"""
    try:
        cursor.execute(sql)
        rs = cursor.fetchall()
        for i in rs:
            print(i)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    print('1.增加信息\n2.修改信息\n3.删除信息\n4.查询信息\n0.退出')
    while True:
        n = input('请输入：')
        if n == '1':
            name = input("请输入留言人姓名：")
            note = input("请输入留言信息：")
            add(note, name)
        elif n == '2':
            a = int(input("请输入要修改的ID值："))
            b = input("请输入修改后的留言内容：")
            update(a, b)
        elif n == '3':
            id0 = input("请输入要删除的ID：")
            delete(id0)
        elif n == '4':
            id0 = input("请输入要查找的id值：")
            search(id0)
        else:
            break
