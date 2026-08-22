import pandas as pd

'''Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.'''

data = pd.Series([4, 8, 15, 16, 23, 42])
# print(data)

'''Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
variable print it.'''

var_list = ['ashu','naman','sourabh',10,10.11,True]
pd_list = pd.Series(var_list)
# print(pd_list)


'''Q3. Create a Pandas DataFrame that contains the following data:
Then, print the DataFrame.'''
data = {
    'name':['Alice','Bob','Claire'],
    'age' :[25,30,27],
    'gender': ['male','male','female']
}
pd_df = pd.DataFrame(data)
# print(pd_df)

'''Q4. What is DataFrame in pandas and how is it different from pandas.series? Explain with an example.'''
#a DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). 
'''
| Feature    | Series              | DataFrame           |
| ---------- | ------------------- | ------------------- |
| Dimension  | 1D                  | 2D                  |
| Structure  | Single column       | Multiple columns    |
| Similar to | Single Excel column | Excel table         |
| Example    | `[10, 20, 30]`      | `Name, Age, Salary` |
'''


'''Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
you give an example of when you might use one of these functions?'''
'''
Common Data Manipulation Functions------

dropna(): Removes rows or columns with missing values.
fillna(): Replaces missing or null values with a specified scalar or method.
sort_values(): Reorders rows based on values in one or more columns.
groupby(): Splits data into groups to perform aggregate calculations.
apply(): Executes a custom function along a specific axis (row-wise or column-wise).
merge(): Combines two data structures using database-style joins on common columns'''




'''Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
Ans---
In pandas, both a DataFrame and a Panel are mutable in both size and values, while a Series is mutable in its values but 
immutable in its size (you cannot change its length once created, though you can modify existing elements).'''


'''Q7. Create a DataFrame using multiple Series. Explain with an example.'''

names = pd.Series(["Ashu",'Naman',"Anna"])
age = pd.Series([26,25,24])
marks = pd.Series([90,89,78])

df7 = pd.DataFrame({
    "Names" : names,
    'Age' : age,
    "Marks": marks
})
print(df7)