"""

"""
from sqlalchemy import Column, String, Integer,and_
from sqlalchemy.ext.declarative import declarative_base
from courseselection import session,engine


Base = declarative_base()


#  学生表，学生信息一旦注册，不可修改
class Students(Base):
    __tablename__ = "students"
    id = Column(String(32), primary_key=True)   # 学号
    name = Column(String(32))  # 姓名
    department = Column(String(32))  # 院系
    #cla = Column(String(32))  # 班级
    password = Column(String(255))

    @classmethod
    def create(cls):
        try:
            Base.metadata.create_all(engine)
        except Exception as err:
            print(err)

    @classmethod
    def add(cls, **kwargs):
        try:
            infomation = Students(
                id=kwargs.get('id'),
                name=kwargs.get('name'),
                department=kwargs.get('department'),
               # cla=kwargs.get('cla'),
                password=kwargs.get('password')

            )
            session.add(infomation)
            session.commit()
        except Exception as err:
            session.rollback()
            print(err)
        finally:
            session.close()

    @classmethod
    def search(cls, idnum):
        try:
            flag = 0
            result = session.query(Students).filter_by(id=idnum).all()
            print(len(result))
            print(type(result))
            if len(result) != 0:
                flag = 1
            return flag,result
        except Exception as err:
            print(err)
        finally:
            session.close()


class SelectedClass(Base):
    __tablename__ = "selectedclass"
    num = Column(Integer,primary_key=True)
    id = Column(String(32))
    classID = Column(String(32))


    @classmethod
    def create(cls):  # 有重复代码怎么优化？？？？？？？？？？？？？？？？？？？？？？每个类的创建函数都一样
        try:
            Base.metadata.create_all(engine)
        except Exception as err:
            print(err)

    @classmethod
    def add(cls, **kwargs):
        try:
            information = SelectedClass(
                num=0,
                id=kwargs.get('id'),
                classID=kwargs.get('classID')
            )
            session.add(information)
            session.commit()
        except Exception as err:
            print(err)
        finally:
            session.close()

    @classmethod
    def delete(cls, **kwargs):
        try:
            session.query(SelectedClass).filter(and_(SelectedClass.id == kwargs.get('id'),SelectedClass.classID == kwargs.get('classID'))).delete()
            session.commit()
        except Exception as err:
            print(err)
        finally:
            session.close()

    @classmethod
    def search(cls, num):  # 查询当前学号的所有课程
        try:
            result = session.query(SelectedClass).filter_by(id=num).all()
            return result
        except Exception as err:
            print(err)
        finally:
            session.close()




class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(String(32))
    name = Column(String(32))
    classID = Column(String(32), primary_key=True)
    classname = Column(String(32))
    time = Column(String(255))
    password = Column(String(255))


    @classmethod
    def create(cls):
        try:
            Base.metadata.create_all(engine)
        except Exception as err:
            print(err)

    @classmethod
    def add(cls, **kwargs):
        try:
            infomation = Teacher(
                id=kwargs.get('id'),
                name=kwargs.get('name'),
                classID=kwargs.get('classID'),
                classname=kwargs.get('classname'),
                time=kwargs.get('time'),
                password=kwargs.get('password'),

            )
            session.add(infomation)
            session.commit()
        except Exception as err:
            print(err)
        finally:
            session.close()

    @classmethod
    def search(cls, classID):  # 用于学生导出课程表。根据课程号，查找教师姓名,课程名称，上课时间
        try:
            result = session.query(Teacher).filter(Teacher.classID == classID).first()
            return result
        except Exception as err:
            print(err)
        finally:
            session.close()

    @classmethod
    def findall(cls):
        res = session.query(Teacher)
        return res


class TeacherInfo(Base):
    __tablename__ = 'teacherinfo'
    id = Column(String(32), primary_key=True)
    name = Column(String(32))
    password = Column(String(255))

    @classmethod
    def create(cls):
        try:
            Base.metadata.create_all(engine)
        except Exception as err:
            print(err)

    @classmethod
    def searchID(cls, ID):
        try:
            flag = 0
            result = session.query(TeacherInfo).filter(TeacherInfo.id == ID).first()
            if result is not None:
                flag = 1
            return flag, result
        except Exception as err:
            print(err)
        finally:
            session.close()
