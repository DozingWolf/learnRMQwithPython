__author__ = 'DozingWolf'
import json
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,MetaData
from sqlalchemy.orm import sessionmaker,query
from sqlalchemy.dialects.oracle import DATE,VARCHAR2,NUMBER

# db_ip = '10.62.24.24'
# db_port = 1521
# db_sid = 'orcl12c'
# db_user = 'T_OUT_TP_D'
# db_password = 'T_OUT_TP_D'

def createEngine(user, password, ip, port, sid):
    db_engine = create_engine('oracle://%s:%s@%s:%d/%s'%(user, password, ip, port, sid ), echo=False)
    return db_engine

Base = declarative_base()
#
class T_OUT_TP_D(Base):
    __tablename__ = 'T_OUT_TP_D'
    id = Column(NUMBER,primary_key=True,nullable=False)
    msg01 = Column(VARCHAR2(20))
    msg02 = Column(DATE)
    msg03 = Column(NUMBER)
    sendfg = Column(VARCHAR2(2))
    wbflag = Column(VARCHAR2(2))
    def __repr__(self):
        return '<T_OUT_TP_D(id=%d,msg01=%s,msg02=%s,msg03=%d)>'%(self.id,self.msg01,str(self.msg02),self.msg03)
    def to_json(self):
        return {
                'id':self.id,
                'msg01':self.msg01,
                'msg02':self.msg02,
                'msg03':self.msg03,
                'sendfg':self.sendfg,
                'wbflag':self.wbflag
                }

# engine = createEngine(db_ip,db_password,db_sid,db_user,db_password)

def CreateorReplaceTable(db_engine):
    Base.metadata.create_all(db_engine)

def CreateSession(db_engine):
    session = sessionmaker(bind=db_engine)
    return session()
