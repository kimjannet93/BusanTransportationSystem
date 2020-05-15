import os
import cx_Oracle as oci
import csv
import codecs
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()

with open('./bus.csv',encoding='euc-kr') as fp:
    rd = csv.reader(fp)
    next(rd)
    for row in rd:
        print(row)
        data = [row[0],row[2],float(row[6]),float(row[7]),int(row[9])]
        sql = 'INSERT INTO BUS(NO,버스번호,정류장이름,X,Y,BUSTOPID) VALUES (bus_no.NEXTVAL,:1,:2,:3,:4,:5)'
        cursor.execute(sql,data)
        conn.commit()
