#!/usr/bin/env python3 
"""
    2019-07-11
    제작 : 이동현
    검수 및 수정 : 김준한
    
    수온, 염분, 용존산소 로지스틱 회귀분석
"""

import pandas as pd
import statsmodels.api as sm
from tqdm import tqdm_notebook

def logistic_Temperature_Salinity_Oxygen (input_file, output_file):

    # header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
    data_frame = pd.read_csv(input_file, header=0)
    # 종속변수로 선언
    dependent_variable = data_frame['On/Off']
    # 독립변수로 선언
    independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen']]
    # 입력변수에 전체 값이 1인 열을 추가
    independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
    # 로지스틱 회귀모형에 피팅 (NaN행 무시)
    logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()
    # 출력
    print(logit_model.summary())
    
    # 회귀계수 해석
    def inverse_logit(model_formula):
        from math import exp
        return (1.0/(1.0+exp(-model_formula)))
    
    # 평균값을 입력시 발생확률
    at_means = float(logit_model.params[0]) + \
        float(logit_model.params[1])*float(data_frame['Temperature'].mean()) + \
        float(logit_model.params[2])*float(data_frame['Salinity'].mean()) + \
        float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'].mean())
    
    probability = (inverse_logit(at_means))*100
    print("'Temperature', 'Salinity', 'Dissolved Oxygen'의 평균 값을 입력시 적조발생 확률 : %.3f %%" % probability)
    
    ###############################################################################
    
    temp_list = []
    sal_list = []
    oxy_list = []
    at_means_list = []
    for i in tqdm_notebook(range(len(data_frame['Observation Date']))):
        
        at_means = float(logit_model.params[0]) + \
        float(logit_model.params[1])*float(data_frame['Temperature'][i]) + \
        float(logit_model.params[2])*float(data_frame['Salinity'][i]) + \
        float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'][i])
        
        temp_list.append(float(data_frame['Temperature'][i]))
        sal_list.append(float(data_frame['Salinity'][i]))
        oxy_list.append(float(data_frame['Dissolved Oxygen'][i]))
        
        # 소수점 3째 자리까지 반올림
        at_means_list.append(round(inverse_logit(at_means), 4))
    
    data = {'Observation Date':data_frame['Observation Date'], 'Temperature': temp_list, 'Salinity':sal_list, 'Dissolved Oxygen':oxy_list, 'On/Off':data_frame['On/Off'], 'Probability':at_means_list}
    df = pd.DataFrame(data)
    
    # Nan행 삭제
    data_edit = df.dropna()
    
    data_edit.to_csv(output_file, index=False)
    
    print(data_edit.head())
    
    # 예측하기
    
    # header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
    data_frame = pd.read_csv(input_file, header=0)
    # 독립변수로 선언
    independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen']]
    
    print('예측하기==============================================================')
    new_observations = data_frame.ix[data_frame.index.isin(range(10)), independent_variables.columns]
    new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
    y_predicted = logit_model.predict(new_observations_with_constant)
    # y_predicted = y_predicted.dropna()
    y_predicted_rounded = [round(score, 4) for score in y_predicted]
    print(y_predicted_rounded)

# test06-1.py
if __name__ == "__main__":
    
    # 함수호출 (입력파일명, 출력파일명)
    logistic_Temperature_Salinity_Oxygen('add_on_off_eng.csv', 'logistic_1.csv')