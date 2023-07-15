# Import    a  CSV    file  and   perform    various   Statistical  and   Comparison     operations    on  rows/columns.

import pandas as pd

df=pd.read_csv("data1.csv")

print(df)


min=df.min()
max=df.max()

mean=df.mean()
std=df.std()
var=df.var()
median=df.median()

mode=df.mode().iloc[0]

count=df.count()

c_s=df.cumsum()
c_p=df.cumprod()

print("Min value is \n",min)
print("Max value is \n",max)
print("Mean is ",mean)
print("Standard Devaition is \n",std)

print("Variance is \n",var)
print("Medain is \n",median)

print("Mode is \n",mode)

print("Cummulative Sum is \n",c_s)

print("Cummulative Product is \n",c_p)
