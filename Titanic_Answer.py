# titanic실습과제.py

# https://kaggle-kr.tistory.com/17

import pandas as pd
import seaborn as sb
titanic = sb.load_dataset('titanic')


# 1.1
titanic.to_csv('titanic_new.csv',index=False)
print(titanic.mean())

# 1.2
titanic_new = titanic.fillna(titanic.mean())
titanic_new.to_csv('titanic_new_no_nan.csv',index=False)

# 1.3

print('survived:',titanic['survived'][titanic['survived']
                                      == 1].count())
print('not survived:',titanic['survived'][titanic['survived']
                                          ==0].count())
# 1.4
print(titanic.pivot_table("survived", "class",aggfunc='mean'))

# 1.5
print(titanic.pivot_table("survived", "sex",aggfunc='mean'))

# 1.6
print(titanic.pivot_table("survived", "age",aggfunc='mean'))

# 1.7
print(titanic.pivot_table("survived", "sibsp",aggfunc='mean'))

# 1.8
print(titanic.pivot_table("fare","pclass",aggfunc='mean'))

# 1.9
new_df = titanic.drop(['deck'], axis = 1)
print(new_df)

# 1.10
print('-'*50)   # age를  3등급으로 나누어 등급의 성별 생존률
titanic["age_class"] = pd.qcut(titanic.age, 3,
                              labels = ["young", "midlle", "old"])
print(titanic.pivot_table('survived', index=['sex',
            'age_class'], aggfunc='mean', columns='pclass'))
print('-'*50)



# titanic실습과제.py

# https://kaggle-kr.tistory.com/17

import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

# 한글 출력을 위한 설정
import matplotlib
matplotlib.rcParams['font.family']="Malgun Gothic"
matplotlib.rcParams['axes.unicode_minus'] = False

titanic = sb.load_dataset('titanic')


# 한글 출력을 위한 설정
import matplotlib
matplotlib.rcParams['font.family']="Malgun Gothic"
matplotlib.rcParams['axes.unicode_minus'] = False

titanic = sb.load_dataset('titanic')

# 2.1 생존자와 사망자의 수를 pie 차트로 그리시오(matplotlib)

survived = titanic['survived'][titanic['survived'] == 1].count()

not_survived = titanic['survived'][titanic['survived'] ==0].count()
data = [survived,not_survived]
pie_label = ['생존자','사망자']
exp = [0.05,0.05]
plt.figure(figsize=(5,5))
plt.pie(data,labels = pie_label,explode = exp,
        autopct ='%.1f%%',shadow = True)
plt.title('2.1 Titanic Survived - Pie Chart')
plt.show()


# 2.2 등급별 티켓 비용(fare)의 평균을  barplot으로 그리시오(seaborn)
sb.barplot('pclass','fare', data=titanic)
plt.title('2.2 Titanic pclass/fare - barplot')
plt.show()

# 2.3 성(Sex)별 생존자와 사망자의 수를 countplot 으로 그리시오(seaborn)
sb.countplot(data=titanic,x='sex',hue='survived')
plt.title('2.3 Titanic Survived/sex - countplot')
plt.show()


# 2.4  상관 관계 heatmap을 출력하시요 (seaborn)
plt.figure(figsize=(10, 10))
sb.heatmap(titanic.corr(), linewidths=0.01, square=True,
            annot=True, cmap=plt.cm.viridis, linecolor="white")
plt.title('2.4 Titanic Correlation between features')
plt.show()

# 2.5 나이(age) 분포도(distplot)를 그리시오 (seaborn)
#       결측치는 평균값으로 수정
titanic = titanic.fillna(titanic.mean())
sb.distplot(titanic['age'])
plt.title('2.5 Titanic age - distplot')
plt.show()


# 2.6 객실의 등급(pclass)별 'age'의 분포를 boxplot으로 그리시오(seaborn)
titanic = sb.load_dataset('titanic')

sb.boxplot(data=titanic, x='pclass',y='age')

df = titanic.groupby('pclass')
med = df.agg([np.median])
r = med['age']
t0 = r['median'].values[0]
t1 = r['median'].values[1]
t2 = r['median'].values[2]
plt.text(0,t0, round(t0,2))
plt.text(1,t1, round(t1,2))
plt.text(2,t2, round(t2,2))

plt.title('2.6 Titanic pclass/age - boxplot')
plt.show()