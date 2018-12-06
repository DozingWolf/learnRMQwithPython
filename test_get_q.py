import pika
import sys

print('========消费者========')
#配置
crea = pika.PlainCredentials(username='admin',password='admin@123')
para = pika.ConnectionParameters(host='10.62.24.70',credentials=crea)
conn = pika.BlockingConnection(parameters=para)
#连接
channel = conn.channel()
#创建队列
channel.queue_declare(queue='hello_q')

def cb(ch,method,properties,body):
    print('[x] Receiced %r' % body)
#获取
channel.basic_consume(cb,queue='hello_q',no_ack=True)
print('please wait for message , to exit press ctrl+c')
channel.start_consuming()
