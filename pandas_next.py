import pandas as pd

# Q.7
sales1 = {'판매월':['1월','2월','3월','4월'] ,
          '제품A':[100, 150, 200, 130] ,
          '제품B':[90, 110, 140, 170]}
sales2 = {'판매월':['1월','2월','3월','4월'] ,
          '제품C':[112, 141, 203, 134] ,
          '제품D':[90, 110, 140, 170]}

x1 = pd.DataFrame(sales1)
x2 = pd.DataFrame(sales2)

print(x1)
print(x2)

y = pd.merge(x1, x2, how = 'inner', on = '판매월')
print(y)


# Q.8

df0 = {'key':['A', 'B', 'C'],
       'left':[1, 2, 3]}
df00 = {'key':['A', 'B', 'D'],
       'right':[4, 5, 6]}
df1 = pd.DataFrame(df0)
df2 = pd.DataFrame(df00)


# (1)
df_i = pd.merge(df1, df2, how = 'inner', on = 'key')
print('inner:', '\n', df_i)

# (2)
df_o = pd.merge(df1, df2, how = 'outer')
print('outer','\n', df_o)

# (3)
df_l = pd.merge(df1, df2, how = 'left')
print('left:','\n', df_l)

# (4)
df_r = pd.merge(df1, df2, how = 'right')
print('right:','\n',df_r)


# Q.5

df = pd.read_csv('sunspots.csv')
# 결측치의 열마다 존재하는 개수
print(pd.isnull(df).sum())
# NaN 값을 모두 0으로 변경
df2 = df.fillna(0)
print(pd.isnull(df2).sum())

df2.to_csv('sunspot_new.csv', index = False)

# Q.6

date = df['Date']
df3 = pd.to_datetime(date)
