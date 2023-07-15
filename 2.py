# Manipulation of NumPy arrays- Indexing, Slicing, Reshaping, Joining and Splitting.

import numpy as np

lst=[0,1,2,3,4,5]

arr=np.array(lst)

# Accessing elements in the Array by indexing

for i in range(6):
    print("Element at index ",i," is ",arr[i])

# Slicing in Numpy Array

print(arr[1:5])


# Reshaping of Numpy Array

new_arr=arr.reshape(2,3)

print(new_arr)

# Joining of two arrays

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

new_arr=np.concatenate((arr1,arr2))

print(new_arr)

# Splitting arrays

newarrlist=np.array_split(new_arr,3)

print(newarrlist);
