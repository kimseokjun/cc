import numpy as np

print("10-7. 20203035 김석준")

n_arr = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]])

print("1)",n_arr)
print("")
print("2)")
print("첫 원소 : ",n_arr[0,0])
print("마지막 원소 : ", n_arr[-1,-1])
print("")
print("3)")
print(n_arr[0:2,0:5])
print("")
print("4)")
print(n_arr[2:5,0:5])
print("")
print("5)")
print(n_arr[0:5,0:5:2])
print("")
print("6)")
print(n_arr[0:5:2,0:5:2])
print("")
print("7)")
slice_n = n_arr[0:2,0:5]
print(slice_n.reshape(5,2))
