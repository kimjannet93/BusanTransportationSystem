# import cx_Oracle as oci
# import pandas as pd 

# conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')

# df = pd.read_sql_query("select * from bus", conn)

# print(df.head())


import pandas as pd
import cx_Oracle as oci
 
df = pd.read_excel('./data/지역에 따른 주중_주말 유동 2019년.xlsx', sheet_name='요일별 평균 유동인구 현황(명)',header=2,dtype={0:str, 1:str,2:str,3:str,4:str,5:str,6:str,7:float,8:float,9:str})
# print(df)
df1 = df[['년','월','요일','구군','읍면동','주중/주말 유동인구']]
# print(df1)
rows = [tuple(x) for x in df1.to_records(index=False)]
# print(rows[0])
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding='utf-8')
 
cursor = conn.cursor()
 
cursor.executemany("INSERT INTO FP_WEEK (NO, 연도, 월, 요일, 시군구, 읍면동, 유동인구) VALUES (fp_no.NEXTVAL,:1,:2,:3,:4,:5,:6)", rows)
conn.commit()
 
 
