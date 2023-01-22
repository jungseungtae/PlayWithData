import pandas as pd

file_path = 'C:/Users/USER/Downloads/doit_pandas-master/doit_pandas-master/data/'

df = pd.read_csv(file_path + 'gapminder.tsv', sep = '\t')

# print(df.head())

# print(df.info())

country_df = df['country']

# print(country_df)

## loc로 행 데이터 추출하기
## 인덱스로 추출하는 방법이기 때문에 인덱스가 아닌 -1 같은 수로는 추출 불가
# print(df.loc[0 : 5])

# print(df.loc[99])

number_of_rows = df.shape[0]
# print(number_of_rows)
last_row_index = number_of_rows - 1
# print(last_row_index)

# print(df.loc[last_row_index])

# print(df.tail(n = 1))

# print(df.loc[[0, 99, 999]]

## iloc 행 데이터 추출하기
## 데이터의 순서를 기준으로 행을 추출하는 것

# print(df.iloc[1])
# print(df.iloc[-1])

## 컬럼 추출
## 컬럼의 이름으로 추출 가능
subset = df.loc[:, ['year', 'pop']]
# print(subset.head())

## 컬럼의 순서로 추출 가능
subset = df.iloc[:, [2,4,-1]]
# print(subset.head())

small_range = list(range(5))
# print(small_range)

subset = df.iloc[:, small_range]
# print(subset.head())

## 슬라이싱과 range

## 컬럼 0~2까지 추출
subset = df.iloc[:, :3]
# print(subset.head())

subset = df.iloc[:, 0:6:2]
# print(subset.head())

## 데이터를 0, 99, 999번째 행을 가져오고 컬럼은 0, 3, 5번째 컬럼을 가져옴
# print(df.iloc[[0, 99, 999], [0, 3, 5]])

## 행 0, 99, 999를 가져오고 컬럼은 뒤의 컬럼만 가져옴
# print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# print(df.loc[10:13,['country', 'lifeExp', 'gdpPercap']])

# print(df.head(n = 10))

## 연도별 평균
# print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
# print(grouped_year_df)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
# print(type(grouped_year_df_lifeExp))

mean_lifeExp_df_lifeExp = grouped_year_df_lifeExp.mean()
# print(mean_lifeExp_df_lifeExp)

## 연도와 지역을 그룹으로 데이터 출력
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# print(multi_group_var)

# print(df.groupby('continent')['country'].nunique())

import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
# print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()