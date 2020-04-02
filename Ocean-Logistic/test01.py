#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 김준한
    
    필요한 열을 필터링 한다.
"""

import pandas as pd

def filtering (input_file, output_file):
    
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, index_col= None, encoding='cp949')
    
    # iloc는 행, 열을 숫자로만 구분하여 추출 할 수 있다.
    # 수심 0으로 필터링
    data_frame = data_frame[data_frame.iloc[:,7] == 0]
    
    # 원하는 해역 추출 (ex. 남해)
    # data_frame = data_frame[data_frame.iloc[:,0]=='남해']
    
    # loc는 행, 열을 이름으로 구분하는데. 숨겨진 이스케이프 문자가 많아서 iloc로 해당 열 번호 입력
    # 원하는 열만 추출
    data_frame = data_frame.iloc[:,[6,8,10,12,15,16,17,18]]
    
    # 파일 만들기
    data_frame.to_csv(output_file, index = None, encoding = 'cp949')

# test01.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명, 출력파일명)
    filtering('ocean_all_data.csv', 'filtering_row_column.csv')