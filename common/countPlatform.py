#!/usr/bin/env python
# -*- coding: cp936 -*-

import  time
import pymongo
import pymongo
from pymongo import MongoClient

import datetime
class platform():
    def __init__(self):


        client = pymongo.MongoClient('120.24.228.227', 3717)
        userA = 'ora_data'
        password = 'aaaaa8888'
        client.ora_db.authenticate(userA, password, mechanism='SCRAM-SHA-1')
        self.db = client.ora_db  # 连接ora_db数据库，没有则自动创建

    def countPlatform(self):
        self.my_car= self.db.ora_car  # 统计车辆
        carList=self.my_car.find({"storeId": "586a1a0267907f3c72bf6c27","documentState" : 1,"status":1})
        carNumber=0
        for car in carList:
            carNumber=carNumber+1
        print "车辆数为："+str(carNumber)
        self.my_driver=self.db.ora_driver#统计司机
        driverList=self.my_driver.find({"storeId": "586a1a0267907f3c72bf6c27","documentState" : 1,"status":1})
        driverNumber = 0
        for driver in driverList:
            driverNumber = driverNumber + 1
        print "司机数为：" + str(driverNumber)
        self.my_cityproduct = self.db.ora_city_product  # 统计城际产品
        cityproductList = self.my_cityproduct.find({"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1,"status":1})
        cityproductNumber = 0
        for cityproduct in  cityproductList:
            cityproductNumber = cityproductNumber + 1

        #print  "城际"+str(cityproductNumber)
        self.my_airportproduct = self.db.ora_airport_product  # 统计接送飞机产品
        airportproductList = self.my_airportproduct.find({"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1,"status":1})
        airportproductNumber = 0
        for airportproduct in airportproductList:
            airportproductNumber =airportproductNumber + 1

        #print  "接送飞机"+str(airportproductNumber)
        self.my_scenicproduct = self.db.ora_scenic_product  # 统计景点专线产品
        scenicproductList = self.my_scenicproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        scenicproductNumber = 0
        for scenicproduct in scenicproductList:
            scenicproductNumber = scenicproductNumber + 1
        #print  "景点专线" + str(scenicproductNumber)
        self.my_workproduct = self.db.ora_work_product  # 统计工作班车产品
        workproductList = self.my_workproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        workproductNumber = 0
        for workproduct in workproductList:
            workproductNumber = workproductNumber + 1
        #print  "工作班车" + str(workproductNumber)
        self.my_schoolproduct = self.db.ora_school_product  # 统计校园专线产品
        schoolproductList = self.my_schoolproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        schoolproductNumber = 0
        for schoolproduct in schoolproductList:
            schoolproductNumber = schoolproductNumber + 1
        #print  "校园专线" + str(schoolproductNumber)
        self.my_lineproduct = self.db.ora_line_product  # 统计主题包车产品
        lineproductList = self.my_lineproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        lineproductNumber = 0
        for lineproduct in lineproductList:
            lineproductNumber = lineproductNumber + 1
        #print  "主题包车" + str(lineproductNumber)
        self.my_customproduct = self.db.ora_custom_product  # 统计定制包车产品
        customproductList = self.my_customproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        customproductNumber = 0
        for customproduct in customproductList:
            customproductNumber = customproductNumber + 1
        #print  "定制包车" + str(customproductNumber)
        self.my_train_stationproduct = self.db.ora_train_station_product  # 统计接送火车产品
        train_stationproductList = self.my_train_stationproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        train_stationproductNumber = 0
        for train_stationproduct in train_stationproductList:
            train_stationproductNumber = train_stationproductNumber + 1
        #print  "接送火车" + str(train_stationproductNumber)
        self.my_chproduct = self.db.ora_ch_product  # 统计品牌约车产品
        chproductList = self.my_chproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        chproductNumber = 0
        for chproduct in chproductList:
            chproductNumber = chproductNumber + 1
        #print  "品牌约车" + str(chproductNumber)
        self.my_taxiproduct = self.db.ora_taxi_product  # 统计出租的士产品
        taxiproductList = self.my_taxiproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        taxiproductNumber = 0
        for taxiproduct in taxiproductList:
            taxiproductNumber = taxiproductNumber + 1
        #print  "出租的士" + str(taxiproductNumber)
        self.my_car_rentalproduct = self.db.ora_car_rental  # 统计自驾租车产品
        car_rentalproductList = self.my_car_rentalproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        car_rentalproductNumber = 0
        for car_rentalproduct in car_rentalproductList:
            car_rentalproductNumber = car_rentalproductNumber + 1
        #print  "自驾租车" + str(car_rentalproductNumber)
        self.my_public_busproduct = self.db.ora_public_bus_product  # 统计公交产品
        public_busproductList = self.my_public_busproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        public_busproductNumber = 0
        for cpublic_busproduct in public_busproductList:
            public_busproductNumber = public_busproductNumber + 1
        #print  "公交产品" + str(public_busproductNumber)
        self.mystation_busproduct = self.db.ora_station_bus_product  # 统计车站班车产品
        station_busproductList = self.mystation_busproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        station_busproductNumber = 0
        for station_busproduct in station_busproductList:
            station_busproductNumber = station_busproductNumber + 1
        #print  "班线产品" + str(station_busproductNumber)
        self.mytourproduct = self.db.ora_tour_product  # 统计旅游度假产品
        tourproductList = self.mytourproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        tourproductNumber = 0
        for tourproduct in tourproductList:
            tourproductNumber = tourproductNumber + 1
        #print  "旅游度假产品" + str(tourproductNumber)
        productNumber=cityproductNumber+scenicproductNumber+airportproductNumber+workproductNumber+schoolproductNumber+lineproductNumber+customproductNumber+\
              train_stationproductNumber+chproductNumber+taxiproductNumber+car_rentalproductNumber+public_busproductNumber+station_busproductNumber+tourproductNumber

        print "产品总数："+str(productNumber)
        print "班线产品："+str(station_busproductNumber)


f=platform().countPlatform()
