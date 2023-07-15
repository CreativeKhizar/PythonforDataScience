import pandas as pd

df=pd.read_csv("data.csv")
print(df)

#a
first10=df.head(10)
last10=df.tail(10)

print("First 10 records")
print(first10)

print("Last 10 records")
print(last10)

#b
shape=df.shape
index=df.index
columns=df.columns

print("Shape ",shape)
print("Index ",index)
print("Columns ",columns)

#c

print("Selecting Records")
print(df[df['Salary']>90000])

print("Selecting Colums")
print(df['Salary'])


print("Deleting Columns")

print(df.drop(['Salary'],axis=1))


#d

df['Rank']=df['Salary'].rank(ascending=False)

print("Adding Rank")
sdf=df.sort_values('Salary',ascending=True)

print(sdf)

#e

print("Mean ",df['Salary'].mean())

print("max ",df['Salary'].max())

print("min ",df['Salary'].min())

#f

print(df['Gender'].value_counts())

print(df['Salary'].unique())

#g

nd=df.rename(columns={"Salary":"Income"})

print("After Renaming")

print(nd)
