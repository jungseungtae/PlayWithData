import pandas as pd

#### python pandas ####

path = 'C:/Users/USER/Downloads/datasalon-master/datasalon-master/02_개정판/2_Data_Analysis_Basic/files/'

## 1. 데이터 읽어오기
sample_1 = pd.read_excel('C:/Users/USER/Downloads/data/sample_1.xlsx',
                         header=1,
                         skipfooter=2,
                         usecols='A:C')

# print(sample_1.head(3))
# print(sample_1.tail(3))
# print(sample_1.info())
# print(sample_1.describe())

## 2. 데이터 선택
# print(sample_1['입국객수'])
# print(sample_1[['국적코드', '입국객수']])

condition = (sample_1['성별'] == '남성')
# print(condition)
# print(sample_1[condition])

condition = (sample_1['입국객수'] >= 150000)
# print(sample_1[condition])

# print(sample_1)

conditions = (sample_1['성별'] == '남성') & (sample_1['입국객수'] >= 150000)
# print(conditions)
# print(sample_1[conditions])

conditions = (sample_1['국적코드'] == 'A01') \
             | (sample_1['국적코드'] == 'A18')

# print(sample_1[conditions])

conditions = (sample_1['국적코드'].isin(['A01', 'A18']))
# print(sample_1[conditions])

conditions = (sample_1['국적코드'].isin(['A01', 'A18']))
# print(sample_1[conditions] == True)
# print(sample_1[conditions] == False)

code_master = pd.read_excel(path + 'sample_codemaster.xlsx')
# print(code_master)

# left join
sample_1_code = pd.merge(left=sample_1,
                         right=code_master,
                         how='left',
                         left_on='국적코드',
                         right_on='국적코드')
sample_1_code['기준년월'] = '2019-12'
# print(sample_1_code)

# inner join(null 값은 출력하지 않음)
sample_1_code_inner = pd.merge(left=sample_1,
                               right=code_master,
                               how='inner',
                               left_on='국적코드',
                               right_on='국적코드')
# print(sample_1_code_inner)

sample_2 = pd.read_excel(path+'sample_2.xlsx',
                         header=1,
                         skipfooter=2,
                         usecols='A:C')
sample_2['기준년월'] = '2019-12'
# print(sample_2)

sample_2_code = pd.merge(left=sample_1,
                         right=code_master,
                         how='left',
                         left_on='국적코드',
                         right_on='국적코드')
sample_2_code['기준년월'] = '2019-12'
# print(sample_2_code)

# 데이터 세로 통합
sample = pd.concat([sample_1_code, sample_2_code], axis=0, ignore_index=True)
# print(sample)

# sample.to_excel(path+'sample.xlsx')
# sample.to_excel(path+'sample_index.xlsx', index = False)

sample_pivot = sample.pivot_table(values='입국객수',
                                  index='국적명',
                                  columns='기준년월',
                                  aggfunc='mean')

# print(sample_pivot)

sample_pivot2 = sample.pivot_table(values='입국객수',
                                   index='국적명',
                                   aggfunc='max')
# print(sample_pivot2)

