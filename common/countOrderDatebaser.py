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
        db = client.ora_db  # ����ora_db���ݿ⣬û�����Զ�����
        self.my_set = db.ora_order  # ʹ��ora_car���ϣ�û�����Զ�����
        status = {0: u'��֧��', 1: u'��֧��', 11: u'���˿�', 3: u'���˿�', 2: u'��ȡ��', 4: u'������', 5: u'������', 6: u'�ѹ���'}

    def countOrder(self,status,startDateTime,EndDateTime):#���մ�����
        nowTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        noEvaluateOrder = self.my_set.find({"documentState": 1, "storeId": "586a1a0267907f3c72bf6c27","status":status,
                            'createdTime': {"$gte":startDateTime,#2017/12/22/00/00/00
                                            "$lte":EndDateTime}})#2017/12/22/23/59/59
        dictOder={}
        actualPayment =0#ʵ��֧��
        orderAmount=0#��������
        actualImCome=0#ʵ������
        actualImComePhone=0
        orderSourceInternet=0#���綩��0
        orderSourcePhone=0#���ٶ���1
        orderSourceAndroid=0#��׿����2
        orderSourceIOS=0#ios����3

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
                print u"������Դ��������~~~~~"


        #print u"ʵ��֧��:"+str(actualPayment )
        #print u'��������:'+str(orderAmount)
        #print u"���綩��:"+str(orderSourceInternet)
        #print u"���ٶ���:"+str(orderSourcePhone)
        #print u"��׿����:"+str(orderSourceAndroid)
       # print u"IOS����:"+str(orderSourceIOS)
        #print actualImCome,actualPayment
        #print actualImComePhone
        return actualPayment,orderAmount,orderSourceInternet,orderSourcePhone,orderSourceAndroid,orderSourceIOS,actualImCome,actualImComePhone

#startDateTime=datetime.datetime(2017, 12, 14, 16, 0, 0, 201000)#2017/12/22/00/00/00
#EndDateTime=datetime.datetime(2017, 12, 25, 15, 59, 59, 201000)#2017/12/22/23/59/59

#f=countOrderDatebase().countOrder(4,startDateTime,EndDateTime)
