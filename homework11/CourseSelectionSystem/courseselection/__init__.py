"""
初始化，创建数据库连接
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:2349zzh@localhost:3306/courseselectionsystem')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session
session = DBSession()
