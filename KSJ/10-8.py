import numpy as np

print("10-8. 20203035 김석준")

print("1) 배열 a:")

a = np.random.rand(3,3,3)

print(a)

print("")

max_a = np.max(a)
print("2) a의 원소들 중 최댓값 : ", max_a)
print("")
print("3) a의 원소들 중 최댓값의 위치 : ",np.argmax(a))
