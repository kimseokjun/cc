import numpy as np

print("10-2. 20203035 김석준")
 
a = np.array([0,1,2,3,4,5,6,7,8,9])
print("실습 1: array_a = {}".format(a))
b = np.array(range(10))
print("실습 2: array_b = {}".format(b))
c = np.array(range(0,9,2))
print("실습 3: array_c = {}".format(c))
print("실습 4:")
print("array_c의 shape : {}".format(c.shape))
print("array_c의 ndim : {}".format(c.ndim))
print("array_c의 dtpye : {}".format(c.dtype))
print("array_c의 size : {}".format(c.size))
print("array_c의 itemsize : {}".format(c.itemsize))

