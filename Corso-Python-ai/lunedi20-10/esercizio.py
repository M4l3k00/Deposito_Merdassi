import numpy as np


array = np.arange(0,50) + np.random.randint(49, 102, size=50)
print(array)
print(array.dtype)


array = array.astype(np.float64)
print(array.dtype)
print(array.shape)



print(array[0:10])
print(array[-7:])
print(array[10:20])
print(array[0:-1:4])

array[10:15] = 999
print(array)



inidici = [0, 3, 7, 12, 25, 33, 48]

print(array[inidici])


maschera = array%2 ==0
print("======================")
print(array[maschera])


media = array.mean()

maschera1 = array>media
array_maggiori = array[maschera1]
print("================")
print(array_maggiori)
print("================")

print(array)




