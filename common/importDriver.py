
import requests
from login import login
import os
import urllib
import xlrd
import pymongo
from pymongo import MongoClient

class importDriver():
    def __init__(self):
        dict={"username":"13730687504","password":"123456"}
        self.token = login().Login(dict)
        self.header = {"X-Auth-Token": self.token, "STORE_ID": "59a507e60fbaa0201299a741"}  
    def importDriverGeneral(self):
        getDriverURL="http://stg-firm.ichengke.cn/orange-firm/driver/find?belongType=&driverRoleEnum=&fullName=&groupId=&pageNo=0&pageSize=10&phone="
        getDriver=requests.get(getDriverURL,headers=self.header)
        content=getDriver.text
        print(content)
        
        '''
        if os.path.exists(r"D:\\Downloads\\司机.xlsx"):
            os.remove (r"D:\\Downloads\\司机.xlsx")             
        URL="http://stg-firm.ichengke.cn/static/importDriverFile/%E5%8F%B8%E6%9C%BA.xlsx" 
        LOCAL=os.path.join('D:\\Downloads','司机.xlsx')
        urllib.request.urlretrieve(URL,LOCAL)#从网页下载excel表格
        if os.path.exists(r"D:\\Downloads\\司机.xlsx"):
            print('下载司机表格成功')
        
        openFile=xlrd.open_workbook("D:\\Downloads\\司机.xlsx")#打开表格
        table=openFile.sheets()[0]#获取第一个表格里面的数据
        for rownum in range(1,table.nrows):
            print(table.row_values(rownum))
        '''



f=importDriver()
f.importDriverGeneral()
