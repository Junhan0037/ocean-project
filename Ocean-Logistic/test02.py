#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 김준한

    날짜 형식 변환
"""

import pandas as pd
from dateutil.parser import parse

def change_data_type(input_file, output_file):
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, index_col= None, encoding='cp949')
    
    # Jupter Notebook에서 상태 진행바를 만들어주는 tqdm 모듈
    # cmd창에서 conda install -c conda-forge tqdm
    from tqdm import tqdm_notebook
    
    # 날씨 형식 변환
    i = 0
    for obseration_date in tqdm_notebook(data_frame['관측일시(KST)']) :
        data_frame['관측일시(KST)'][i] = parse(obseration_date).strftime('%Y-%m-%d')
        i += 1
    
    # 파일 만들기
    data_frame.to_csv(output_file, index = None, encoding = 'cp949')

# test02.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명, 출력파일명)
    change_data_type('filtering_row_column.csv', 'change_date_type.csv')