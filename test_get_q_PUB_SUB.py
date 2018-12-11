import pika
import sys
import time
print('========消费者========')
#配置
crea = pika.PlainCredentials(username='admin',password='admin@123')
para = pika.ConnectionParameters(host='10.62.24.70',credentials=crea)
conn = pika.BlockingConnection(parameters=para)
#连接
channel = conn.channel()
#创建随机队列
channel.queue_declare(queue='hello_q_durable',durable=True)
#申明绑定
channel.queue_bind(exchange='TEST_EXCHANGE',queue=inst.method.queue)
def cb(ch,method,properties,body):
    print('[x] Receiced %r' % body)
    #使用delivery标记表示信息投递反馈
    #注意！反馈ACK必须在系统工作事务完成之后再进行，可以实现公平调度，否则会认为已经成功完成业务内容而不再公平调度
    #time.sleep(body.count(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

#获取
#申明本消费者要求公平调度，在本消费者持有未发送ACK的数据情况下不再发送新消息到该消费者
channel.basic_qos(prefetch_count=1)
#在有delivery标记之后必须使用no_ack=false标记，否侧将报错
channel.basic_consume(cb,queue='hello_q_durable',no_ack=False)
print('please wait for message , to exit press ctrl+c')
channel.start_consuming()
