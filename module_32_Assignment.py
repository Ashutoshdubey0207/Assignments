import pandas as pd

'''Q1. List any five functions of the pandas library with execution.'''

data = {
    'Product' : ['Laptop','Pendrive','Monitor','Mouse','Keyboard'],
    'Price': [1200,25,300,26,75],
    'Stock':[15,50,8,90,30]
}

df = pd.DataFrame(data) # to create data
df.head() # to print first five records
df.tail() # to print last five records
df.describe() # to get the description of table based on numerica value like min,max std,var    
df.value_counts() # to get the count of every item in the df if the are duplicate or not
df.groupby('Product')['Stock'].sum() # to group items and get their sum
df.drop_duplicates() # to remove duplicate data from the df

'''Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
DataFrame with a new index that starts from 1 and increments by 2 for each row.'''
df1 = pd.DataFrame({
        'A':[1,2,3,4,5],
        'B':[6,7,8,9,0],
        'C':[6,5,4,7,8]
})
# print(df1)
def re_index(df1):
    end_point = len(df1)*2
    df1.index = range(1,end_point,2)
    return df1
# print(re_index(df1))

'''Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console.'''

df2 = pd.DataFrame({
        'Values':[1,2,3,4,5],
        'Product':[6,7,8,9,0],
        'quantity':[6,5,4,7,8]
})

sum = df2['Values'][0:3].sum() # iteratinig first three values and getting their sum
# print(sum) # values sum 1+2+3 = 6

'''Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
'Word_Count' that contains the number of words in each row of the 'Text' column.'''

df3 = pd.DataFrame({
    'Text': ['I am Ashu','Love my mother very much','My',"Inda"]
})
df3['Word_Count'] = df3['Text'].apply(lambda x :  len(x.split()))
# print(df3)

'''Q5. How are DataFrame.size() and DataFrame.shape() different?'''
df5 = pd.DataFrame({
        'Values':[1,2,3,4,5],
        'Product':[6,7,8,9,0],
        'quantity':[6,5,4,7,8]
})

# print(df5.size) # size return the number of elements in the data frame
# print(df.shape) # shapre return the shape of Data frame in terms of rows and columns (no fo rows,no of columns)


'''Q6. Which function of pandas do we use to read an excel file?'''
# pd.read_excel for reading exel file
# pd.read_csv for reading csv file
# pd.read_xml read xml document
# pd.read_html  read html files

'''Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
addresses in the format 'username@domain.com'. Write a Python function that creates a new column
'Username' in df that contains only the username part of each email address.'''
df7 = pd.DataFrame({
    'emails': ["rahul.sharma@gmail.com","priya.patel@gmail.com","amit.kumar@gmail.com","sneha_reddy@gmail.com","vikram.singh@gmail.com","anjali.joshi@gmail.com","rohit_verma@gmail.com","pooja.gupta@gmail.com","sandeep.nair@gmail.com","divya_choudhary@gmail.com"]
})
def sep_user(x):
    username = ""
    for i in x:
        if(i != '@'):
            username = username + i
        else:
            return username

df7['user_name'] = df7['emails'].apply(lambda x : sep_user(x)  )
# print(df7)

'''Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
function should return a new DataFrame that contains only the selected rows.

For example, if df contains the following values:

   A   B   C

0  3   5   1

1  8   2   7

2  6   9   4

3  2   3   5

4  9   1   2

Your function should select the following rows:  
   A   B   C

1  8   2   7

4  9   1   2

The function should return a new DataFrame that contains only the selected rows.'''

df8 = pd.DataFrame({
    'A' :  [3,8,6,2,9],
    'B' : [5,2,9,3,1],
    'C' : [1,7,4,5,2]
})

new_df = df8[(df8['A']>5) & (df8['B']< 10)] # the real condition
# print(new_df)

'''Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
median, and standard deviation of the values in the 'Values' column.'''

df9 = pd.DataFrame({
    'Values':[1,2,3,4,5,6,1,1,2,2,2,2,2],
})

# print(df9.mean())
# print(df9.median())
# print(df9.std())
# print(df9.mode())

'''Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
should include the current day.'''

df10 = pd.DataFrame({
    'Sales': [
        1200, 1500, 1800, 1100, 2100,
        2500, 1900, 1700, 2300, 2800,
        1600, 2000, 2200, 3000, 2700,
        1400, 1850, 2400, 3200, 2900
    ],
    'Date': [
        '2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05',
        '2026-01-06', '2026-01-07', '2026-01-08', '2026-01-09', '2026-01-10',
        '2026-01-11', '2026-01-12', '2026-01-13', '2026-01-14', '2026-01-15',
        '2026-01-16', '2026-01-17', '2026-01-18', '2026-01-19', '2026-01-20'
    ]
})

df10['MovingAverage'] = df10['Sales'].rolling(window=7,min_periods=1).mean() # minperiod = to get average of first 6 data in place of  NaN
# print(df10)

'''Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
Monday, Tuesday) corresponding to each date in the 'Date' column.

For example, if df contains the following values:

         Date

0  2023-01-01

1  2023-01-02

2  2023-01-03

3  2023-01-04

4  2023-01-05

Your function should create the following DataFrame:


         Date    Weekday

0  2023-01-01    Sunday

1  2023-01-02     Monday

2  2023-01-03    Tuesday

3  2023-01-04    Wednesday

4  2023-01-05    Thursday

The function should return the modified DataFrame.'''
df11 = pd.DataFrame({'Date': [
        '2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05',
        '2026-01-06', '2026-01-07', '2026-01-08', '2026-01-09', '2026-01-10',
        '2026-01-11', '2026-01-12', '2026-03-13', '2026-01-14', '2026-01-15',
        '2026-01-16', '2026-01-17', '2026-02-18', '2026-01-19', '2026-01-20'
]})
# to convert dataframe into date time object
df11['Date'] = pd.to_datetime(df11['Date'])
df11['Weekday'] = df11['Date'].dt.day_name()
df11['Month_name'] = df11['Date'].dt.month_name()
df11['Month'] = df11['Date'].dt.month
# printing the values
# print(df11)

'''Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
function to select all rows where the date is between '2026-01-01' and '2026-01-31'.'''

df11 = pd.DataFrame({'Date': [
        '2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05',
        '2026-01-06', '2026-05-07', '2026-10-08', '2026-01-09', '2026-01-10',
        '2026-01-11', '2026-08-12', '2026-03-13', '2026-01-14', '2026-01-15',
        '2026-01-16', '2026-09-17', '2026-02-18', '2026-01-19', '2026-01-20'
]})
date_range = pd.date_range(start='2026-01-01',end='2026-01-31')
df11['Date'] = pd.to_datetime(df11['Date'])
def finddate(x):
    date_range = pd.date_range(start='2026-01-01',end='2026-01-31')
    for i in date_range:
        if i != x:
           continue
        else:
            return x
# to convert date and time formate
df_ans = pd.DataFrame(df11['Date'].apply(finddate))
# print(df_ans)

'''Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
be imported?'''
# Ans = import Pandas (you need to import pandas)


























