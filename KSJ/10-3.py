import numpy as np

print("10-3. 20203035 김석준")

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
print("대상자들의 키: {}".format(heights))
np_heights = np.array(heights)
print("키가 1.80 이상인 사람 : {}".format(np_heights[np_heights>=1.80]))

weights = [86, 74, 59, 95, 80, 68]
print("대상자들의 몸무게 : {}".format(weights))
np_weights = np.array(weights)
print("몸무게가 85 이상인이 사람 : {}".format(np_weights[np_weights>=85]))


bmi = np_weights/(np_heights**2)
print("대상자들의 BMI : {}".format(bmi))  
print("BMI가 27 이상인 사람 : {}".format(bmi[bmi>=27]))
