import pika
import sys

print('========生产者========')
print('========路由方式========')
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
para_dur = pika.BasicProperties(delivery_mode=2)
exc_name = 'TEST_EXCHANGE_ROUTER'
#输入想要传输的内容
a = 1
msg = 'k'
rt_key_1 = 'rk1'
rt_key_2 = 'rk2'
for a in range(100):
    msg = msg+'k'
    if a%2 == 0:
        channel.basic_publish(exchange=exc_name,routing_key=rt_key_1,body=msg,properties=para_dur)
    else:
        channel.basic_publish(exchange=exc_name,routing_key=rt_key_2,body=msg,properties=para_dur)
    print(a)

#输出状态
print('========队列开始========')
conn.close()
