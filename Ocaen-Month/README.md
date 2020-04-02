﻿[test00.py]

설명 : 2000년~2017년 정선해양관측자료 통합, 수심 0으로 필터링

입력 : 정선해양관측정보_2000~2017.xls

출력 : ocean_all_data.csv


[test01.py]

설명 : 필요한 열 필터링, 날짜 (월별) 데이터 추출, 이상한 값 제거

입력 : ocean_all_data.csv

출력 : filtering_data_month.csv


[test02-1.py]

설명 : 동해 월별 요소들의 평균값 정리

입력 : filtering_data_month.csv

출력 : east_ocean.csv


[test02-2.py]

설명 : 남해 월별 요소들의 평균값 정리

입력 : filtering_data_month.csv

출력 : south_ocean.csv


[test02-3.py]

설명 : 서해 월별 요소들의 평균값 정리

입력 : filtering_data_month.csv

출력 : west_ocean.csv


[test02-4.py]

설명 : 동중국해 월별 요소들의 평균값 정리

입력 : filtering_data_month.csv

출력 : east_china_ocean.csv


[test03-1.py]

설명 : 월별 수온 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-2.py]

설명 : 월별 염분 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-3.py]

설명 : 월별 용존산소 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-4.py]

설명 : 월별 인산염인 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-5.py]

설명 : 월별 아질산질소 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-6.py]

설명 : 월별 질산규소 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv


[test03-7.py]

설명 : 월별 규산수소 그래프 시각화 및 통합

입력 : east_ocean.csv, south_ocean.csv, west_ocean.csv, east_china_ocean.csv

출력 : ocean_month.csv

