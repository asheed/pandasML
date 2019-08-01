# -*- coding: utf-8 -*-

import pandas as pd

# 튜플은 시리즈로 변환
tup_data = ('영인', '2010-05-01', '여', True)
sr3 = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr3)

# 원소를 한개 선택
print(sr3[0])    # sr의 1번째 원소를 선택(정수형 위치 인덱스)
print(sr3['이름']) # '이름' 라벨을 가진 원소를 선택(인덱스 이름)
print()
# 여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr3[[1,2]])
print()
print(sr3[['생년월일', '성별']])

print()
# 여러 개의 원소를 선택
print(sr3[1:2])
print()
print(sr3['생년월일':'성별'])