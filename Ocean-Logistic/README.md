[test00.py]

설명 : 2000년~2017년 정선해양관측자료 통합

입력 : 정선해양관측정보_2000~2017.xls

출력 : ocean_all_data.csv


[test01.py]

설명 : 필요한 열 필터링 (수심 0)

입력 : ocean_all_data.csv

출력 : filtering_row_column.csv


[test02.py]

설명 : 날짜 형식 변환

입력 : filtering_row_column.csv

출력 : change_date_type.csv


[test03.py]

설명 : 2000~2017년 적조데이터 웹 크롤링

출력 : result01.csv


[test04.py]

설명 : 적조 발생여부 표시

입력 : result01.csv

입력 : change_date_type.csv

출력 : add_on_off.csv


[test05.py]

설명 : 날짜별 평균값을 구하여 따로 csv에 저장, 컬럼 명 수정

입력 : add_on_off.csv

출력 : add_on_off_eng.csv

출력 : average values.csv


[test06-1.py]

설명 : 수온, 염분, 용존산소 로지스틱 회귀분석

입력 : add_on_off_eng.csv

출력 : logistic_1.csv


[test06-2.py]

설명 : 인산염인, 아질산질소, 질산규소, 규산수소 로지스틱 회귀분석

입력 : add_on_off_eng.csv

출력 : logistic_2.csv


[test06-3.py]
설명 : 수온, 염분, 용존산소, 인산염인, 아질산질소, 질산규소, 규산수소 로지스틱 회귀분석

입력 : add_on_off_eng.csv

출력 : logistic_3.csv


[test07.py]

설명 : 적중률 계산

입력 : logistic_3.csv


[test08.py]

설명 : 로지스틱 회귀선 그리기

입력 : logistic_3.csv


[test09.py]

설명 : DB 연동

입력 : Oracle DataBase