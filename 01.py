import pandas as pd
import numpy as np
import xlrd
import xlsxwriter

workbook = xlrd.open_workbook('PD-1.xlsx')

# Sheet names
x = workbook.sheet_names()

# 행마다
for sheet in workbook.sheets():
    print('시트이름', sheet.name)
    for i in range(sheet.nrows):
        row = sheet.row(i)
        print('행','---',i,'---', row)
        for j in row:
            print(j, j.value)

z = workbook.sheets()
print(z)

# 이름으로 시트 불러오기
worksheet_RawData = workbook.sheet_by_name('Raw Data')
print(worksheet_RawData)

# 인덱스로 시트 불러오기
worksheet_index = workbook.sheet_by_index(2)
print(worksheet_index)

# 시트이름 지정하여 저장하기
a = [[1, 2, 3] , [4, 5, 6], [7, 8, 9]]
b = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
x = pd.DataFrame(a)
y = pd.DataFrame(b)
print(x)

# pip install openpyxl
x.to_excel('test_1.xlsx', sheet_name = 'test1')

# 1. 엑셀 파일 열기 w/ExcelWriter
# pip install XlsxWriter
writer = pd.ExcelWriter('test_2.xlsx', engine = 'xlsxwriter')

# 2. 시트별 데이터 추가하기
x.to_excel(writer, sheet_name = '1')
y.to_excel(writer, sheet_name = '2')

writer.save()

# 엑셀 시트 데이터 불러오기

p = pd.read_excel('PD-1.xlsx', sheet_name='Raw Data', index = False)
print(p)
q = pd.read_excel('PD-1.xlsx', sheet_name=0)

p = p.drop(index=1, inplace = True)
print(p)