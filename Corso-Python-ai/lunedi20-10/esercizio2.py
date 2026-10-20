import numpy as np

arr = np.linspace(0,1,12)
print(arr)
print("=================")

reshap_arr = arr.reshape(3,4)
print(reshap_arr)
print("=================")

random_arr = np.random.rand(3,4)
print(random_arr)
print("=================")

print(reshap_arr.sum())
print(random_arr.sum())

