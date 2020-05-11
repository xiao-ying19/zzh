"""
对2中的表结构，用SQLAchemy模块来实现同样的操作；
"""
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('mysql+mysqlconnector://root:2349zzh@localhost:3306/test')
Base = declarative_base()


class NoteBook(Base):
    __tablename__ = "notebook"
    id = Column(Integer, primary_key=True)
    note = Column(String(32))
    name = Column(String(32))
    time = Column(Date)
    is_delete = Column(Integer)


def insert():
    Session = sessionmaker(engine)
    db_session = Session()
    obj = NoteBook(id=0, note='help', name='Jack', time=datetime.now(), is_delete=1 )
    try:
        db_session.add(obj)
        db_session.commit()
    except Exception as e:
        print(e)
    finally:
        db_session.close()


def search():
    Session = sessionmaker(engine)
    db_session = Session()
    try:
        user_list = db_session.query(NoteBook).filter(NoteBook.id >= 10).all()
    except Exception as e:
        print(e)
    finally:
        db_session.close()
        for user in user_list:
            print(user.id, user.name, user.note, user.time)


def update():
    Session = sessionmaker(engine)
    db_session = Session()
    try:
        db_session.query(NoteBook).filter_by(id=10).update({"name": "John"})
        db_session.commit()
    except Exception as e:
        print(e)
    finally:
        db_session.close()


def delete():
    Session = sessionmaker(engine)
    db_session = Session()
    try:
        db_session.query(NoteBook).filter_by(id=10).delete()
        db_session.commit()
    except Exception as e:
        print(e)
    finally:
        db_session.close()

# insert()
# delete()
#search()
update()





