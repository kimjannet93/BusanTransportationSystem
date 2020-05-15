from selenium import webdriver
from bs4 import BeautifulSoup
import time, urllib.request, requests, json, csv, random, os
from selenium.webdriver import ChromeOptions
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()

select_sql = 'SELECT NO,X,Y FROM BUS'
cursor.execute(select_sql)
xys = cursor.fetchall()
success = 1

for xy in xys:
    bustop = xy[0]
    print(success)
    x = xy[1]
    y = xy[2]
    open_api = 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=%s&y=%s&input_coord=WGS84'%(x,y)
    api_key = 'f56b92905ade194d1254314f9e91d103'

    res = requests.get(open_api, headers={'Authorization' : 'KakaoAK ' + api_key } )
    dic1 = res.json()
    try:
        result = dic1['documents'][0]['address']
        data = [result['region_1depth_name'],result['region_2depth_name'],result['region_3depth_name'],bustop]
        update_sql = 'UPDATE BUS SET 시도=:1, 시군구=:2, 읍면동=:3 WHERE NO=:4'
        cursor.execute(update_sql,data)
        conn.commit()
        success += 1
    except:
        pass