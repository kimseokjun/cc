import numpy as np

print("10-1. 20203035 김석준")

a = np.array(range(1,11))
b = np.array(range(10,101,10))
plus = a+b
minus = a-b
multy = a*b
div = a/b

print("a = {}".format(a),end=' ')
print("b = {}".format(b))
print("a+b= {}".format(plus))
print("a-b= {}".format(minus))
print("a*b= {}".format(multy))
print("a/b= {}".format(div))
