__author__ = 'DozingWolf'
import pika
import sys

def createMQengine(ip,user,password,hb=60,port=15672):
    if not all([ip,port,user,password,hb]):
        print('some RMQlink parameter was empty ,please check parameters again! ip=%s,port=%d,user=%s,password=%s,hb=%d'%(ip,port,user,password,hb))
        rtf = -1
        conn = -1
        para_dur = -1
    else:
        rtf = 1
    if rtf == 1:
        crea = pika.PlainCredentials(username=user,password=password)
        para = pika.ConnectionParameters(host=ip,credentials=crea,heartbeat_interval=hb)
        conn = pika.BlockingConnection(parameters=para)
        para_dur = pika.BasicProperties(delivery_mode=2)

    return rtf,conn,para_dur
