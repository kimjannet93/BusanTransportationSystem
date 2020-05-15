import os
import csv
import cx_Oracle as oci

file_list = os.listdir('./부산 콜택시(15.2~19.9)')

page = 1
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
cursor = conn.cursor()

for file_name in file_list:
    filepath = os.path.join('./부산 콜택시(15.2~19.9)/',file_name)
    with open(filepath,'r',encoding='utf-8') as fp:
        rd = csv.reader(fp)
        next(rd)
        for row in rd:
            data = [row[0],row[1],int(row[2]),row[3],row[4],row[5],int(row[6])]
            sql = 'INSERT INTO TAXI(NO,기준년월일,요일,시간대,발신지_시도,발신지_시군구,발신지_읍면동,통화건수) VALUES (taxi_no.NEXTVAL,:1,:2,:3,:4,:5,:6,:7)'
            cursor.execute(sql,data)
            conn.commit()
        print(page)
        page += 1
    
