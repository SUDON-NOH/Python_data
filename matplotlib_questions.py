import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# [ matplotlib  실습]
#
# 1. Boston 데이터 시각화 실습 문제
#
#    1.1 boston_train.csv 파일을 읽어와서 log plot을 출력하세요
#        'CRIM'과 'MEDV' 컬럼의 데이터를 사용한다
#
#    1.2 boston_train.csv 파일을 읽어와서 scatter plot을 출력하세요
#        'CRIM'과 'MEDV','ZN' 컬럼의 데이터를 사용한다
#
#    1.3 boston_train.csv 파일을 읽어와서 plot 및 scatter plot에 범례와 주석을
#       함께 출력하세요
#        'CRIM'과 'MEDV','ZN' 컬럼의 데이터를 사용한다
#
#    1.4 boston_train.csv파일을 읽어와서 3차원 plot을 출력하세요
#        'CRIM'과 'MEDV','ZN' 컬럼의 데이터를 사용한다
#
#    <Pandas 플로팅>
#    1.5 boston_train.csv파일을 읽어와서 pandas를 사용해서
#     'MEDV'의 지연 plot을 출력하세요
#
#    1.6 boston_train.csv 파일을 읽어와서 pandas를 사용해서
#     'MEDV'의 자기 상관 plot을 출력하세요
#
#    1.7 boston_train.csv 파일을 읽어와서 pandas를 사용해서
#        전체 컬럼의 box plot과 'TAX' 컬럼의 box plot을 출력하세요


x = pd.read_csv('boston_train.csv')


MEDV = x['MEDV'].values
CRIM = x['CRIM'].values

# plt.plot(MEDV, np.log(CRIM))


# ============================Q1================================
x1 = np.polyfit(CRIM, np.log(MEDV), deg = 1)
print('Poly', x1)
print('Poly', x1[0])
print('Poly', x1[1])

# plt.plot(CRIM, np.log(MEDV),'o')
# plt.show()
# plt.semilogy(CRIM, MEDV, 'o')
plt.semilogy(CRIM, np.exp(np.polyval(x1, CRIM)), label = 'Semilogy')


# x = pd.read_csv('boston_train.csv')
#
# x = x.groupby('CRIM').agg(np.mean)
#
#
# CRIM = x.index.values
# MEDV = x['MEDV'].values
#
# # plt.plot(MEDV, np.log(CRIM))
#
# x1 = np.polyfit(CRIM, np.log(CRIM), deg = 1)
# print('Poly', x1)
# print('Poly', x1[0])
# print('Poly', x1[1])
#
# plt.semilogy(CRIM, MEDV, 'o')
# plt.semilogy(CRIM, np.exp(np.polyval(x1, CRIM)))
# plt.show()

# ============================Q2================================

df = pd.read_csv('boston_train.csv')
df = df.groupby('CRIM').agg(np.mean)

MEDV = df['MEDV'].values
CRIME = df.index.values
ZN = df['ZN'].values
CRIME_log = np.log(CRIME)

plt.scatter(CRIME, MEDV, c = 20 * CRIME,
            s = 50+20 * ZN/ZN.max(), alpha = 0.5, label = 'Scatter Plot')


# ============================Q3================================
crim_start = df.index.values.min()
# print(crim_start) # 0.00632
y_ann = np.log(df.at[crim_start, 'MEDV'])
# print(y_ann) # 3.1780538303479458
ann_str = 'Crime'
plt.annotate(ann_str, xy = (34.811, 10.0897),
             arrowprops = dict(arrowstyle = '->'),
             xytext = (0 , +30),
             textcoords = 'offset points')
plt.legend(loc = 'upper right')

plt.grid(True)
plt.xlabel('Crime')
plt.ylabel('Medv')
plt.title('Boston Housing : Crime Medv')
plt.show()


# DataFrame.corr()
# 상관관계(Correlation)
# -1.0과 -0.7 사이이면, 강한 음적 선형관계
# -0.7과 -0.3 사이이면, 뚜렷한 음적 선형 관계
# -0.3과 -0.1 사이이면, 약한 음적 선형관계
# -0.1과 0.1 사이이면, 거의 무시될 수 잇는 선형관계
# 0.1과 0.3 사이이면, 약한 양적 선형관계
# 0.3과 0.7 사이이면 뚜렷한 양적 선형관계
# 0.7과 1.0 사이이면 강한 양적 선형관계


#=================================Q4======================

df = pd.read_csv('boston_train.csv')


MEDV = df['MEDV'].values
CRIME = df['CRIM'].values
ZN = df['ZN'].values


fig = plt.figure()
print(fig)
ax = Axes3D(fig)

X = CRIME
Y =  np.where(df['MEDV'].values > 0,
             np.log(df['MEDV'].values), 0)
Z = np.where(df['ZN'].values > 0,
             np.log(df['ZN'].values), 0)
# result = np.where(conditions, a, b)
# result is a if contions == True else b


X,Y = np.meshgrid(X, Y)
Z,_ = np.meshgrid(Z, 0) # _ 는 아무런 변수가 없다. Z만 쓰면 meshgrid의 결과가 모두 Z에 튜플로 형성된다.
# print(X.shape) # (37, 37) 1차원인 데이터를 3D 데이터를 만들기 위해 2차원으로 변경해서 생성

# Z = Z.reshape(1, Z.shape[0]) # 1차원인 데이터를 2차원으로 변경


ax.plot_surface(X, Y, Z)
ax.set_xlabel('CRIME')
ax.set_ylabel('MEDV')
ax.set_zlabel('ZN')
ax.set_title("CRIME & MEDV & ZN")
plt.show()


# matplotlib_실습문제.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('boston_train.csv')



#=======================================================================================================
# 교수님 답

# # 1.1번 로그플롯
# crim = df['CRIM'].values
# medv = df['MEDV'].values
#
# poly = np.polyfit(crim,np.log(medv),deg=1) # 학습
# print(type(poly))
# print('Poly',poly[0]) # W, 기울기
# print('Poly',poly[1]) # b, y절편
# # plt.plot(crim,np.log(medv),'o')
# # plt.show()
# plt.semilogy(crim,medv,'o')
# plt.semilogy(crim,np.exp(np.polyval(poly,crim)))
# plt.title('1.1 Boston crim/zn medv scatter plot')
#
# plt.show()
# print(df.corr())
#
#
# # 1.2번 분산 플롯
# crim = df['CRIM'].values
# medv = df['MEDV'].values
# zn = df['ZN'].values
#
# # c: color, s:size, apha:투명도
# plt.scatter(crim,medv,c = 200*crim,
#             s =20 + 200*zn/zn.max(),
#             alpha = 0.5)  # 버블차트
#
# plt.grid(True)
# plt.xlabel('crim')
# plt.ylabel('medv')
# plt.title('1.2 Boston crim/zn medv scatter plot')
# plt.show()
#
# # 1.3 번
# crim = df['CRIM'].values
# medv = df['MEDV'].values
#
# poly = np.polyfit(crim,np.log(medv),deg=1) # 학습
# plt.plot(crim, np.polyval(poly, crim), label='Fit')
#
# medv_start = int(medv.mean())
# print(medv_start )
# y_ann = np.log(df.at[medv_start, 'MEDV']) - 0.1
# print(y_ann)
# ann_str = "Medv Crime\n %d" % medv_start
# plt.annotate(ann_str, xy=(medv_start, y_ann),
#              arrowprops=dict(arrowstyle="->"),
#              xytext=(-30, +70), textcoords='offset points')
#
# cnt_log = np.log(medv)
# plt.scatter(crim, cnt_log, c= 200 * crim,
#             s=20 + 200 * zn/zn.max(),
#             alpha=0.5, label="Scatter Plot")
# plt.legend(loc='upper right')
# plt.grid()
# plt.xlabel("Crime")
# plt.ylabel("Medv", fontsize=16)
# plt.title("1.3 Boston Housing : Crime Medv")
# plt.show()
#
# # 1.4번
# from mpl_toolkits.mplot3d.axes3d import Axes3D
#
# fig = plt.figure()
# ax = Axes3D(fig)
# X = df['CRIM'].values
#
# Y = np.where(df['MEDV'].values>0, np.log(df['MEDV'].values), 0)
# X, Y = np.meshgrid(X, Y)
#
# Z = np.where(df['ZN'].values>0, np.log(df['ZN'].values), 0)
# # Z =Z.reshape(1,Z.shape[0])
# Z,_ =np.meshgrid(Z,0)
#
# ax.plot_surface(X, Y, Z)
# ax.set_xlabel('CRIME')
# ax.set_ylabel('MEDV')
# ax.set_zlabel('ZN')
# ax.set_title("1.4 Boston Housing : Crime/ZN  Medv")
# plt.show()
#
# #  1.5번
# from pandas.plotting import lag_plot
#
# lag_plot(np.log(df['MEDV']))
# plt.title('1.5 Boston lag_plot')
# plt.show()
#
# #  1.6번
# from pandas.plotting import autocorrelation_plot
# autocorrelation_plot(np.log(df['MEDV']))
#
# plt.title('1.6 Boston autocorrelation_plot')
# plt.show()
#
# # 1.7번
#
# df.plot.box()
# plt.title('1.7.1 Boston Box plot')
# plt.show()
#
# df['TAX'].plot.box()
# plt.boxplot(df['TAX'],labels=['TAX'])
# plt.text(1, df['TAX'].median(), df['TAX'].median())
#
# plt.title('1.7.2 Boston TAX Box plot')
# plt.show()
#
# plt.boxplot(df['TAX'],labels=['TAX'])
# plt.text(1, df['TAX'].median(), df['TAX'].median())
# plt.title('1.7.3 Boston TAX Box plot')
# plt.show()