#!/usr/bin/env python
# -*- coding: cp936 -*-
import requests
#from openURL import openURL

class login():
    def __init__(self):
        pass
        #cookie=openURL().openUrl()
    def Login(self,dict):

        url="http://stg-firm.undunion.com/orange-firm/firmUser/a/login"
        r=requests.post(url,data=dict)
        token = r.json()["resultData"]
        print "login ok:"+str(r.status_code)
        return token


#dict={"username":"18030839210","password":"123456"}
#f=login()
#f.Login(dict)
