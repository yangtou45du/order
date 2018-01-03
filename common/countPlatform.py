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
        self.db = client.ora_db  # ����ora_db���ݿ⣬û�����Զ�����

    def countPlatform(self):
        self.my_car= self.db.ora_car  # ͳ�Ƴ���
        carList=self.my_car.find({"storeId": "586a1a0267907f3c72bf6c27","documentState" : 1,"status":1})
        carNumber=0
        for car in carList:
            carNumber=carNumber+1
        print "������Ϊ��"+str(carNumber)
        self.my_driver=self.db.ora_driver#ͳ��˾��
        driverList=self.my_driver.find({"storeId": "586a1a0267907f3c72bf6c27","documentState" : 1,"status":1})
        driverNumber = 0
        for driver in driverList:
            driverNumber = driverNumber + 1
        print "˾����Ϊ��" + str(driverNumber)
        self.my_cityproduct = self.db.ora_city_product  # ͳ�ƳǼʲ�Ʒ
        cityproductList = self.my_cityproduct.find({"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1,"status":1})
        cityproductNumber = 0
        for cityproduct in  cityproductList:
            cityproductNumber = cityproductNumber + 1

        #print  "�Ǽ�"+str(cityproductNumber)
        self.my_airportproduct = self.db.ora_airport_product  # ͳ�ƽ��ͷɻ���Ʒ
        airportproductList = self.my_airportproduct.find({"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1,"status":1})
        airportproductNumber = 0
        for airportproduct in airportproductList:
            airportproductNumber =airportproductNumber + 1

        #print  "���ͷɻ�"+str(airportproductNumber)
        self.my_scenicproduct = self.db.ora_scenic_product  # ͳ�ƾ���ר�߲�Ʒ
        scenicproductList = self.my_scenicproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        scenicproductNumber = 0
        for scenicproduct in scenicproductList:
            scenicproductNumber = scenicproductNumber + 1
        #print  "����ר��" + str(scenicproductNumber)
        self.my_workproduct = self.db.ora_work_product  # ͳ�ƹ����೵��Ʒ
        workproductList = self.my_workproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        workproductNumber = 0
        for workproduct in workproductList:
            workproductNumber = workproductNumber + 1
        #print  "�����೵" + str(workproductNumber)
        self.my_schoolproduct = self.db.ora_school_product  # ͳ��У԰ר�߲�Ʒ
        schoolproductList = self.my_schoolproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        schoolproductNumber = 0
        for schoolproduct in schoolproductList:
            schoolproductNumber = schoolproductNumber + 1
        #print  "У԰ר��" + str(schoolproductNumber)
        self.my_lineproduct = self.db.ora_line_product  # ͳ�����������Ʒ
        lineproductList = self.my_lineproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        lineproductNumber = 0
        for lineproduct in lineproductList:
            lineproductNumber = lineproductNumber + 1
        #print  "�������" + str(lineproductNumber)
        self.my_customproduct = self.db.ora_custom_product  # ͳ�ƶ��ư�����Ʒ
        customproductList = self.my_customproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        customproductNumber = 0
        for customproduct in customproductList:
            customproductNumber = customproductNumber + 1
        #print  "���ư���" + str(customproductNumber)
        self.my_train_stationproduct = self.db.ora_train_station_product  # ͳ�ƽ��ͻ𳵲�Ʒ
        train_stationproductList = self.my_train_stationproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        train_stationproductNumber = 0
        for train_stationproduct in train_stationproductList:
            train_stationproductNumber = train_stationproductNumber + 1
        #print  "���ͻ�" + str(train_stationproductNumber)
        self.my_chproduct = self.db.ora_ch_product  # ͳ��Ʒ��Լ����Ʒ
        chproductList = self.my_chproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        chproductNumber = 0
        for chproduct in chproductList:
            chproductNumber = chproductNumber + 1
        #print  "Ʒ��Լ��" + str(chproductNumber)
        self.my_taxiproduct = self.db.ora_taxi_product  # ͳ�Ƴ����ʿ��Ʒ
        taxiproductList = self.my_taxiproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        taxiproductNumber = 0
        for taxiproduct in taxiproductList:
            taxiproductNumber = taxiproductNumber + 1
        #print  "�����ʿ" + str(taxiproductNumber)
        self.my_car_rentalproduct = self.db.ora_car_rental  # ͳ���Լ��⳵��Ʒ
        car_rentalproductList = self.my_car_rentalproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        car_rentalproductNumber = 0
        for car_rentalproduct in car_rentalproductList:
            car_rentalproductNumber = car_rentalproductNumber + 1
        #print  "�Լ��⳵" + str(car_rentalproductNumber)
        self.my_public_busproduct = self.db.ora_public_bus_product  # ͳ�ƹ�����Ʒ
        public_busproductList = self.my_public_busproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        public_busproductNumber = 0
        for cpublic_busproduct in public_busproductList:
            public_busproductNumber = public_busproductNumber + 1
        #print  "������Ʒ" + str(public_busproductNumber)
        self.mystation_busproduct = self.db.ora_station_bus_product  # ͳ�Ƴ�վ�೵��Ʒ
        station_busproductList = self.mystation_busproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        station_busproductNumber = 0
        for station_busproduct in station_busproductList:
            station_busproductNumber = station_busproductNumber + 1
        #print  "���߲�Ʒ" + str(station_busproductNumber)
        self.mytourproduct = self.db.ora_tour_product  # ͳ�����ζȼٲ�Ʒ
        tourproductList = self.mytourproduct.find(
            {"storeId": "586a1a0267907f3c72bf6c27", "documentState": 1, "status": 1})
        tourproductNumber = 0
        for tourproduct in tourproductList:
            tourproductNumber = tourproductNumber + 1
        #print  "���ζȼٲ�Ʒ" + str(tourproductNumber)
        productNumber=cityproductNumber+scenicproductNumber+airportproductNumber+workproductNumber+schoolproductNumber+lineproductNumber+customproductNumber+\
              train_stationproductNumber+chproductNumber+taxiproductNumber+car_rentalproductNumber+public_busproductNumber+station_busproductNumber+tourproductNumber

        print "��Ʒ������"+str(productNumber)
        print "���߲�Ʒ��"+str(station_busproductNumber)


f=platform().countPlatform()
