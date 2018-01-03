#!/usr/bin/env python
# -*- coding: cp936 -*-
import pymongo

from countOrderDatebaser import countOrderDatebase
import time
import re
import datetime
from pymongo import MongoClient
import pymongo
from selenium import webdriver
class gaiKuang():
    def __init__(self):
        self.count=countOrderDatebase()
    def homePage(self,startDateTime,EndDateTime):
        status1 = {u'��֧��':0,  u'��֧��':1,  u'���˿�':11,  u'���˿�':3, u'��ȡ��':2,  u'������':4,  u'������':5,  u'�ѹ���':6}
        status = {'daizhifu': 0, 'yizhifu': 1, 'daituikuan': 11, 'yituikuan': 3, 'yiquxiao': 2, 'daipingjia': 4, 'yipingjia': 5, 'yiguoqi': 6}
        """actualPayment,orderAmount,orderSourceInternet,orderSourcePhone,orderSourceAndroid,orderSourceIOS,actualImCome,"""
        dictOrder={}
        for status1 in status:
            result=self.count.countOrder(status[status1],startDateTime,EndDateTime)
            dict={}
            dictOrder[status1]=result

        print dictOrder
        #����ɶ���=������+������+�ѹ���+��ȡ��+���˿�
        orderCompleted=dictOrder["daipingjia"][1]+dictOrder["yipingjia"][1]+\
                       dictOrder["yiguoqi"][1]+dictOrder["yiquxiao"][1]+dictOrder["yituikuan"][1]#����ɶ���
        orderCompletedPhone=dictOrder["daipingjia"][3]+dictOrder["yipingjia"][3]+\
                       dictOrder["yiguoqi"][3]+dictOrder["yiquxiao"][3]+dictOrder["yituikuan"][3]

        if orderCompleted==0:
            orderCompletedPhoneRate ="0.00"+'%'
        else:
            orderCompletedPhoneRate="%.2f%%" %(float(orderCompletedPhone)/float(orderCompleted)*100)#('%.2f%%' % ((float('%.2f' %(orderCompletedPhone/orderCompleted))) * 100))
        print u"����ɶ���:"+str(orderCompleted)

        print u"����ɵ��ٱȣ�"+str(orderCompletedPhoneRate)
        #δ��ɶ���=��֧��+��֧��+���˿�
        orderUnCompleted=dictOrder["yizhifu"][1]+dictOrder["daizhifu"][1]+dictOrder["daituikuan"][1]
        orderUnCompletedPhone = dictOrder["yizhifu"][3] + dictOrder["daizhifu"][3] + dictOrder["daituikuan"][3]#δ��ɵ���

        if orderUnCompleted==0:
            orderUnCompletedPhoneRate="0.00"+'%'#('%.2f%%' % ((float('%.2f' %(0))) * 100))
        else:
            orderUnCompletedPhoneRate="%.2f%%" %(float(orderUnCompletedPhone)/float(orderUnCompleted)*100)

            #orderUnCompletedPhoneRate=('%.2f%%' % ((float('%.2f' %(orderUnCompletedPhone/orderUnCompleted))) * 100))
            #print float('%.2f' %(orderUnCompletedPhone/orderUnCompleted))

        print u"δ��ɶ�����"+str(orderUnCompleted)
        print u"δ��ɵ��ٶ����ȣ�"+str(orderUnCompletedPhoneRate)

        #��������=������+������+�ѹ���+���˿�+��֧��
        payAmountPerson=dictOrder["daipingjia"][1]+dictOrder["yipingjia"][1]+\
                        dictOrder["yiguoqi"][1]+dictOrder["yizhifu"][1]+dictOrder["yituikuan"][1]#��������
        payAmountPersonPhone = dictOrder["daipingjia"][3] + dictOrder["yipingjia"][3] + \
                          dictOrder["yiguoqi"][3] + dictOrder["yizhifu"][3] + dictOrder["yituikuan"][3]#���ٸ�������
        if payAmountPerson==0:
            payAmountPersonPhoneRate="0.00"+'%'
        else:
            payAmountPersonPhoneRate="%.2f%%" %(float(payAmountPersonPhone)/float(payAmountPerson)*100)#('%.2f%%' % ((float('%.2f' %(payAmountPersonPhone/payAmountPerson))) * 100))
        print u"����������"+str(payAmountPerson)
        print u"�����������ٱȣ�"+str(payAmountPersonPhoneRate)
        #���ն�������=������+������+�ѹ���+���˿�+��֧��actualPayment+prePayAmount-refundAmount
        orderInCome=round((dictOrder["daipingjia"][6]+dictOrder["yipingjia"][6]+dictOrder["yiguoqi"][6]+dictOrder["yituikuan"][6]+dictOrder["yizhifu"][6]),2)
       # orderInCome=dictOrder["daipingjia"][6]+dictOrder["yipingjia"][6]+dictOrder["yiguoqi"][6]+dictOrder["yituikuan"][6]+dictOrder["yizhifu"][6]
        print u"���ն������룺"+str(orderInCome)
        orderInComePhone=dictOrder["daipingjia"][7]+dictOrder["yiguoqi"][7]
        if orderInCome==0:
            orderInComePhoneRate="0.00"+'%'#('%.2f%%' % ((float('%.2f' %(0))) * 100))
        else:
            orderInComePhoneRate="%.2f%%" %(float(orderInComePhone)/float(orderInCome)*100)
        print u"���յ��ٶ�������ȣ�"+str(orderInComePhoneRate)
        return (orderCompleted,orderUnCompleted,payAmountPerson,orderInCome,
                orderCompletedPhoneRate,orderUnCompletedPhoneRate,payAmountPersonPhoneRate,orderInComePhoneRate)

startDateTime=datetime.datetime(2017, 12, 26, 16, 0, 0, 201000)#2017/12/22/00/00/00
EndDateTime=datetime.datetime(2017, 12, 27, 15, 59, 59, 201000)#2017/12/22/23/59/59

f=gaiKuang().homePage(startDateTime,EndDateTime)
