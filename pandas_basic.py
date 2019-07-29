import pandas as pd

df = pd.read_csv('boston_train.csv')
print(df)


print('Shape : ', df.shape)
print('Len : ', len(df))
print('Header : ', df.columns)
print('Index : ', df.index)
print('Values : ', df.values)

print(df['CRIM'])
print(max(df['CRIM']))
print(sum(df['CRIM']))
print(sum(df['CRIM']/len(df['CRIM'])))

x = ['CRIM', 'ZN', 'INDUS']

def info(Dataframe_name, List_Series_name):
    for x in List_Series_name:
        print('Series Name : ', Dataframe_name[x].name)
        print('SUM : ', sum(Dataframe_name[x]))
        print('MAX : ', max(Dataframe_name[x]))
        print('MIN : ', min(Dataframe_name[x]))
        print('AVG : ', sum(Dataframe_name[x])/len(Dataframe_name[x]))

info(df, x)

print(df[:3])
print(df.columns[:3])
print(df['CRIM'])
print(df[df.columns[1]])
print(df[['CRIM', 'ZN', 'INDUS', 'NOX']])

print(df.loc[:5, ['CRIM', 'ZN', 'INDUS']])
print(df.iloc[:5, [0, 1, 2]])
print(df.iloc[1, [0, 1]])


x = df[['CRIM', 'ZN', 'INDUS', 'NOX']]
x.to_csv('편집본.csv', index = False)



x = pd.read_csv('boston_train.csv')

print(x)

print(x.describe())
print(x.count())
print(x.mad())
print(x.std())

y = x[x['CRIM'] > x['CRIM'].mean()]
print(y)
z = x[x['AGE'] < x['AGE'].mean()]
print(z)
b = x[x['MEDV'] < x['MEDV'].median()]
print(b)



# pandas 기본실습.py

import pandas as pd

df = pd.read_csv('boston_train.csv')

# 1.1 속성 출력: shape, index, value
print('shape:',df.shape)
print('Index :',df.index)
print('Values :', df.values)
print('-'*50)
# 1.2 행(row)으로 접근
print(df[:1])
print(df[11:16])
print(df[::3])  # 3개씩 건너뛰어 접근
print(df[::-1]) # 행을 역순으로 출력
print('-'*50)
# 1.3 열(column)로 접근
print(len(df.columns))   # 10 개 열
print(df['CRIM'])
print(df[df.columns[0]])
print(df[df.columns[9]])
print(df.columns[-1])
print(df[df.columns[-1]])
print('-'*50)

# 1.4 열의 이름을 직접 사용하여 열을 추출하여
#     Series객체 생성
sr = df['CRIM']
print(type(sr))   # Series
print(sr)

print('-'*50)

# 1.5 열의 번호를 사용하여 열을 추출하여
#     Series 객체 생성
sr = df[df.columns[0]]
print(type(sr))   # Series
print(sr)
print('-'*50)

# 1.6 열의 이름을 직접 사용하여 여러개열을
#     추출하여 DataFrame 객체 생성
r = df[['CRIM','ZN','INDUS']]
print(type(r))  # DataFrame
print('-'*50)

# 1.7 열의 번호를 사용하여 여러개 열을 추출하여
#     DataFrame 객체 생성
r2 = df[[df.columns[0],df.columns[1],df.columns[2]]]
print(type(r2))  # DataFrame
r3 = df[[df.columns[0],df.columns[1],df.columns[2]]][:10]
print('-'*50)

# 1.8 df.iloc[행번호, 열번호]를 사용하여 스칼라값(원소)을
#     접근하고 수정
print(df.loc[5,'CRIM'])
print(df.loc[:5,'CRIM'])
print(df.loc[:5,['CRIM','ZN','INDUS']])
print('-'*50)

data = df.iloc[0,0]
print(data, type(data))
print('-'*50)
data = df.iloc[2,2]
print(data, type(data))

print('-'*50)

data = df.iloc[2,[0,1,2]]
print(data, type(data))

print('-'*50)

data = df.iloc[:3,[0,1,2]]
print(data, type(data))

print('-'*50)

df.iloc[3,0] = 9.99999  # 0.15876 -> 9.99999 스칼라값 변경
print(df.iloc[:5,0])


# 1.9 수정된 DataFrame을 새로운 csv 파일로 저장
df.to_csv('boston_train_new.csv',index=False)