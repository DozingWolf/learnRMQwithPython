import pika
import sys

print('========消费者========')
print('========路由方式========')
#配置
crea = pika.PlainCredentials(username='admin',password='admin@123')
para = pika.ConnectionParameters(host='10.62.24.70',credentials=crea)
conn = pika.BlockingConnection(parameters=para)
#连接
channel = conn.channel()
#申明交换机类型为直连
exc_name = 'TEST_EXCHANGE_ROUTER'
channel.exchange_declare(exchange='TEST_EXCHANGE_ROUTER',exchange_type='direct')
#申明队列，为临时队列
que = channel.queue_declare(exclusive=True)
#取回队列名用于后续
que_name = que.method.queue
#创建绑定
rt_key_1 = 'rk1'
rt_key_2 = 'rk2'
#消费者1只接收rt_key_1的消息
channel.queue_bind(queue=que_name, exchange=exc_name,routing_key=rt_key_2)
def cb(ch, method, properties, body):
    print (' [x] %r:%r' % (method.routing_key, body,))
#接受
channel.basic_consume(cb, queue=que_name,no_ack=False)
#
channel.start_consuming()
