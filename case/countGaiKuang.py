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
        driver.get("http://stg-firm.ichengke.cn")#打开浏览器
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
        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_nav"]/div/ul/li[1]/a/span')))#等待概况出现
        todayOrderCompleted=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/a/span").text#今日已完成订单
        todayOrderUnCompleted=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/a/span").text#今日未完成订单
        todayPayAmountPerson=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/a/span").text#今日付款人数
        todayOrderInCome=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/a/span/text()").text#今日订单收入
        todayOrderCompletedPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/p[2]/span[2]").text#今日已完成电召比
        todayOrderUnCompletedPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/p[2]/span[2]").text#今日未完成电召比
        todayPayAmountPersonPhoneRate=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/p[2]/span[2]").text#今日电召付款人数比
        todayOrderInComePhoneRate = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/p[2]/span[2]").text  # 今日电召收入比
        yesterdayOrderCompleted = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[1]/p[3]/span[2]").text  # 昨日已完成订单
        yesterdayOrderUnCompleted = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[2]/p[3]/span[2]").text  # 昨日未完成订单
        yesterdayPayAmountPerson = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[3]/p[3]/span[2]").text  # 昨日付款人数
        yesterdayOrderInCome=driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[6]/div[1]/div[1]/div[2]/ul/li[4]/p[3]/span[2]").text#昨日订单收入
        if int(todayOrderCompleted)==int(today[0]):
            print todayOrderCompleted
            print colored("今日已完成订单数正确："+str(today[0]),"green")
        else:
            print todayOrderCompleted
            print colored(("今日已完成订单数错误，实际为：" + str(todayOrderCompleted)+"应该是："+str(today[0])),"red")
        if int(todayOrderUnCompleted)==(today[1]):
            #print "今未完成订单数正确："+str(today[1])
            print colored("今未完成订单数正确：" + str(today[1]), "green")
        else:
            #print "今日未完成订单数错误，实际为：" + str(todayOrderUnCompleted)+"应该是："+str(today[1])
            print colored(("今日未完成订单数错误，实际为：" + str(todayOrderUnCompleted) + "应该是：" + str(today[1])), "red")
        if int(todayPayAmountPerson)==int(today[2]):
            #print "今日付款人数正确："+str(today[2])
            print colored("今日付款人数正确：" + str(today[2]), "green")

        else:
            #print "今日付款人数错误，实际为：" + str(todayPayAmountPerson)+"应该是："+str(today[2])
            print colored(("今日付款人数错误，实际为：" + str(todayPayAmountPerson) + "应该是：" + str(today[2])), "red")
        '''
        if  float(todayOrderInCome) == float(today[3]):
            print colored("今日订单收入正确：" + str(today[3]), "green")
        else:
            print colored(("今日订单收入错误，实际为：" + str(todayOrderInCome) + "应该是：" + str(today[3])), "red")'''
        if str(todayOrderCompletedPhoneRate) == str(today[4]):
            print colored("今日已完成订单电召比正确：" + str(today[4]), "green")
        else:
            print colored(("今日已完成订单电召比错误，实际为：" + str(todayOrderCompletedPhoneRate) + "应该是：" + str(today[4])), "red")
        if str(todayOrderUnCompletedPhoneRate) == str(today[5]):
            print colored("今日未完成订单电召比正确：" + str(today[5]), "green")
        else:
            print colored(("今日未完成订单电召比错误，实际为：" + str(todayOrderUnCompletedPhoneRate) + "应该是：" + str(today[5])), "red")
        if str(todayPayAmountPersonPhoneRate) == str(today[6]):
            print colored("今日付款人数电召比正确：" + str(today[6]), "green")
        else:
            print colored(("今日付款人数电召比错误，实际为：" + str(todayPayAmountPersonPhoneRate) + "应该是：" + str(today[6])), "red")
        if str(todayOrderInComePhoneRate) == str(today[7]):
            print colored("今日订单实际收入电召比正确：" + str(today[7]), "green")
        else:
            print colored(("今日订单实际收入电召比错误，实际为：" + str(todayOrderInComePhoneRate) + "应该是：" + str(today[7])), "red")
        if int(yesterdayOrderCompleted)==int(yesterday[0]):
            print colored("昨日已完成订单数正确："+str(yesterday[0]),"green")
        else:
            print colored(("昨日已完成订单数错误，实际为：" + str(yesterdayOrderCompleted)+"应该是："+str(yesterday[0])),"red")
        if int(yesterdayOrderUnCompleted)==(yesterday[1]):

            print colored("昨日未完成订单数正确：" + str(yesterday[1]), "green")
        else:

            print colored(("昨日未完成订单数错误，实际为：" + str(yesterdayOrderUnCompleted) + "应该是：" + str(yesterday[1])), "red")
        if int(yesterdayPayAmountPerson)==int(yesterday[2]):

            print colored("昨日付款人数正确：" + str(yesterday[2]), "green")
        else:

            print colored(("昨日付款人数错误，实际为：" + str(yesterdayPayAmountPerson) + "应该是：" + str(yesterday[2])), "red")
        '''
        if int(yesterdayOrderInCome) == int(yesterday[3]):
            print colored("昨日订单收入正确：" + str(yesterday[3]), "green")
        else:
            print colored(("昨日订单收入错误，实际为：" + str(yesterdayOrderInCome) + "应该是：" + str(yesterday[3])), "red")
        '''
todayStartDateTime=datetime.datetime(2017, 12, 25, 16, 0, 0, 201000)#2017/12/22/00/00/00
TodayEndDateTime=datetime.datetime(2017, 12, 26, 15, 59, 59, 201000)#2017/12/22/23/59/59
yesterdayStartDateTime=datetime.datetime(2017, 12, 24, 16, 0, 0, 201000)#2017/12/22/00/00/00
yesterdayEndDateTime=datetime.datetime(2017, 12, 25, 15, 59, 59, 201000)#2017/12/22/23/59/59
dict={"username":"18030839210","passwd":"123456"}
f=countGaiKaung().testCaseGaiKuang(todayStartDateTime,TodayEndDateTime,yesterdayStartDateTime,yesterdayEndDateTime,dict)
