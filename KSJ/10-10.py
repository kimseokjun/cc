import numpy as np

print("10-10. 20203035 김석준")

print("x1 : ")
x1 = [i for i in range(100)]
print(x1)
print("")

print("x2 : ")
x2 = [i+ np.random.randint(1,10) for i in range(100)]
print(x2)
print("")


print("x3 : ")
x3 = [i +np.random.randint(1,50) for i in range(100)]
print(x3)
print("")


print("x4 : ")
x4 = [np.random.randint(1,100) for i in range(100)]
print(x4)
print("")


print(np.corrcoef([x1,x2,x3,x4]))
