#!/usr/bin/env python3 
"""
    2019-07-11
    제작 : 김준한, 이동현
    검수 및 수정 : 김준한
    
    DB 연동
"""

from __future__ import print_function
import cx_Oracle

# 한글지원
import os
os.putenv('NLS_LANG', '.UTF8')

# 접속
# '서비스'에 들어가서 오라클 관련된 것들 실행시키기!
connection = cx_Oracle.connect('scott','tiger','localhost/JHKIM')
cursor = connection.cursor()

# SQL문
cursor.execute("""
    select ROUND(AVG(TEMPERATURE), 3), ROUND(AVG(SALINITY), 3), ROUND(AVG(OXYGEN), 3)
    from marine
    where sea_area = :ocean""",
    ocean = "동해"
)

print("[결과]")
for temp in cursor:
    print("평균 수온 : ", temp[0], "평균 염분 : ", temp[1], "평균 용존산소 : ", temp[2])