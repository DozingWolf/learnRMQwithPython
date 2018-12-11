import pika
import sys

print('========生产者========')
#配置
#注意，不加用户会403错误
#注意，需要添加MQ权限，不加会503错误
crea = pika.PlainCredentials(username='admin',password='admin@123')
#加heartbeat参数控制broken pipe error
#好像没什么用处？需要再调查
para = pika.ConnectionParameters(host='10.62.24.70',credentials=crea,heartbeat_interval=60)
#连接
conn = pika.BlockingConnection(parameters=para)
#创建频道
channel = conn.channel()
#创建队列
#申明durable表示要求持久化
channel.queue_declare(queue='hello_q_durable_e2',durable=True)
#持久化需要使用delivery_mode=2
para_dur = pika.BasicProperties(delivery_mode=2)
#申明交换机
exchange_name = 'TEST_EXCHANGE'
exchange_type = 'fanout'
exchange_durable = True
channel.exchange_declare(exchange=exchange_name,exchange_type=exchange_type)
#输入想要传输的内容
a = 1
msg = 'k'
for a in range(100):
    msg = msg+'k'
    channel.basic_publish(exchange=exchange_name,routing_key='hello_q_durable',body=msg,properties=para_dur)
    print(a)

#输出状态
print('========队列开始========')
conn.close()
