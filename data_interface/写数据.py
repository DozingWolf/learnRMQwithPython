import io
import sys
#用于解决print乱码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#default connect data
db_ip = '10.62.24.24'
db_port = 1521
db_sid = 'orcl12c'
db_user = 'wande_data'
db_password = 'wande_data'

engine = createEngine(db_user, db_password, db_ip, db_port, db_sid)
CreateorReplaceTable(engine)
session = sessionmaker(bind=engine)
sess = session()

getConnecttoWind()
stock_list = getStocks()
print(stock_list)
print('==========================')
print(stock_list.Data[0][0])
#len(stock_list.Codes)
#先完成股票基础数据的IO
for num in range(len(stock_list.Codes)):
    print('id:',num,'/stock_code is:',stock_list.Data[1][num],'/stock_name is:',stock_list.Data[2][num])
    sess.add_all([TMST_STOCK(id=num,stockcode=stock_list.Data[1][num],stockname=stock_list.Data[2][num],getdate=datetime.now(),getseq=1)])
sess.commit()
#再进行股票明细的获取
for num in range(len(stock_list.Codes)):
    print(num)
    if num == 0:
        stock_detail_CSRC = getStockDetailCSRC(stock_list.Data[1][num]).Data
        stock_detail_WIND = getStockDetailWIND(stock_list.Data[1][num]).Data
    else:
        stock_detail_CSRC = stock_detail_CSRC + getStockDetailCSRC(stock_list.Data[1][num]).Data
        stock_detail_WIND = stock_detail_WIND + getStockDetailWIND(stock_list.Data[1][num]).Data
#写入股票明细CSRC
for num in range(len(stock_detail_CSRC.Codes)):
    pass#print('id=',)

# sess.commit()
closeConnect()
print(stock_detail_CSRC)
print(stock_detail_WIND)
