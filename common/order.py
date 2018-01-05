#!/usr/bin/env python
# -*- coding: cp936 -*-
import json
import requests
from login import login
class countAllOrder():

    def __init__(self):
        #pass
        self.token = login().Login(login_para)
        self.header = {"X-Auth-Token": self.token, "STORE_ID": "586a1a0267907f3c72bf6c27"}

    def orderListConventional(self,dict,login_para):#常规订单
        '''
        url1 = "http://stg-firm.undunion.com/orange-firm/order/find?"
        list=[]
        for i in dict:
            list.append(str(i) + "=" + str(dict[i]))
        print list
        url2 = "&".join(list)
        URL=url1+url2'''
        #self.token = login().Login(login_para)
        #self.header = {"X-Auth-Token": self.token, "STORE_ID": "586a1a0267907f3c72bf6c27"}
        url1="http://stg-firm.undunion.com/orange-firm/order/find?"
        obj = requests.get(url1,params=dict, headers=self.header)
        result=obj.text
        param = json.loads(result)
        order=param['resultData']['content']
        print order
        print len(order)
        return order
    def orderListChOrder(self,dict,login_para):#品牌约车
        #token = login().Login(login_para)
        #header = {"X-Auth-Token": token, "STORE_ID": "586a1a0267907f3c72bf6c27"}
        url="http://stg-firm.undunion.com/orange-firm/chOrder/find"
        obj = requests.post(url, data=dict, headers=self.header)
        result = obj.text
        param = json.loads(result)
        order = param['resultData']['content']
        print order
        print len(order)
        return order
    def orderListTaxiOrder(self,dict,login_para):#出租车
        url = "http://stg-firm.undunion.com/orange-firm/taxiOrder/find?"
        obj = requests.get(url, params=dict, headers=self.header)
        result = obj.text
        #print obj.url
        param = json.loads(result)
        order = param['resultData']['content']
        print order
        print len(order)
        return order

    def orderListCrOrder(self, dict, login_para):#自驾租车
        url = "http://stg-firm.undunion.com/orange-firm/crOrder/find?"
        obj = requests.get(url, params=dict, headers=self.header)
        result = obj.text
        # print obj.url
        param = json.loads(result)
        order = param['resultData']['content']
        print order
        print len(order)
        return order
    def orderListOrder(self, dict, login_para):#积分
        url = "http://stg-firm.undunion.com/orange-firm/order/find?"
        obj = requests.get(url, params=dict, headers=self.header)
        result = obj.text
        # print obj.url
        param = json.loads(result)
        order = param['resultData']['content']
        print order
        print len(order)
        return order
    def orderListGoodsOrder(self, dict, login_para):#连接小店
        url = "http://stg-firm.undunion.com/orange-firm/goodsOrder/find?"
        obj = requests.get(url, params=dict, headers=self.header)
        result = obj.text
        # print obj.url
        param = json.loads(result)
        order = param['resultData']['content']
        print order
        print len(order)
        return order





dictConventional={"aAddress":u"北京","bAddress":u'绵阳','businessModel':"", 'code':'', 'driverName':'', 'endTime':'',
      'groupId':'', 'licensePlat':'', 'licensePlatProvince':'', 'licensePlatType':'',
      'orderSource':'0', 'pageNo':'0', 'pageSize':'20', 'payTimeEnd':'', 'payTimeStart':'',
      'productTypeLevelOne':'CITY_BUS', 'productTypeLevelTwo':'CITY_CAR_POOL_BUS', 'startTime':'',
      'status':'0'}
dictChOrder={'pageNo':'0','pageSize':'10','startTime':'2017-11-22 00:00:00','endTime':'2017-12-21 00:00:00',
       'status':'4','code':'','groupId':''}
dictTaxiOrder={'pageNo':'0','pageSize':'10','startTime':'2017-11-22 00:00:00','endTime':'2017-12-21 00:00:00',
       'status':'4','code':'','groupId':'',"businessModel":"0"}
dictCrOrder={'endTime':'2017-12-21 00:00:00','pageNo':'0','pageSize':'20','startTime':'2017-10-22 00:00:00','status':"","productTypeLevelOne":"CAR_RENTAL","businessModel":"0",'groupId':''}
dictOrder={'endTime':'2017-12-21 00:00:00','pageNo':'0','pageSize':'20','startTime':'2017-10-22 00:00:00','status':"","orderType":1,"businessModel":"0","code":"",'groupId':''}
dictGoodsOrder={'endTime':'2017-12-21 00:00:00','pageNo':'0','pageSize':'10','startTime':'2017-11-22 00:00:00','status':'','contactTelephone':'',"groupId":"","name":u"车票test1"}
login_para={"username":"18030839210","password":"123456"}
#Conventional=countAllOrder().orderListConventional(dictConventional,login_para)#常规订单

#ChOrder=countAllOrder().orderListChOrder(dictChOrder,login_para)#品牌约车

#TaxiOrder=countAllOrder().orderListTaxiOrder(dictTaxiOrder,login_para)#出租车
#CrOrder=countAllOrder().orderListCrOrder(dictCrOrder,login_para)#自驾租车
#Order=countAllOrder().orderListOrder(dictOrder,login_para)#积分订单
GoodsOrder=countAllOrder().orderListGoodsOrder(dictGoodsOrder,login_para)