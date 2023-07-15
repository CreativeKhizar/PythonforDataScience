import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data)

#a

missing_values = data.isnull().sum()

print("Missing values ")
print(missing_values)

df_dropped = data.dropna()

print(df_dropped)

df = data.fillna(data.mean())

#c

df['Salary_Transformed'] = df['Salary'].apply(lambda x: x + 1000)

gender_mapping = {'male': 0, 'Female': 1}

df['Gender_mapped'] = df['Gender'].map(gender_mapping)

print("apply() and map() functions")
print(df)

#b

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)

ior = Q3 - Q1

lowerbound = Q1 - 1.5 * ior
upperbound = Q3 + 1.5 * ior

outlier = df[(df['Age'] < lowerbound) | (df['Age'] > upperbound)]

filtered_df = df[(df['Age'] >= lowerbound) & (df['Age'] <= upperbound)]

print("After clearing outlier and filtered")
print(filtered_df)


#d

df['City_LowerCase'] = df['City'].str.lower()
df['City_Length'] = df['City'].str.len()

print("Vectorized Operations")
print(df)


#e

print("Graphs")
df.plot(kind='line', x='Name', y='Salary', title='Salary by Name')
df.plot(kind='bar', x='Name', y='Age', title='Age by Name')
df['Age'].plot(kind='hist', title='Age Distribution')
df['Salary'].plot(kind='density', title='Salary Density')
df.plot(kind='scatter', x='Age', y='Salary', title='Age vs Salary')

plt.show()
