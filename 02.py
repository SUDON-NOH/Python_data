import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

from sklearn.preprocessing import MinMaxScaler

import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'

data = pd.read_csv('data.csv')

print(data[(data['사업체id'] == 5951704)])

# 필요한 column 들만 추출
data1 = data[['기준년월', '공정위업종중분류명칭', '공정위업종중분류코드','사업체명칭', '사업체id', '건물번호', '시군구명칭', '행정동명칭', '행정동코드', '사업체수',
            '버스정류장 거리', '지하철역 거리', '도로까지의거리', '버스정류장수', '지하철역수', '야간상주인구_합계', '예상매출액']]
data1 = data1.replace(to_replace = '_', value = 0, regex = True)

print(data.columns)

# # MinMaxScaler
# scaler = MinMaxScaler()
# data_new = data[['버스정류장 거리', '지하철역 거리', '도로까지의거리', '예상매출액']]
# data_new[['버스정류장 거리', '지하철역 거리', '도로까지의거리', '예상매출액']] = \
#     scaler.fit_transform(data_new[['버스정류장 거리', '지하철역 거리', '도로까지의거리', '예상매출액']])
#
# data_mms = data

# # 기준년월만 추출
# data_new = data_mms[(data_mms['기준년월'] == 201806)]
# data_x = data_new[['버스정류장 거리', '지하철역 거리', '도로까지의거리', '지하철역수', '예상매출액']]

# ====================================================================================================

# 같은 건물 , 같은 달, 다른 업종의 매출액이 같은 경우
data_a = data1.sort_values(['건물번호', '기준년월'])

# 1)
print(data1.head(data1['건물번호']))

data_x = data1[(data1['사업체id'] == 5936306)]
data_x1 = data1[(data1['사업체id'] == 6016638)]



# 2)
data_y = data1[(data1['건물번호'] == '3014010100100520005027006')]


data_b = data_a.astype({'예상매출액':float})
print(data_a.dtypes)

data_sort = data_b.sort_values(['예상매출액'], ascending = False)

x = data_a[(data_a['사업체id'] == 1531554)]



# 연매출이 '_' 로 된 데이터
print(data.count())     # 166,926

data_m = data[(data['예상매출액'] == '_')]
print(data_m.count())   # 11,292


# 연매출이 '_' 로 된 데이터를 제외한 데이터

data_n = data[(data['예상매출액'] != '_')]

# 연매출이 5000 이상인 데이터

data_z = data_n.astype({'예상매출액':float})
data_f = data_z[(data_z['예상매출액'] >= 5000)]
print(data_f.count())   # 6453

data_t = data_z[(data_z['예상매출액'] < 800)]
print(data_t.count())


plt.boxplot(data_t['예상매출액'], labels = ['예상매출액'])
plt.show()


