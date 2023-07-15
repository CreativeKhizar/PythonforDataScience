# Write  a   program   to   compute   summary   statistics   such   as   mean,   median,   mode,   standard  deviation and variance of the given different types of data.

import statistics as st

lst=[1,2,3,4,5,6,7,8,9]

mean=st.mean(lst)
median=st.median(lst)
mode=st.mode(lst)
std=st.stdev(lst)
var=st.variance(lst)

print("Mean is ",mean)
print("Mode is ",mode)
print("Median is ",median)
print("Standard Deviation is ",std)
print("Variance is ",var)
