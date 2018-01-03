#!/usr/bin/env python
# -*- coding: cp936 -*-

import time
import datetime
from pymongo import MongoClient
import pymongo
from selenium import webdriver
from common.gaiKuang import gaiKuang
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import *
class countGaiKaung():
    
    def testCaseGaiKuang(self,todayStartDateTime,TodayEndDateTime,yesterdayStartDateTime,yesterdayEndDateTime,dict):
        today=gaiKuang().homePage(todayStartDateTime,TodayEndDateTime)
        yesterday=gaiKuang().homePage(yesterdayStartDateTime,yesterdayEndDateTime)
        print today,yesterday
        driver=webdriver.Chrome()
        driver.get("http://stg-firm.ichengke.cn")#�������
        driver.maximize_window()
        WebDriverWait(driver, 30, 0.5).until(
            EC.presence_of_element_located((By.ID, 'phone1')))
        driver.find_element_by_id("phone1").clear()
        driver.find_element_by_id("phone1").send_keys(dict["username"])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(dict["passwd"])
        # self.driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[3]/div[5]/input").click()
        WebDriverWait(driver, 30, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[1]/a')))
        driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div/div/div[1]/div[2]/ul/li[1]/h3").click()
        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_nav"]/div/ul/li[1]/a/span')))#�ȴ��ſ�����
        todayOrderCompleted=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/a/span").text#��������ɶ���
        todayOrderUnCompleted=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/a/span").text#����δ��ɶ���
        todayPayAmountPerson=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/a/span").text#���ո�������
        todayOrderInCome=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/a/span/text()").text#���ն�������
        todayOrderCompletedPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/p[2]/span[2]").text#��������ɵ��ٱ�
        todayOrderUnCompletedPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/p[2]/span[2]").text#����δ��ɵ��ٱ�
        todayPayAmountPersonPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/p[2]/span[2]").text#���յ��ٸ���������
        todayOrderInComePhoneRate = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/p[2]/span[2]").text  # ���յ��������
        yesterdayOrderCompleted = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/p[3]/span[2]").text  # ��������ɶ���
        yesterdayOrderUnCompleted = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/p[3]/span[2]").text  # ����δ��ɶ���
        yesterdayPayAmountPerson = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/p[3]/span[2]").text  # ���ո�������
        yesterdayOrderInCome=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/p[3]/span[2]").text#���ն�������
        if int(todayOrderCompleted)==int(today[0]):
            print todayOrderCompleted
            print colored("��������ɶ�������ȷ��"+str(today[0]),"green")
        else:
            print todayOrderCompleted
            print colored(("��������ɶ���������ʵ��Ϊ��" + str(todayOrderCompleted)+"Ӧ���ǣ�"+str(today[0])),"red")
        if int(todayOrderUnCompleted)==(today[1]):
            #print "��δ��ɶ�������ȷ��"+str(today[1])
            print colored("��δ��ɶ�������ȷ��" + str(today[1]), "green")
        else:
            #print "����δ��ɶ���������ʵ��Ϊ��" + str(todayOrderUnCompleted)+"Ӧ���ǣ�"+str(today[1])
            print colored(("����δ��ɶ���������ʵ��Ϊ��" + str(todayOrderUnCompleted) + "Ӧ���ǣ�" + str(today[1])), "red")
        if int(todayPayAmountPerson)==int(today[2]):
            #print "���ո���������ȷ��"+str(today[2])
            print colored("���ո���������ȷ��" + str(today[2]), "green")

        else:
            #print "���ո�����������ʵ��Ϊ��" + str(todayPayAmountPerson)+"Ӧ���ǣ�"+str(today[2])
            print colored(("���ո�����������ʵ��Ϊ��" + str(todayPayAmountPerson) + "Ӧ���ǣ�" + str(today[2])), "red")
        '''
        if  float(todayOrderInCome) == float(today[3]):
            print colored("���ն���������ȷ��" + str(today[3]), "green")
        else:
            print colored(("���ն����������ʵ��Ϊ��" + str(todayOrderInCome) + "Ӧ���ǣ�" + str(today[3])), "red")'''
        if str(todayOrderCompletedPhoneRate) == str(today[4]):
            print colored("��������ɶ������ٱ���ȷ��" + str(today[4]), "green")
        else:
            print colored(("��������ɶ������ٱȴ���ʵ��Ϊ��" + str(todayOrderCompletedPhoneRate) + "Ӧ���ǣ�" + str(today[4])), "red")
        if str(todayOrderUnCompletedPhoneRate) == str(today[5]):
            print colored("����δ��ɶ������ٱ���ȷ��" + str(today[5]), "green")
        else:
            print colored(("����δ��ɶ������ٱȴ���ʵ��Ϊ��" + str(todayOrderUnCompletedPhoneRate) + "Ӧ���ǣ�" + str(today[5])), "red")
        if str(todayPayAmountPersonPhoneRate) == str(today[6]):
            print colored("���ո����������ٱ���ȷ��" + str(today[6]), "green")
        else:
            print colored(("���ո����������ٱȴ���ʵ��Ϊ��" + str(todayPayAmountPersonPhoneRate) + "Ӧ���ǣ�" + str(today[6])), "red")
        if str(todayOrderInComePhoneRate) == str(today[7]):
            print colored("���ն���ʵ��������ٱ���ȷ��" + str(today[7]), "green")
        else:
            print colored(("���ն���ʵ��������ٱȴ���ʵ��Ϊ��" + str(todayOrderInComePhoneRate) + "Ӧ���ǣ�" + str(today[7])), "red")
        if int(yesterdayOrderCompleted)==int(yesterday[0]):
            print colored("��������ɶ�������ȷ��"+str(yesterday[0]),"green")
        else:
            print colored(("��������ɶ���������ʵ��Ϊ��" + str(yesterdayOrderCompleted)+"Ӧ���ǣ�"+str(yesterday[0])),"red")
        if int(yesterdayOrderUnCompleted)==(yesterday[1]):

            print colored("����δ��ɶ�������ȷ��" + str(yesterday[1]), "green")
        else:

            print colored(("����δ��ɶ���������ʵ��Ϊ��" + str(yesterdayOrderUnCompleted) + "Ӧ���ǣ�" + str(yesterday[1])), "red")
        if int(yesterdayPayAmountPerson)==int(yesterday[2]):

            print colored("���ո���������ȷ��" + str(yesterday[2]), "green")
        else:

            print colored(("���ո�����������ʵ��Ϊ��" + str(yesterdayPayAmountPerson) + "Ӧ���ǣ�" + str(yesterday[2])), "red")
        '''
        if int(yesterdayOrderInCome) == int(yesterday[3]):
            print colored("���ն���������ȷ��" + str(yesterday[3]), "green")
        else:
            print colored(("���ն����������ʵ��Ϊ��" + str(yesterdayOrderInCome) + "Ӧ���ǣ�" + str(yesterday[3])), "red")
        '''
todayStartDateTime=datetime.datetime(2017, 12, 25, 16, 0, 0, 201000)#2017/12/22/00/00/00
TodayEndDateTime=datetime.datetime(2017, 12, 26, 15, 59, 59, 201000)#2017/12/22/23/59/59
yesterdayStartDateTime=datetime.datetime(2017, 12, 24, 16, 0, 0, 201000)#2017/12/22/00/00/00
yesterdayEndDateTime=datetime.datetime(2017, 12, 25, 15, 59, 59, 201000)#2017/12/22/23/59/59
dict={"username":"18030839210","passwd":"123456"}
f=countGaiKaung().testCaseGaiKuang(todayStartDateTime,TodayEndDateTime,yesterdayStartDateTime,yesterdayEndDateTime,dict)
