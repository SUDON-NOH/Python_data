# Python_data
- https://www.esrikr.com/  # 지리정보시스템
- https://www.esrikr.com/products/arcgis-desktop/arcgis-pro/
- http://datakorea.datastore.or.kr/ # 데이터코리아 - 각종 
- Data Analysis

- UTF-8 Encoding 과정에서 오류
- UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte

- encoding = 'CP949' 로 불러온다


### 검색 기능
- df['columns].str.contains("str") columns 에 str을 포함한 행 찾기
- df.isin([str, num]) str, num을 포함한 행 찾기


### 조건 검색

- DataFrame[(DataFrame[Column's_name] == x) & (DataFrame[Column's_name_2] == y)]

- DataFrame[['column1', 'column2']][DataFrame['column1'] == 1].mean
- DataFrame의 column1,column2를 추출하는데, DataFrame의 column1이 1인 값들만을 추출해서 평균을 냄



### 정렬
- data = data.sort_values(["column"], ascending=[False])
- data = data.reset_index(drop=True) 인덱스 재정렬



### boxplot 극단치 제거

- q75, q25 = np.percentile(Dataframe 열 or 행, [75, 25])
- iqr = q75 - q25
- a = q75 + (1.5 * iqr)
- b = q25 - (1.5 * iqr)  
https://goodtogreate.tistory.com/entry/%EC%9D%B4%EC%83%81%EC%B9%98-%EC%A0%9C%EA%B1%B0-Boxplot-%ED%95%B4%EC%84%9D%EC%9D%84-%ED%86%B5%ED%95%9C

### column name 변경
- DataFrame.rename(columns={'original name1':'new name1', 'original name2':'new name2', 'original name3':'new name3'}, inplace=True)
- DataFrame.rename(columns=lambda x: x[0:3], inplace=True) # 4글자로 줄이기
- DataFrame.rename(index={0:'zero',1:'one'}, inplace=True) # index의 이름을 zero, 1로 바꾸기


### index로 merge
- data = pd.merge(data, data_1, how = 'inner', left_index = True, right_index = True)


### 깃허브에서 주피터노트북 로드가 되지 않을 때
nbviewer의 url에서 주피터 노트북 파일이 올려져 있는 깃허브 url을 합친다.

https://nbviewer.jupyter.org

깃허브 사이트의 url

https://github.com/SUDON-NOH/Python_data/blob/master/matplotlib_basic.ipynb

- 결과

https://nbviewer.jupyter.org/github/SUDON-NOH/Python_data/blob/master/matplotlib_basic.ipynb

