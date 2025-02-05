#!/usr/bin/env python3
"""
    2019-07-11
    제작 : 김준한
    검수 및 수정 : 이동현
    
    염분 그래프 시각화, 표 합치기
"""

import pandas as pd
import matplotlib.pyplot as plt
# 주피터 노트북에서 그래프 생성 시 (%matplotlib inline 추가)

def salinity_graph(input_file1, input_file2, input_file3, input_file4, output_file):
    
    # 해역별 csv파일 불러오기
    df1 = pd.read_csv(input_file1, index_col = None, encoding='cp949')
    df2 = pd.read_csv(input_file2, index_col = None, encoding='cp949')
    df3 = pd.read_csv(input_file3, index_col = None, encoding='cp949')
    df4 = pd.read_csv(input_file4, index_col = None, encoding='cp949')
    
    # 데이터 입력
    date = df1['Date']
    data1 = df1['Salinity_avg'].astype('float')
    data2 = df2['Salinity_avg'].astype('float')
    data3 = df3['Salinity_avg'].astype('float')
    data4 = df4['Salinity_avg'].astype('float')
    
    # 선 그래프
    plt.figure(figsize=(20,8))
    plt.plot(date, data1, 'g', label='East')
    plt.plot(date, data2, 'r', label='South')
    plt.plot(date, data3, 'b', label='West')
    plt.plot(date, data4, 'y', label='East China')
    #plt.grid()
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Salinity')
    plt.title('Sea area Salinity')
    plt.show()
    
    # 막대 그래프
    plt.style.use('ggplot')
    fig = plt.figure(figsize=(20,8))
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(date, data1, align='center', color='g', label='East')
    ax1.bar(date, data2, align='center', color='r', label='South')
    ax1.bar(date, data3, align='center', color='b', label='West')
    ax1.bar(date, data4, align='center', color='y', label='East China')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Salinity')
    plt.title('Sea area Salinity')
    plt.show()
    
    # 점 그래프
    plt.figure(figsize=(20,8))
    plt.scatter(date, data1, s=50, color='g', label='East')
    plt.scatter(date, data2, s=50, color='r', label='South')
    plt.scatter(date, data3, s=50, color='b', label='West')
    plt.scatter(date, data4, s=50, color='y', label='East China')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Salinity')
    plt.title('Sea area Salinity')
    plt.show()
    
    # 상자그림 그래프 (전체 해역 기준)
    data_frame = pd.read_csv('filtering_data_month.csv', index_col = None, encoding='cp949')
    plt.figure(figsize=(20,8))
    plt.boxplot((data_frame.loc[data_frame['Observation Date']==1, 'Salinity'].dropna(), 
                 data_frame.loc[data_frame['Observation Date']==2, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==3, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==4, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==5, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==6, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==7, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==8, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==9, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==10, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==11, 'Salinity'].dropna(),
                 data_frame.loc[data_frame['Observation Date']==12, 'Salinity'].dropna()))
    plt.xlabel('Month')
    plt.ylabel('Salinity')
    plt.title('Sea area Salinity')
    plt.show()
    
    # 표 합치기
    df = pd.concat([df1, df2, df3, df4])
    
    # 출력
    df.to_csv(output_file, index= None, encoding='cp949')

# test03-2.py
if __name__ == "__main__":
    
    # 함수 호출 (동해, 남해, 서해, 동중국해, 출력파일명)
    salinity_graph('east_ocean.csv', 'south_ocean.csv', 'west_ocean.csv', 'east_china_ocean.csv', 'ocean_month.csv')