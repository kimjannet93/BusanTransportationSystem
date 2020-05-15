import pandas as pd
import cx_Oracle as oci
 
df = pd.read_excel('./data/Floating Population by Time Zone by Region2019.xlsx', sheet_name='시간대별 유동인구 현황(명)',header=2,dtype={0:str, 1:str,2:str,3:str,4:str,5:float,6:float,7:str})
# print(df)
df['시간'] = df['시간'].apply(lambda x: x.replace('시','')).astype('float')
df1 = df[['년','월','시간','구군','시간_유동인구']]
# df1['시간'].apply(lambda x: x.replace('시','')).astype('float')
# print(df)
# 'ab'.replace('a','b')
# print(df1)
rows = [tuple(x) for x in df1.to_records(index=False)]
# # print(rows[0])
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
 
cursor = conn.cursor()
 
cursor.executemany("INSERT INTO FP_TIME (NO, 연도, 월, 시간, 시군구, 유동인구) VALUES (fpt_no.NEXTVAL,:1,:2,:3,:4,:5)", rows)
conn.commit()
 