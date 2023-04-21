#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Creating an 1D array

arr=np.array([1,2,3,4,5])

print("Elements in the Array are ",arr)


# In[3]:


# Creating a 1D List

lst=[1,2,3,4,5]

print("Elements in the List are ",lst)


# In[4]:


# Creating a tuple

tp=(1,2,3,4,5)

print("Elements in the Tuple are ",tp)


# In[5]:


# 1D array

lst=[1,2,3,4,5]

arr=np.array(lst)

print("One Dimensional Array")
print(lst)


# In[6]:


# 2D array

lst=[[1,2,3],[4,5,6],[7,8,9]]

arr=np.array(lst)

print("Two Dimensional Array")
print(arr)


# In[7]:


# 3D Array

lst=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]

arr=np.array(lst)

print("Three Dimensional Array")
print(arr)


# In[8]:


# Type of Array

lst=[[1,2,3],[4,5,6],[7,8,9]]

arr=np.array(lst)

print(type(arr))


# In[22]:


# Shape of an Array

lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

arr=np.array(lst)

print("The Dimensions of the Numpy Array is ",arr.shape)


# In[10]:


# Fill a 2d Array with 0 values


# In[11]:


# Adding a number to the multi dimensional array

lst=[[1,2,3],[4,5,6]]

arr=np.array(lst)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]+=2
        
print(arr)


# In[12]:


# Multiplying a number to all elements in multi dimensional array

lst=[[1,2,3],[4,5,6]]

arr=np.array(lst)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]*=2
        
print(arr)


# In[14]:


# Divide a number to all elements in multi dimensional array

lst=[[1,2,3],[4,5,6]]

arr=np.array(lst,dtype='float')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]=arr[i][j]/2
        
print(arr)


# In[21]:


# Transpose of a matrix

lst=[[1,2,3],[4,5,6],[7,8,9]]

arr=np.array(lst)

print("Before Transpose")

print(arr)

print("After Transpose")


for i in range(0,len(arr)):
    for j in range(i+1):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

print(arr)


# In[23]:


# Filling the elements in the array with zeroes

lst=[[1,2,3],[4,5,6]]

arr=np.array(lst)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]=0
        
print(arr)


# In[ ]:




