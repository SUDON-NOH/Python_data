import pandas as pd

data_86 = pd.read_table('201806.txt')
data_87 = pd.read_table('201807.txt')
data_88 = pd.read_table('201808.txt')
data_89 = pd.read_table('201809.txt')
data_810 = pd.read_table('201810.txt')
data_811 = pd.read_table('201811.txt')
data_812 = pd.read_table('201812.txt')
data_91 = pd.read_table('201901.txt')
data_92 = pd.read_table('201902.txt')
data_93 = pd.read_table('201903.txt')
data_94 = pd.read_table('201904.txt')
data_95 = pd.read_table('201905.txt')


data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_87 = data_87.replace(to_replace = '_', value = 0, regex = True)
data_87 = data_87.astype({'pred_slng_amt':float})
print(data_87['pred_slng_amt'].max())

data_88 = data_88.replace(to_replace = '_', value = 0, regex = True)
data_88 = data_88.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())

data_86 = data_86.replace(to_replace = '_', value = 0, regex = True)
data_86 = data_86.astype({'pred_slng_amt':float})
print(data_86['pred_slng_amt'].max())




data = data_86.append(data_87)
data = data.append(data_88)
data = data.append(data_89)
data = data.append(data_810)
data = data.append(data_811)
data = data.append(data_812)
data = data.append(data_91)
data = data.append(data_92)
data = data.append(data_93)
data = data.append(data_94)
data = data.append(data_95)

table = pd.read_excel('table.xlsx', index_col= None, skiprows= 6)
table = table[['컬럼명(영문)', '컬럼명(한글)']]

x = [i for i in table['컬럼명(영문)']]
y = [i for i in table['컬럼명(한글)']]

for i, r, step in zip(x, y, range(len(x))):
    data = data.rename(columns = { i : r })
    print(step)

print(data.head())

data.to_csv('data.csv', index = False)


print(data.count())
new = pd.read_csv('data.csv')
print(new.count())
