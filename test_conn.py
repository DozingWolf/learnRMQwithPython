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
channel.queue_declare(queue='hello_q')
#输入想要传输的内容
a = 1
while a == 1:
    print('please input u r word:')
    msg = input()
    #写队列
    if msg == 'exit':
        a = 0
    else:
        channel.basic_publish(exchange='',routing_key='hello_q',body=msg)

#输出状态
print('========队列开始========')
conn.close()
