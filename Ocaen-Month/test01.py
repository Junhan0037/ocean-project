#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 이동현
    
    필요한 열 필터링, 날짜 (월별) 데이터 추출
"""

import pandas as pd
from dateutil.parser import parse
from tqdm import tqdm_notebook

def filtering_data_date(input_file, output_file):
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, index_col = None, encoding='cp949')
    
    # 필요한 열 추출
    data_frame = data_frame.iloc[:,[0,6,8,10,12,15,16,17,18]]
    
    # 속성 이름 변경
    data_frame.rename(columns = {'해역':'Sea_area',
                                 '관측일시(KST)':'Observation Date',
                                 '수온(℃)':'Temperature',
                                 '염분(psu)':'Salinity',
                                 '용존산소(ml/L)':'Dissolved Oxygen',
                                 '인산염인 \n(ug-at/L)':'Phosphate Phosphorus',
                                 '아질산질소\n(ug-at/L)':'Nitrous Acid Nitrogen',
                                 '질산질소\n(ug-at/L)':'Nitric Acid Nitrogen',
                                 '규산규소\n(ug-at/L)':'Silicic Acid Silicon'}, inplace=True)
    
    # 날짜 데이터에 월만 추출하기
    i = 0
    for date_time in tqdm_notebook(data_frame['Observation Date']):
        data_frame['Observation Date'][i] = parse(date_time).strftime('%m')
        i = i + 1
    
    # 염분 99.999 제거 하기 (그 행을 삭제 시켜줍시다.)
    data_frame = data_frame[data_frame['Salinity'] <= 90]
    
    # 인산염인, 아질산질소, 질산규소의 type이 object로 있어서 형변환 (errors='coerce' : 오류데이터인 경우 Nan으로 변환)
    data_frame['Phosphate Phosphorus'] = pd.to_numeric(data_frame['Phosphate Phosphorus'], errors='coerce')
    data_frame['Nitrous Acid Nitrogen'] = pd.to_numeric(data_frame['Nitrous Acid Nitrogen'], errors='coerce')
    data_frame['Nitric Acid Nitrogen'] = pd.to_numeric(data_frame['Nitric Acid Nitrogen'], errors='coerce')
    
    # 출력
    data_frame.to_csv(output_file, index = None, encoding = 'cp949')

# test01.py
if __name__ == "__main__":
    
    filtering_data_date('ocean_all_data.csv', 'filtering_data_month.csv')