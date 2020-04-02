#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 이동현
    
    컬럼 명 수정, 쓸데없는 값 제거
    날짜별 평균값을 구하여 따로 csv에 저장
"""

import pandas as pd
import numpy as np
from tqdm import tqdm_notebook

def Calculate_Avg(input_file, output_file1, output_file2):
    
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, header=0, encoding='cp949')
    
    # 컬럼 이름 변경
    data_frame.rename(columns = {'관측일시(KST)':'Observation Date',
                                 '수온(℃)':'Temperature',
                                 '염분(psu)':'Salinity',
                                 '용존산소(ml/L)':'Dissolved Oxygen',
                                 '인산염인 \n(ug-at/L)':'Phosphate Phosphorus',
                                 '아질산질소\n(ug-at/L)':'Nitrous Acid Nitrogen',
                                 '질산질소\n(ug-at/L)':'Nitric Acid Nitrogen',
                                 '규산규소\n(ug-at/L)':'Silicic Acid Silicon'}, inplace=True)
    
    #염분 99.999 제거 하기 (그 행을 삭제 시켜줍시다.)
    data_frame = data_frame[data_frame['Salinity'] <= 90]

    #인산염인, 아질산질소, 질산규소의 type이 object로 있어서 형변환 (errors='coerce' : 오류데이터인 경우 Nan으로 변환)
    data_frame['Phosphate Phosphorus'] = pd.to_numeric(data_frame['Phosphate Phosphorus'], errors='coerce')
    data_frame['Nitrous Acid Nitrogen'] = pd.to_numeric(data_frame['Nitrous Acid Nitrogen'], errors='coerce')
    data_frame['Nitric Acid Nitrogen'] = pd.to_numeric(data_frame['Nitric Acid Nitrogen'], errors='coerce')
    
    # 파일 저장
    data_frame.to_csv(output_file1, index=False, encoding='cp949')
    
    # 평균값 컬럼 추가
    data_frame['Grouped_Date'] = np.nan
    data_frame['Avg_Temp'] = np.nan
    data_frame['Avg_Sal'] = np.nan
    data_frame['Avg_Oxy'] = np.nan
    data_frame['Avg_Phosphorus'] = np.nan
    data_frame['Avg_Nitrous'] = np.nan
    data_frame['Avg_Nitric'] = np.nan
    data_frame['Avg_Silicon'] = np.nan
    
    # 위에 만들어 놓았던,데이터 프레임에서 온도 부분의 열에서 data_frampe
    # groupby가 많이 쓰이는데, 여러가지를 사용할 수 있다.
    # 파일을 전체적으로 찝어서 뭔가를 하기 위해서 사용하는데 그 찝는 기능을 한다.
    # 나누거나 합치거나 찾거나 등등 모두 가능하다.
    
    # 데이터 프레임에서 온도 부분을 첫번쨰 날짜와 찝어준거죠.?
    # 데이터프레임에 딕셔너리 같은 느낌으로 자료 그룹의 2개를 놓고 행할때 쓰기 위해서 
    # 이런식으로 구분.
    
    # 날짜를 기준으로 온도값을 그룹화
    grouped_temperature = data_frame['Temperature'].groupby(data_frame['Observation Date'])
    i = 0
    for index in tqdm_notebook(grouped_temperature.mean().index): # index에는 그룹화의 기준인 날짜 데이터가 들어있다.
        data_frame['Grouped_Date'][i] = index
        i += 1
        
    i = 0
    for value in tqdm_notebook(grouped_temperature.mean().values): # value에는 수온값이 들어있다.
        data_frame['Avg_Temp'][i] = round(value, 3)
        i += 1
    
    grouped_salinity = data_frame['Salinity'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_salinity.mean().values): # 염분
        data_frame['Avg_Sal'][i] = round(value, 3)
        i += 1
    
    grouped_Oxygen = data_frame['Dissolved Oxygen'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_Oxygen.mean().values): # 용존산소
        data_frame['Avg_Oxy'][i] = round(value, 3)
        i += 1
    
    grouped_Phosphorus = data_frame['Phosphate Phosphorus'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_Phosphorus.mean().values): # 인산염인
        data_frame['Avg_Phosphorus'][i] = round(value, 3)
        i += 1
    
    grouped_Nitrous = data_frame['Nitrous Acid Nitrogen'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_Nitrous.mean().values): # 아질산질소
        data_frame['Avg_Nitrous'][i] = round(value, 3)
        i += 1
        
    grouped_Nitric = data_frame['Nitric Acid Nitrogen'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_Nitric.mean().values): # 질산규소
        data_frame['Avg_Nitric'][i] = round(value, 3)
        i += 1
        
    grouped_Silicon = data_frame['Silicic Acid Silicon'].groupby(data_frame['Observation Date'])
    i = 0
    for value in tqdm_notebook(grouped_Silicon.mean().values): # 규산수소
        data_frame['Avg_Silicon'][i] = round(value, 3)
        i += 1  
    
    # 해양관측정보와 평균값들을 다른 파일로 처리
    df = data_frame.loc[:, ['Grouped_Date','Avg_Temp','Avg_Sal','Avg_Oxy', 'Avg_Phosphorus', 'Avg_Nitrous', 'Avg_Nitric', 'Avg_Silicon']]
    df.to_csv(output_file2, index=False, encoding='cp949')

# test05.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명, 출력파일명)
    Calculate_Avg('add_on_off.csv', 'add_on_off_eng.csv', 'average values.csv')