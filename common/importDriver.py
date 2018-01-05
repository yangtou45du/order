
import requests
from login import login
import os
import urllib
import xlrd
import pymongo
from pymongo import MongoClient
import xlwt
from xlrd import *
from xlutils.copy import copy

class importDriver():
    def __init__(self):
        dict={"username":"13730687504","password":"123456"}
        self.token = login().Login(dict)
        self.header = {"X-Auth-Token": self.token, "STORE_ID": "59a507e60fbaa0201299a741"}  
    def importDriverGeneral(self):
        '''
        获取司机信息
        getDriverURL="http://stg-firm.ichengke.cn/orange-firm/driver/find?belongType=&driverRoleEnum=&fullName=&groupId=&pageNo=0&pageSize=10&phone="
        getDriver=requests.get(getDriverURL,headers=self.header)
        content=getDriver.text
        print(content)
                    
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
        file=xlwt.Workbook()#指定file以utf-8的格式打开
        table=file.add_sheet("司机.xls",'a+')#指定打开的文件名
        data=[['客运+网约+出租+公交','合营','张',14,'18728014115','男','汉族','成都','这是平台：847038'],
            ['公交','合营','张','强','18728014101','男','汉族','成都','这是平台：847038'],
            ['客运','公营','张',1,'18728014102','男','汉族','成都','这是平台：847038'],
            ['网约','合营','张',2,'18728014103','男','汉族','成都','这是平台：847038'],
            ['出租','公营','张',3,'18728014104','男','汉族','成都','这是平台：847038'],
            ['','合营','张',4,'18728014105','男','汉族','成都','这是平台：847038'],
            ['客运+出租',"",'张',5,'18728014106','男','汉族','成都','这是平台：847038'],
            ['客运+公交','合营',"",6,'18728014107','男','汉族','成都','这是平台：847038'],
            ['网约+出租','公营','张',"",'18728014108','男','汉族','成都','这是平台：847038'],
            ['网约+公交','合营','张',8,"",'男','汉族','成都','这是平台：847038'],
            ['出租+公交','公营','张',9,'18728014110','','汉族','成都','这是平台：847038'],
            ['客运+网约+出租','合营','张',10,'18728014111','男','','成都','这是平台：847038'],
            ['客运+网约+公交','公营','张',11,'18728014112','男','汉族','','这是平台：847038'],
            ['客运+出租+公交','合营','张',12,'18728014113','男','汉族','成都',''],
            ['网约+出租+公交','公营','张',13,'187280141','男','汉族','成都','这是平台：847038']]
        
        for i,p in enumerate(data):
            #print (i,p)
            for j,q in enumerate(p):
                #print(i,j,q)
                t=i+1
                table.write(t,j,q)
        file.save("司机.xls")
        
        
        
        '''
        data={'客运+网约+出租+公交':['合营','张',14,'18728014115','男','汉族','成都','这是平台：847038'],
            '公交':['合营','张强','18728014101','男','汉族','成都','这是平台：847038'],
            '客运':['公营','张',1,'18728014102','男','汉族','成都','这是平台：847038'],
            '网约':['合营','张',2,'18728014103','男','汉族','成都','这是平台：847038'],
            '出租':['公营','张',3,'18728014104','男','汉族','成都','这是平台：847038'],
            '':['合营','张',4,'18728014105','男','汉族','成都','这是平台：847038'],
            '客运+出租':["",'张',5,'18728014106','男','汉族','成都','这是平台：847038'],
            '客运+公交':['合营',"",6,'18728014107','男','汉族','成都','这是平台：847038'],
            '网约+出租':['公营','张',"",'18728014108','男','汉族','成都','这是平台：847038'],
            '网约+公交':['合营','张',8,"",'男','汉族','成都','这是平台：847038'],
            '出租+公交':['公营','张',9,'18728014110','','汉族','成都','这是平台：847038'],
            '客运+网约+出租':['合营','张',10,'18728014111','男','','成都','这是平台：847038'],
            '客运+网约+公交':['公营','张',11,'18728014112','男','汉族','','这是平台：847038'],
            '客运+出租+公交':['合营','张',12,'18728014113','男','汉族','成都',''],
            '网约+出租+公交':['公营','张',13,'187280141','男','汉族','成都','这是平台：847038']}
        dataKey=[]#取出key值
        for key in data:
            dataKey.append(key)
        print(dataKey)
        listData=[]
        for x in dataKey:
            t=[x]
            print(t)
            for i in data[x]:
                t.append(i)
            listData.append(t)
        print(listData)
        '''
            
        



f=importDriver()
f.importDriverGeneral()
