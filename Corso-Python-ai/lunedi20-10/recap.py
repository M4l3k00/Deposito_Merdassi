import numpy as n


arr = n.array([1,2,3,4,5,6]) #array

#arr2 = n.array2d([[1,2,3],[4,5,6]]) #array2d

#una collezione di dati viene convertita in un array
#ndarry
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.argmax())


array = n.arange(10)
print(array)

#reshape
reshape_arr = array.reshape(2,5)
print(reshape_arr)



#indexing
print(arr[0])
#slicing
print(arr[1:4])
#boolean indexing
print(arr[arr>2])


arr = n.linspace(0,5,10)
print(arr)


random_arr = n.random.rand(3,3)

print(random_arr)