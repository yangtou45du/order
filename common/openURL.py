#!/usr/bin/env python
# -*- coding: cp936 -*-
import requests
'''
class openURL():
    def openUrl(self):
        obj=requests.get("http://stg-firm.undunion.com/#/in/login")
        if obj.status_code==200:
            print "open URL normal:"+str(obj.status_code)
        else:
            print "open URL fail:"+str(obj.status_code)
        return requests.session()
        '''


#f=openURL().openUrl()
#session = requests.Session()


string="aAddress=%E4%BA%95%E9%99%89%E7%9F%BF%E5%8C%BA&bAddress=%E8%A5%BF%E5%B2%97%E5%8C%BA&" \
            "businessModel=&code=10003870&driverName=%E8%91%9B%E9%A3%9E&endTime=2017-12-21+00:00:00&" \
            "groupId=5976e1ea67907f337cf26daf&licensePlat=E23455&licensePlatProvince=%E5%B7%9D&" \
            "licensePlatType=0&orderSource=0&pageNo=0&pageSize=10&payTimeEnd=2017-12-21+00:00:00&" \
            "payTimeStart=2017-11-22+00:00:00&productTypeLevelOne=CITY_BUS&" \
            "productTypeLevelTwo=CITY_CAR_POOL_BUS&startTime=2017-11-22+00:00:00&status=4"
list=string.split("&")
print list
a={"aAddress":"%E4%BA%95%E9%99%89%E7%9F%BF%E5%8C%BA", 'bAddress':'%E8%A5%BF%E5%B2%97%E5%8C%BA',
'businessModel':"", 'code':'10003870', 'driverName':'%E8%91%9B%E9%A3%9E', 'endTime':'2017-12-21+00:00:00',
'groupId':'5976e1ea67907f337cf26daf', 'licensePlat':'E23455', 'licensePlatProvince':'%E5%B7%9D', 'licensePlatType':'0',
'orderSource':'0', 'pageNo':'0', 'pageSize':'10', 'payTimeEnd':'2017-12-21+00:00:00', 'payTimeStart':'2017-11-22+00:00:00',
'productTypeLevelOne':'CITY_BUS', 'productTypeLevelTwo':'CITY_CAR_POOL_BUS', 'startTime':'2017-11-22+00:00:00', 'status':'4'}
