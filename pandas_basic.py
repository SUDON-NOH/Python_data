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

