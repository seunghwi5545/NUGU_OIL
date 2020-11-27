from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import os
import requests
from pyproj import Proj
from pyproj import transform
import datetime
import time
import pandas as pd
from pandas import DataFrame
import telepot
from apscheduler.schedulers.background import BackgroundScheduler

#Functions
def location(): #find users location
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDkx6muQn1Jz-y6hLOcTPVdYAhklm6WJQo'
    data = {
        'considerIp': True,
    }
    result = requests.post(url, data)
    a=result.json()
    lat=a['location']['lat'] # Y point
    lng=a['location']['lng'] # X point
    return lat,lng

def trans(lat,lng): #wgs84 -> tm128
    WGS84 = { 'proj':'latlong', 'datum':'WGS84', 'ellps':'WGS84', }

    TM128 = { 'proj':'tmerc', 'lat_0':'38N', 'lon_0':'128E', 'ellps':'bessel',
   'x_0':'400000', 'y_0':'600000', 'k':'0.9999',
   'towgs84':'-146.43,507.89,681.46'}

    def wgs84_to_tm128(longitude, latitude):
       return transform( Proj(**WGS84), Proj(**TM128), longitude, latitude )
            
    x_point,y_point=wgs84_to_tm128(lng,lat)
    return x_point,y_point

def ask_oil_type(ans):
    if ans == "2번" : #경유
        return "D047"
    elif ans == "1번" : #휘발유
        return "B027"
    else :
        return None

def browse(x_point,y_point,oil_type):
    url = 'http://www.opinet.co.kr/api/aroundAll.do'
    payload = {
        "code" : "F886201116",
        "out" : "json",
        "x" : x_point,
        "y" : y_point,
        "radius" : "1000",
        "prodcd" : oil_type ,
        "sort" : "1"
        }
    result = requests.get(url,params=payload).json()
    return result

def content():
    global data_num
    global oil_list
    global title
    global cost
    data_num = len(oil_list["RESULT"]["OIL"]) #주유소 개수 확인
    
    #if (data_num == 0): #주유소 상호명 -> title
        #return None

    if (data_num == 1):
        for i in range(0, 1):
            title.append(oil_list["RESULT"]["OIL"][i]['OS_NM']) 
    elif (data_num >= 3):
        for i in range(0, 3):  
            title.append(oil_list["RESULT"]["OIL"][i]['OS_NM'])
    elif (data_num == 2):
        for i in range(0,2):
            title.append(oil_list["RESULT"]["OIL"][i]['OS_NM'])

    content_num = data_num

    if content_num == 0: #검색된 주유소가 0개인 경우
        title.append("null")
        cost.append("null")
    elif content_num > 3: #검색된 주유소 3개 초과일 경우 차례대로 3개만 처리
        for i in range(0, 3):
            cost.append(oil_list['RESULT']['OIL'][i]['PRICE'])

    else: #검색된 주유소가 2개 혹은 3개인 경우
        for i in range(content_num):
            cost.append(oil_list['RESULT']['OIL'][i]['PRICE'])
    return title, cost

def action(c):
    global data_num
    keys=['number','title','cost']
    arr=[]
    if data_num == 0: 
        return arr

    elif data_num == 1:
        values = ["1", c[0], c[1]]
        A = dict(zip(keys, values))
        arr.append(A)
        return arr

    elif data_num == 2:
        values_1 = ["1", c[0][0], c[1][0]]
        values_2 = ["2", c[0][1], c[1][1]]
        A = dict(zip(keys, values_1))
        B = dict(zip(keys, values_2))
        arr.append(A)
        arr.append(B)
        return arr

    else:
        values_1 = ["1", c[0][0], c[1][0]]
        values_2 = ["2", c[0][1], c[1][1]]
        values_3 = ["3", c[0][2], c[1][2]]
        A = dict(zip(keys, values_1))
        B = dict(zip(keys, values_2))
        C = dict(zip(keys, values_3))
        arr.append(A)
        arr.append(B)
        arr.append(C)
        return arr
    
def make_response(result_list):
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "COUNT": "0",
            "STATION_INFORMATION": ""
        }
    }
    result_len = len(result_list)
    temp = ""
    if result_len == 0:
        return response
    
    elif result_len>0:
        response["output"]["COUNT"] = str(result_len)

    if result_len == 1:
        temp = str(result_list[0]["title"]) + "," + str(result_list[0]["cost"]) + "원"
        temp = temp.replace(']','')
        temp = temp.replace('[','')
        temp = temp.replace("'",'')
        response["output"]["STATION_INFORMATION"] = temp
    else:
        for i in range(result_len):
            temp = temp + str(result_list[i]["title"]) + "," + str(result_list[i]["cost"]) + "원" + ","
            temp = temp.replace("]","")
            temp =temp.replace("[","")
            temp = temp.replace("'","")
        response["output"]["STATION_INFORMATION"] = temp
    return response


app = Flask(__name__)
api = Api(app)

class Getparams(Resource):
    def post(self):
        data = request.get_json()

        select = data['action']['parameters']['SELECT']['value']
        oil_type = data['action']['parameters']['OIL_TYPE']['value']

        a,b = location()
        a,b = trans(a,b)
        ans = ""
        if oil_type == "경유":
            ans = "2번"
        elif oil_type == "휘발유":
            ans = "1번"
        if select == "1번" or select == "2번":
            ans = select
        global oil_list
        oil_list = browse(a,b,ask_oil_type(ans))

        global data_num
        global title
        global cost
        title = []
        cost = []
        result = action(content())
        response = make_response(result)
        print(response)

        return jsonify(response)

class Getparams2(Resource):
    def post(self):
        data = request.get_json()
        response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "COUNT": "0",
            "STATION_INFORMATION": ""
             }
        }
        print(response)
        return response

api.add_resource(Getparams,'/answer.lowprice.diesel','/answer.lowprice.gasoline','/answer.lowprice.diesel.0','/answer.lowprice.diesel.1','/answer.lowprice.gasoline.0','/answer.lowprice.gasoline.1','/answer.lowprice.select.diesel','/answer.lowprice.select.diesel0','/answer.lowprice.select.diesel1','/answer.lowprice.select.gasoline','/answer.lowprice.select.gasoline0','/answer.lowprice.select.gasoline1')
api.add_resource(Getparams2,'/answer.lowprice','/')

if __name__ == "__main__":
    app.run()
