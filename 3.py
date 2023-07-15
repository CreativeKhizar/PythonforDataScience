# Computation on NumPy arrays using Universal Functions and Mathematical methods. 

import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

#Arithematic Operations

addition=np.add(arr1,arr2)
subtraction=np.subtract(arr1,arr2)
multiplication=np.multiply(arr1,arr2)
division=np.divide(arr1,arr2)
exponention=np.power(arr1,arr2)

# Trignonometic Operations

sin_values=np.sin(arr1)
cos_values=np.cos(arr1)
tan_values=np.tan(arr1)

# Logarithm Operations

log_base_e=np.log(arr1)
log_base10=np.log10(arr1)
log_base_2=np.log2(arr1)

# Statistical Operations

mean=np.mean(arr1)
median=np.median(arr1)
sd=np.std(arr1)
variance=np.var(arr1)

# Array Comparision

greater=np.greater(arr1,arr2)
lesser=np.less(arr1,arr2)
equal=np.equal(arr1,arr2)
sorted_arr=np.sort(arr1)

print("Addition is ",addition)
print("Subtraction is ",subtraction)
print("Mulitplication is ",multiplication)
print("Division is ",division)
print("Exponention is ",exponention)
print("Sin values ",sin_values)
print("Cos values ",cos_values)
print("Tan values ",tan_values)


print("log base e ",log_base_e)
print("log base 10 ",log_base10)
print("log base 2 ",log_base_2)

print("mean is ",mean,"\nMedian is ",median,"\nStandard Devaition is ",sd,"\nVariance is ",variance)

print("greater is ",greater,"\nlesser is ",lesser,"\nequal is ",equal,"\nsorted array is ",sorted_arr)
