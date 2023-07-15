# Create Pandas Series and DataFrame from various inputs.

import pandas as pd

# 1. Create Pandas Series from various inputs

data_list=[10,20,30,40,50]

series_from_list=pd.Series(data_list)

print("Series from list is \n",series_from_list)

data_dict={'A':10,'B':20,'C':30,'D':40,'E':50}

series_from_dict=pd.Series(data_dict)

print("Series from dictionary is ")
print(series_from_dict)

scalar=6.2

series_from_scalar=pd.Series(scalar,index=[1,2,3,4,5])

print("Series from scalar")

print(series_from_scalar)
#---------------------------------------------------------------------------------------------------------


# 1. Create Pandas Series from various inputs


data_nested_list=[[1,"John",25],[2,'Jane',30],[3,'Sam',35]]
cols=['Id','Name','Age']

df_from_nested_list=pd.DataFrame(data_nested_list,columns=cols)


print("DataFrame from nested list is ")
print(df_from_nested_list)


data_dict_of_list={'IO':[1,2,3],'Name':['John','Jane','Sam'],'Age':[25,28,30]}

df_from_dict_of_list=pd.DataFrame(data_dict_of_list)

print("DataFrame form dictionary of lists")

print(df_from_dict_of_list)



