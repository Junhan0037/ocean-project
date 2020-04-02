#!/usr/bin/env python3 
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 이동현
    
    적중률 계산
"""

import pandas as pd
from tqdm import tqdm_notebook

def accuracy_rate (input_file):
    
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, header=0)
    # 적조발생유무, 적조발생확률(50%)를 기준으로 적중률 계산
    hit = 0
    miss = 0
    for i in tqdm_notebook(range(len(data_frame))):
        if (data_frame['On/Off'][i]==1 and data_frame['Probability'][i]>=0.5) or (data_frame['On/Off'][i]==0 and data_frame['Probability'][i]<0.5):
            hit += 1
        else :
            miss += 1
    # 출력
    print(hit)
    print(miss)
    print(len(data_frame))
    hit = hit / len(data_frame)
    print("적중 : %s%%" % round((hit*100), 3))
    miss = miss / len(data_frame)
    print("비적중 : %s%%" % round((miss*100), 3))
    
# test07.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명)
    accuracy_rate('logistic_3.csv')