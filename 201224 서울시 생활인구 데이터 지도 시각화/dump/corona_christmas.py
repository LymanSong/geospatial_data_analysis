import os
import numpy as np
import pandas as pd 
import streamlit as st 
import altair as alt 
from datetime import datetime
import pydeck as pdk 

# 행정동 중심좌표 데이터 출처: https://torrms.tistory.com/55
# 생활인구 데이터 출처: https://data.seoul.go.kr/dataList/OA-15377/F/1/datasetView.do#



# 1. 파일 불러오기
df = pd.read_csv('INNER_PEOPLE_20201224.csv', encoding='cp949')
df = df[['?"기준일ID"', '시간대구분', '행정동코드', '거주지 자치구 코드', '총생활인구수']]
code_df = pd.read_csv('행정동_중심좌표_수정.csv', encoding='cp949') #번1동,2동,3동, 수유1동,2동,3동 수정


# 2. code_df에서 중심좌표를 뽑아 저장할 열 생성 (경도, 위도)
df['중심좌표(경도)'] = float(0)
df['중심좌표(위도)'] = float(0)


# 3. 해당 행정동 코드에 맞는 중심좌표 찾기 
print(code_df.dtypes)
print(df.dtypes)
for i in range(len(df)): 
    code = (str(int(df.iloc[i]['행정동코드'])) + '00')
   
    x_crd = code_df['경도'][code_df['코드'] == int(code)].values[0]
    y_crd = code_df['위도'][code_df['코드'] == int(code)].values[0]
    
    df.loc[i, '중심좌표(경도)'] = x_crd
    df.loc[i, '중심좌표(위도)'] = y_crd
    
    
    if i%100 == 0:
        print('{} out of {}...'.format(i/100, len(df)/100))
        
 
df.to_csv('20201224.csv')
























