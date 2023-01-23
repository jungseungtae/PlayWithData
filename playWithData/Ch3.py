## Chapter 3. 사드 배치의 영향으로 중국인 관광객이 얼마나 줄었을까?

import os
import pandas as pd

## Set Path

os.chdir(r'C:\Users\USER\Downloads\datasalon-master\datasalon-master\01_초판\3_Tourists_Event\files')
# print(os.getcwd())

## Load Data
# kto_201901 = pd.read_excel('kto_201901.xlsx',
#                            header= 1,
#                            usecols='A:G',
#                            skipfooter=4)
# print(kto_201901.info)
# print(kto_201901.describe())

## 0값 필터링
# condition = (kto_201901['관광'] == 0) \
#           | (kto_201901['상용'] == 0) \
#           | (kto_201901['공용'] == 0) \
#           | (kto_201901['유학/연수'] == 0)
# print(kto_201901[condition])

# kto_201901['기준연월'] = '2019-01'
# print(kto_201901.head())

# print(kto_201901['국적'].unique())

## 대륙 목록 만들기
# continents_list = ['아시아주', '미주','구주','대양주','아프리카주','기타대륙','교포소계']

## 대륙 목록 제거
# condition = (kto_201901.국적.isin(continents_list) == False)
# kto_201901_country = kto_201901[condition]
# print(kto_201901_country['국적'].unique())

# print(kto_201901_country.tail())

# kto_201901_country_newindex = kto_201901_country.reset_index(drop = True)
# print(kto_201901_country_newindex.head())

## 대륙 컬럼 생성
# continents = ['아시아'] * 25 + ['아메리카'] * 5 + ['유럽'] * 23 + ['오세아니아'] * 3 \
#            + ['아프리카'] * 2 + ['기타대륙'] + ['교포']
# print(continents)

# kto_201901_country_newindex['대륙'] = continents
# print(kto_201901_country_newindex.head())
# print(kto_201901_country_newindex.tail())

## 관광객 비율 컬럼 만들기
# kto_201901_country_newindex['관광객비율(%)'] = \
# round(kto_201901_country_newindex['관광'] / kto_201901_country_newindex['계'] * 100, 1)
# print(kto_201901_country_newindex.head())

## 차순
# print(kto_201901_country_newindex.sort_values(by = '관광객비율(%)', ascending=False).head())
# kto_201901_country_newindex.sort_values(by = '관광객비율(%)', ascending=True).head()

## 집계
# print(kto_201901_country_newindex.pivot_table(
#   values='관광객비율(%)',
#   index = '대륙',
#   aggfunc= 'mean'
# ))

# condition = (kto_201901_country_newindex.국적 == '중국')
# print(kto_201901_country_newindex[condition])

# tourist_sum = sum(kto_201901_country_newindex['관광'])
# print(tourist_sum)

# kto_201901_country_newindex['전체비율(%)'] = \
# round(kto_201901_country_newindex['관광'] / tourist_sum * 100, 1)
# print(kto_201901_country_newindex.head())

## 국내 입국자 비율
# print(kto_201901_country_newindex.sort_values('전체비율(%)', ascending=False).head())

## 데이터 전처리 과정 함수
def create_kto_data(yy, mm):
  file_path = 'kto_{}{}.xlsx'.format(yy, mm)
  df = pd.read_excel(file_path, header=1, skipfooter=4, usecols='A:G')
  df['기준연월'] = '{}-{}'.format(yy, mm)

  ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']

  condition = (df['국적'].isin(ignore_list) == False)
  df_country = df[condition].reset_index(drop = True)

  continents =  ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['대양주']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']
  df_country['대륙'] = continents

  df_country['관광객비율(%)'] = round(df_country.관광 / df_country.계 * 100, 1)
  tourist_sum = sum(df_country['관광'])
  df_country['전체비율(%)'] = round(df_country['관광'] / tourist_sum * 100, 1)

  return(df_country)

kto_test = create_kto_data(2018, 12)
# print(kto_test.head())

# for yy in range(2010, 2020):
#   for mm in range(1, 13):
#     yymm = '{}{}'.format(yy, mm)
#     print(yymm)

mm = 1
# print(str(mm).zfill(2))
# print(str(mm).zfill(3))
# print(str(mm).zfill(4))

## 연도 만들기
df = pd.DataFrame()

# for yy in range(2010, 2020):
#   for mm in range(1, 13):
#     mm_str = str(mm).zfill(2)
#     yymm = '{}{}'.format(yy, mm_str)
#     print(yymm)

for yy in range(2010, 2020):
  for mm in range(1, 13):
    try:
      temp = create_kto_data(str(yy), str(mm).zfill(2))
      df = pd.concat([df, temp], ignore_index=True)
    except:
      pass

# print(df.head())
# df.to_excel('kto_total_3.xlsx', index = False)