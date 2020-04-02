"""
예측 모델을 타자로 입력하여서 알아보자 .

제작자 : 이동현

"""

import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv('add_on_off_eng.csv', index_col= None, header=0)

#종속변수
dependent_variable = df['On/Off']

independent_variables = df[['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen',
                 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]

independent_variables_witt_constrant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable,independent_variables_witt_constrant, missing='drop').fit()

print("예측하게 할 기본 값을 적으세요.")
input_data1 = input("수온 : ")
input_data2 = input("염분 : ")