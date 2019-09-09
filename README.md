# Python_data
- https://www.esrikr.com/


- Data Analysis

- UTF-8 Encoding 과정에서 오류
- UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte

- encoding = 'CP949' 로 불러온다


### 조건 검색

- DataFrame[(DataFrame[Column's_name] == x) & (DataFrame[Column's_name_2] == y)]

- DataFrame[['column1', 'column2']][DataFrame['column1'] == 1].mean
- DataFrame의 column1,column2를 추출하는데, DataFrame의 column1이 1인 값들만을 추출해서 평균을 냄



### 정렬
- data = data.sort_values(["column"], ascending=[False])
- data = data.reset_index(drop=True) 인덱스 재정렬



### boxplot 극단치 제거

- q75, q25 = np.percentile(Dataframe 행, [75, 25])
- iqr = q75 - q25
- a = q75 + (1.5 * iqr)
- b = q25 - (1.5 * iqr)


### column name 변경
- DataFrame.rename(columns={'original name1':'new name1', 'original name2':'new name2', 'original name3':'new name3'}, inplace=True)
- DataFrame.rename(columns=lambda x: x[0:3], inplace=True) # 4글자로 줄이기
- DataFrame.rename(index={0:'zero',1:'one'}, inplace=True) # index의 이름을 zero, 1로 바꾸기


### index로 merge
- data = pd.merge(data, data_1, how = 'inner', left_index = True, right_index = True)
