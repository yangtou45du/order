
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
import json
import time
import base64 
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
        '''
        if os.path.exists(r"D:\\Downloads\\司机.xls"):
            os.remove (r"D:\\Downloads\\司机.xls")  
        
        os.chdir("D:\\Downloads")   
        file=xlwt.Workbook()#指定file以utf-8的格式打开
        table=file.add_sheet("司机.xls",'a+')#指定打开的文件名
        for i,p in enumerate(data):
            #print (i,p)
            for j,q in enumerate(p):#写入司机信息
                #print(i,j,q)
                t=i+1
                table.write(t,j,q)
        file.save("司机.xls")
        '''
        
        driverURL='http://stg-firm.ichengke.cn/orange-firm/driver/find?'
        driverdict={'belongType':'','driverRoleEnum':'','fullName':'','groupId':'','pageNo':'','pageSize':100,'phone':''}
        getDriver=requests.get(driverURL,data=driverdict,headers=self.header)
        data=[['司机类型','隶属关系','姓','名','手机号','性别','民族','服务城市','所属分组','身份证号码',
            '准驾车型','驾驶证领证日期','驾驶证有效期至','客运从业资格证','客运从业资格证有效期至',
            '出租从业资格证','出租从业资格证有效期至','出租司机服务监督卡','监督卡有效期至','网约从业资格证',
            '网约从业资格证有效期至'],
            ['客运+网约+出租+公交','合营','张',14,'18728014115','男','汉族','成都','这是平台：847038',
            '510622198108050000','A1','2013/8/9','2019/8/9','510622198108050000','2019/8/9',
            '510622198108050000','2019/8/9','510622198108050000','2019/8/9','510622198108050000','2019/8/9'],
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
        phoneList=[]
        for phone in data:#获取所有的手机号
            phoneList.append(phone[4])
        #print (phoneList)
        result=getDriver.json()["resultData"]
        driver=result['content']
        
        #print(driver[0]['id'])
        for phone in driver:           
            if phone['phone'] in phoneList:
                phoneID=phone['id']
                unbindurl='http://stg-firm.ichengke.cn/orange-firm/driver/'+str(phoneID)+'/unbind'
                unbind=requests.post(unbindurl,headers=self.header)
                if unbind.status_code==200:
                    print("下架司机成功")
                deleurl="http://stg-firm.ichengke.cn/orange-firm/driverOffShelf/"+str(phoneID)+"/delete"
                deleDriver=requests.post(deleurl,headers=self.header)
                if deleDriver.status_code==200:
                    print("删除司机成功")               
        os.chdir("D:\\Downloads")
        if os.path.exists(r"D:\\Downloads\\司机.xls"):
            os.remove (r"D:\\Downloads\\司机.xls")        
        file=xlwt.Workbook()#指定file以utf-8的格式打开
        table=file.add_sheet("司机.xls",'a+')#指定打开的文件名
        for i,p in enumerate(data):
            #print (i,p)
            for j,q in enumerate(p):#写入司机信息
                #print(i,j,q)              
                table.write(i,j,q)
        file.save("司机.xls")  
        #开始导入司机
        
        boundary = '----WebKitFormBoundary%s' % hex(int(time.time() * 1000))
        '''
        data = []
        data.append('--%s' % boundary)               
        data.append('Content-Disposition: form-data; name="file"; filename="司机.xls"')        
        data.append('Content-Type: application/octet-stream') 
        fr=open(r'司机.xls','rb')        
        data.append(fr.read())
        fr.close()
        data.append('--%s\r\n' % boundary)
        http_body='\r\n'.join(data) 
        print(http_body)
        '''
        
        file={'file':('司机.xls',open(r'司机.xls','rb'),'application/octet-stream')}    
        #print(file)
        #file={'file':open(r'D:\Downloads\司机.xls','rb')}       
        # payload={ 'name':"file",'filename':"司机.xls"}
        url="http://stg-firm.ichengke.cn/orange-firm/driver/importDriver"
        #importDriver=requests.post(url,data=http_body,headers=self.header)
        #print(self.header)
        importDriver=requests.post(url,files=file,headers=self.header)
        print(importDriver.text)
            
        



f=importDriver()
f.importDriverGeneral()
