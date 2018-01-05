#!/usr/bin/env python
# -*- coding: cp936 -*-

import  time
import pymongo
import pymongo
from pymongo import MongoClient
import datetime
from gaiKuang import gaiKuang
class orderSituation():
    def __init__(self):
        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        self.db = client.ora_db  # ����ora_db���ݿ⣬û�����Զ�����
        status1 = {u'��֧��': 0, u'��֧��': 1, u'���˿�': 11, u'���˿�': 3, u'��ȡ��': 2, u'������': 4, u'������': 5, u'�ѹ���': 6}
    def countSevenOrderSituation(self,startDateTime,EndDateTime):
        sevenOrder = 0  # 7�충����
        noEvaluateOrder = 0  # 7������۶���
        evaluateOrder = 0  # 7�������۶���
        passOrder = 0  # 7���ѹ��ڶ���
        order=self.db.ora_order
        orderList = order.find({"documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
                            'createdTime': {"$gte":startDateTime,#2017/12/22/00/00/00
                                            "$lte":EndDateTime}})
        for order1 in orderList:
            sevenOrder=sevenOrder+1
        print "7�충������"+str(sevenOrder)
        

        noEvaluateOrderList = order.find({"status":2,"documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",#�����۶�����
                                'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                                                "$lte": EndDateTime}})
        for order2 in noEvaluateOrderList:
            noEvaluateOrder=noEvaluateOrder+1
        evaluateOrderList = order.find(# �����۶�����
            {"status": 4, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        for order3 in evaluateOrderList:
            evaluateOrder = evaluateOrder + 1

        passOrderList = order.find(  # �ѹ��ڶ�����
            {"status": 5, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        for order4 in passOrderList:
            passOrder = passOrder + 1
        sevenServeOrder=noEvaluateOrder+evaluateOrder+passOrder
        print "7���ѷ��񶩵���"+str(sevenServeOrder)
        noPayOrderList = order.find(  # ��֧��������
            {"status": 0, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        noPayOrder=0
        for order5 in noPayOrderList:
            noPayOrder = noPayOrder + 1
        payOrderList = order.find(  # ��֧��������
            {"status": 1, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        payOrder = 0
        for order6 in payOrderList:
            payOrder = payOrder + 1

        noRefundOrderList = order.find(  # ���˿����
            {"status": 11, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        noRefundOrder = 0
        for order6 in                                                       :
            noRefundOrder = noRefundOrder + 1
        severUnServeOrder=noPayOrder+payOrder+noRefundOrder
        print "7������񶩵���" + str(severUnServeOrder)
        sevenRefundOrder=0#7���˿���
        sevenRefundOrderList = order.find(  # ���˿����
            {"status": 3, "documentState": 1, "storeId": "586a1a0267907f3c72bf6c27",
             'createdTime': {"$gte": startDateTime,  # 2017/12/22/00/00/00
                             "$lte": EndDateTime}})
        for order7 in sevenRefundOrderList:
            sevenRefundOrder = sevenRefundOrder + 1
        print "7���˿�����"+str(sevenRefundOrder)
        sevenIncome=gaiKuang().homePage(startDateTime,EndDateTime)[3]
        print "7�����룺"+str(sevenIncome)

        



startDateTime=datetime.datetime(2017, 12, 19, 16, 0, 0, 201000)#2017/12/22/00/00/00
EndDateTime=datetime.datetime(2017, 12, 26, 15, 59, 59, 201000)#2017/12/22/23/59/59
f=orderSituation().countSevenOrderSituation(startDateTime,EndDateTime)