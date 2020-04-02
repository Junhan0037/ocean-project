#!/usr/bin/env python3 
"""
    2019-07-02
    제작 : 김준한
    검수 및 수정 : 김준한
    
    로지스틱 회귀선 그리기
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook
# 주피터 노트북에서 그래프 생성 시 (%matplotlib inline 추가)

def logistic_regression_line(input_file):
    
    # 파일 불러오기
    data_frame = pd.read_csv(input_file, header=0)
    
    # 그래프 설정
    sns.set(color_codes=True)
    # 독립변수 선언
    independent_variables = ['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']

    i = 0
    # 그래프 생성
    for i in tqdm_notebook(range(len(independent_variables))):
        sns.lmplot(x=independent_variables[i], y="On/Off", data=data_frame, logistic=True, y_jitter=.03).set_axis_labels(independent_variables[i], "Probability")
        # 그래프 제목
        plt.title(independent_variables[i] + " Logistic Regression")
        # 그래프 출력
        #plt.show()
        plt.savefig(str(i) + ".png")
        i = i + 1

# test08.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명)
    logistic_regression_line('logistic_3.csv')