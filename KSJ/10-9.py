import numpy as np

print("10-9. 20203035 김석준")

a = np.arange(0,32).reshape(4,4,2)

print("a: ",a)

b = a.flatten()

print("b : ",b)

print("10번째 원소 : ", b[10-1])
print("20번째 원소 : ", b[20-1])
