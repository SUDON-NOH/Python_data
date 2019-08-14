# Python_data
Data Analysis

UTF-8 Encoding 과정에서 오류
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte

encoding = 'CP949' 로 불러온다


조건 검색

DataFrame[(DataFrame.Column's_name == x) & (DataFrame.Column's_name_2 == y)]

DataFrame[['column1', 'column2']][DataFrame['column1'] == 1].mean
DataFrame의 column1,column2를 추출하는데, DataFrame의 column1이 1인 값들만을 추출해서 평균을 냄
