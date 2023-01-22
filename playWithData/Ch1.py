## Chapter 1. Pandas

import pandas as pd
import os

## 1. Set Path
# print(os.getcwd())
os.chdir(r'C:\Users\USER\Downloads\datasalon-master\datasalon-master\01_초판\2_Start_DataAnalysis\files')
# print(os.getcwd())

## 2. Data Load
sample_1 = pd.read_excel('sample_1.xlsx',
                         header=1,
                         skipfooter=2,
                         usecols='A:C')
# print(sample_1.info)
# print(sample_1.head())
# print(sample_1.describe())
# print(sample_1.columns)

## 3. Data Handling
# print(sample_1['입국객수'])
# print(sample_1[['입국객수', '국적코드']])

sample_1['기준연월'] = '2019-11'
# print(sample_1)

# condition = (sample_1['성별'] == '남성')
# print(sample_1[condition])

# condition = (sample_1['입국객수'] >= 150000)
# print(sample_1[condition])

# condition = (sample_1['성별'] == '남성') & (sample_1['입국객수'] >= 150000)
# print(sample_1[condition])

# condition = (sample_1['국적코드'] == 'A01') \
#            |(sample_1['국적코드'] == 'A18')
# print(sample_1[condition])

# condition = (sample_1['국적코드'].isin(['A01', 'A18']))
# # print(sample_1[condition])
# print(sample_1[condition == False])

## 4. Data Merge
code_master = pd.read_excel('sample_codemaster.xlsx')
# print(code_master.info)

sample_1_code = pd.merge(
  left=sample_1,
  right=code_master,
  how='left',
  left_on='국적코드',
  right_on='국적코드'
)
# print(sample_1_code.head(5))

# sample_1_code_inner = pd.merge(
#   left = sample_1,
#   right = code_master,
#   how = 'inner',
#   left_on='국적코드',
#   right_on='국적코드'
# )
# print(sample_1_code_inner)

## 5. Data Append
sample_2 = pd.read_excel('sample_2.xlsx',
                         header=1,
                         skipfooter=2,
                         usecols='A:C')
# print(sample_2.info)
sample_2['기준연월'] = '2019-12'
sample_2_code = pd.merge(
  left = sample_2,
  right = code_master,
  how = 'left',
  left_on='국적코드',
  right_on='국적코드'
)
# print(sample_2_code.head())

# sample = sample_1_code.append(sample_2_code, ignore_index=True)
sample = pd.concat([sample_1_code, sample_2_code], axis=0)
# print(sample.info)

# sample.to_excel('sample_index_false.xlsx', index=False)

## 5. Data Pivot
# sample_pivot = sample.pivot_table(
#   values='입국객수',
#   index='국적명',
#   columns='기준연월',
#   aggfunc='mean'
# )
# print(sample_pivot)

# sample_pivot_2 = sample.pivot_table(
#   values='입국객수',
#   index='국적명',
#   aggfunc='min'   ## mean, min, max, sum, median, count, nunique(중복제거)
# )
# print(sample_pivot_2)
