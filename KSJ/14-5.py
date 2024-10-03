import numpy as np
from sklearn import linear_model # scikit-learn 모듈을 가져온다
regr = linear_model.LinearRegression()
com_p = {
    'name' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
    'horse power' : [130, 250, 190, 300, 210, 220, 170],
    'weight' : [1900, 2600, 2200, 2900, 2400, 2300, 2100],
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
    }

X = []
# X = [[130,1900], [250,2600], [190,2200],[300,2900],[210,2400],[220,2300],[170,2100]]

for idx in range(7):
    X.append([com_p['horse power'][idx], com_p['weight'][idx]])

y = com_p['efficiency']
# y = [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
regr.fit(X, y)

coef = regr.coef_ # 직선의 기울기
intercept = regr.intercept_ # 직선의 절편
score = regr.score(X, y) # 학습된 직선이 데이터를 얼마나 잘 따르나

print("계수 :", coef)
print("절편 :", intercept)
print("예측 점수 :", score)

result = regr.predict([[270, 2500]])
print('270 마력 2500kg 자동차의 예상 연비 : {0:.2f}'.format(result[0]), 'km/l')
