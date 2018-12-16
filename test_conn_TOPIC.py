import pika
import sys

print('============topic交换机_生产者===========')
#建立链接参数
#1.建立认证
#1.1.组装登陆参数
login_name = 'admin'
login_pw = 'admin@123'
cera = pika.PlainCredentials(username = login_name, password = login_pw)
host_ip = '10.62.24.70'
hb_int = 60
para = pika.ConnectionParameters(host=host_ip,credentials=cera,heartbeat=hb_int)
#2.创建链接
conn = pika.BlockingConnection(parameters=para)
#3.创建channel
channel = conn.channel()
#4.创建topic交换机
exc_mode = 'topic'
exc_name = ''
