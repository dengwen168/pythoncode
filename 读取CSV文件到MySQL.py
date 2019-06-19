# -*- coding: utf-8 -*-
#https://blog.csdn.net/buffoon1900/article/details/85322318



import importlib,sys
importlib.reload(sys)
import pandas as pd
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
 
DB_CONNECT_STRING = 'mysql+pymysql://root:1900@localhost/mysql?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
 
csv_data = pd.read_csv('abc.csv',encoding='utf-8')
print(csv_data.shape)
pd.io.sql.to_sql(frame=csv_data,name='00test1228',con=engine,index=False,if_exists='append')
