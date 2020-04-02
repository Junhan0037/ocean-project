#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 이동현
    검수 및 수정 : 김준한
    
    발생여부 표시 및 붙이기
"""

import pandas as pd
from tqdm import tqdm_notebook

def add_on_off(input_file1, input_file2, output_file) :
    
    # 웹크롤링 파일은 헤더가 없으므로 header=None
    # 기본데이터파일은 헤더줄을 생략하기위해 header=0
    df1 = pd.read_csv(input_file1, header=None, encoding='cp949')
    df2 = pd.read_csv(input_file2, header=0, encoding='cp949')
    
    # 웹크롤링 파일의 첫번째 컬럼 데이터 반복
    for date_index in tqdm_notebook(df1[0]):
        i = 0
        # 데이터의 필요없는 부분 제거
        date_index = str(date_index).lstrip('[').rstrip(']').strip('\'')

        # 데이터 파일의 '관측일시(KST)' 컬럼 데이터 반복
        for OD_index in df2['관측일시(KST)']:
            # 날짜가 같은 부분을 찾아서 '1'로 변경
            if date_index == OD_index:
                df2['On/Off'][i] = 1
            i += 1
    
    # 파일 저장
    df2.to_csv(output_file, index=False, encoding='cp949')

# test04.py
if __name__ == "__main__":
    
    # 'ON/OFF'컬럼 추가
    df = pd.read_csv('change_date_type.csv', header=0, encoding='cp949')
    df['On/Off'] = 0
    df.to_csv('change_date_type.csv', index=False, encoding='cp949')
    
    # 함수호출 (웹크롤링파일명, 입력파일명, 출력파일명)
    add_on_off('result01.csv', 'change_date_type.csv', 'add_on_off.csv')