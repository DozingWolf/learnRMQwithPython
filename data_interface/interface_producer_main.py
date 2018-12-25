__author__ = 'DozingWolf'
from basic_producer_mq_option import *
from basic_producer_database_option import *
from basic_tool import *
import json
import io
import sys
#用于解决print乱码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# MQ parameter
mq_ip = '10.62.24.70'
mq_user = 'admin'
mq_password = 'admin@123'
mq_exchange = 'TEST_EXCHANGE'
mq_routing_ket = 'interface_001'
# DB parameter
db_ip = '10.62.24.24'
db_port = 1521
db_sid = 'orcl12c'
db_user = 'MQ_OUT'
db_password = 'MQ_OUT'
# 创建mq链接
rtflag,connect,parameter = createMQengine(mq_ip, mq_user, mq_password)
channel = connect.channel()
# 创建DB链接
engine = createEngine(db_user, db_password, db_ip, db_port, db_sid)
CreateorReplaceTable(engine)
session = sessionmaker(bind=engine)
sess = session()
# 取DB中数据
msgbody =[]
for row in sess.query(T_OUT_TP_D).filter_by(sendfg = '00'):
    print(row)
    print(type(row))
    print(row.id)
    print(type(row.id))
    # print(json.dumps(row,default=obj2dict))
    print('__dict__=',row.__dict__)
    print('class2dict=',class_to_dict(row))
    print('row.to_json method =',row.to_json)
    msgbody.append(row.to_json())
    # jsonbody = json.dumps(msgbody)
    msgbody = json.dumps(msgbody)
    print(msgbody)
    # print(json.dumps(row,default=lambda row: row.__dict__))
    # channel.basic_publish(exchange=mq_exchange,routing_key=mq_routing_ket,body=msgbody,properties=parameter)
    print('success!')
# msg='M'
# for a in range(100):
#     msg = msg+'k'
#     channel.basic_publish(exchange=mq_exchange,routing_key=mq_routing_ket,body=msg,properties=parameter)
#     print(a)
connect.close()
