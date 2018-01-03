#!/usr/bin/env python
# -*- coding: cp936 -*-
import  time
from pymongo import MongoClient
import pymongo
import datetime

class countOrderDatebase():
    def __init__(self):
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        db = client.ora_db  # 连接ora_db数据库，没有则自动创建
        self.my_set = db.ora_order  # 使用ora_car集合，没有则自动创建
        status = {0: u'待支付', 1: u'已支付', 11: u'待退款', 3: u'已退款', 2: u'已取消', 4: u'待评价', 5: u'已评价', 6: u'已过期'}

    def countOrder(self,status,startDateTime,EndDateTime):#今日待评价
        nowTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        noEvaluateOrder = self.my_set.find({"documentState": 1, "storeId": "586a1a0267907f3c72bf6c27","status":status,
                            'createdTime': {"$gte":startDateTime,#2017/12/22/00/00/00
                                            "$lte":EndDateTime}})#2017/12/22/23/59/59
        dictOder={}
        actualPayment =0#实际支付
        orderAmount=0#订单数量
        actualImCome=0#实际收入
        actualImComePhone=0
        orderSourceInternet=0#网络订单0
        orderSourcePhone=0#电召订单1
        orderSourceAndroid=0#安卓订单2
        orderSourceIOS=0#ios订单3

        for order in noEvaluateOrder:
            #print order
            orderAmount+=1
            actualPayment=float('%.2f'%order["actualPayment"])+actualPayment


            if order.has_key("prePayAmount"):
                actualImCome=float('%.2f'%order["actualPayment"])+float('%.2f'%order["prePayAmount"])-float('%.2f'%order["refundAmount"])+actualImCome
                #print actualImCome,float('%.2f'%order["actualPayment"]),float('%.2f'%order["prePayAmount"]),float('%.2f'%order["refundAmount"])
            else:
                actualImCome = float('%.2f' % order["actualPayment"])  - float(
                    '%.2f' % order["refundAmount"])+actualImCome
                    #print actualImCome,float('%.2f' % order["actualPayment"]),float(
                        #'%.2f' % order["refundAmount"])
            #print  order['orderSource']
            if order['orderSource']==1:
                   actualImComePhone=actualImComePhone+order["actualPayment"]

            if order['orderSource']==0:
                orderSourceInternet= orderSourceInternet+1
            elif order['orderSource']==1:
                orderSourcePhone=orderSourcePhone+1
            elif order['orderSource']==2:
                orderSourceAndroid=orderSourceAndroid+1
            elif order['orderSource']==3:
                orderSourceIOS=orderSourceIOS+1
            else:
                print u"订单来源出问题啦~~~~~"


        #print u"实际支付:"+str(actualPayment )
        #print u'订单数量:'+str(orderAmount)
        #print u"网络订单:"+str(orderSourceInternet)
        #print u"电召订单:"+str(orderSourcePhone)
        #print u"安卓订单:"+str(orderSourceAndroid)
       # print u"IOS订单:"+str(orderSourceIOS)
        #print actualImCome,actualPayment
        #print actualImComePhone
        return actualPayment,orderAmount,orderSourceInternet,orderSourcePhone,orderSourceAndroid,orderSourceIOS,actualImCome,actualImComePhone

#startDateTime=datetime.datetime(2017, 12, 14, 16, 0, 0, 201000)#2017/12/22/00/00/00
#EndDateTime=datetime.datetime(2017, 12, 25, 15, 59, 59, 201000)#2017/12/22/23/59/59

#f=countOrderDatebase().countOrder(4,startDateTime,EndDateTime)
