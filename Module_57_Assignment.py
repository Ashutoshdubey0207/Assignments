import pandas as pd

'''Q1. Pearson correlation coefficient is a measure of the linear relationship between two variables. Suppose
you have collected data on the amount of time students spend studying for an exam and their final exam
scores. Calculate the Pearson correlation coefficient between these two variables and interpret the result.'''

data = {
     "Student": [
        "Amit", "Amit", "Amit", "Amit",
        "Priya", "Priya", "Priya", "Priya",
        "Rahul", "Rahul", "Rahul", "Rahul",
        "Neha", "Neha", "Neha", "Neha",
        "Rohan", "Rohan", "Rohan", "Rohan"
    ],

    "Subject": [
        "Physics", "Chemistry", "Maths", "Biology",
        "Physics", "Chemistry", "Maths", "Biology",
        "Physics", "Chemistry", "Maths", "Biology",
        "Physics", "Chemistry", "Maths", "Biology",
        "Physics", "Chemistry", "Maths", "Biology"
    ],

    "Study_Hours": [
        3, 4, 5, 2,
        5, 6, 6, 4,
        2, 3, 4, 3,
        4, 5, 5, 6,
        6, 5, 7, 5
    ],

    "Movie_Time_Hours": [
        3, 3, 2, 4,
        2, 1, 1, 2,
        5, 4, 4, 5,
        2, 2, 1, 1,
        1, 2, 1, 2
    ],

    "Final_Exam_Score": [
        58, 67, 74, 52,
        78, 85, 88, 72,
        45, 55, 63, 58,
        70, 76, 81, 86,
        88, 82, 94, 80
    ]
    
}

df = pd.DataFrame(data)
# print(df.corr(method='pearson',numeric_only=True))

'''Q2. Spearman's rank correlation is a measure of the monotonic relationship between two variables.
Suppose you have collected data on the amount of sleep individuals get each night and their overall job
satisfaction level on a scale of 1 to 10. Calculate the Spearman's rank correlation between these two
variables and interpret the result.'''
data = {

     "Sleep_Hours": [
        5, 7, 6, 8, 7,
        4, 6, 8, 5, 7,
        9, 6, 8, 5, 7
    ],

    "Screen_Time_Hours": [
        8, 5, 7, 4, 5,
        9, 7, 3, 8, 5,
        2, 7, 4, 9, 6
    ],

    "Job_Performance": [
        5, 8, 6, 9, 8,
        3, 6, 10, 5, 8,
        10, 6, 9, 4, 8
    ]
}
df2 = pd.DataFrame(data)
# print(df2.corr(method="spearman"))

'''Q3. Suppose you are conducting a study to examine the relationship between the number of hours of
exercise per week and body mass index (BMI) in a sample of adults. You collected data on both variables
for 50 participants. Calculate the Pearson correlation coefficient and the Spearman's rank correlation
between these two variables and compare the results.'''
data = {
    "Exercise_Hours_Per_Week": [
        1, 2, 3, 4, 5, 2, 6, 7, 3, 4,
        5, 1, 8, 6, 2, 4, 7, 3, 5, 6,
        2, 9, 4, 5, 7, 3, 6, 8, 2, 4,
        5, 7, 3, 6, 9, 1, 4, 8, 5, 2,
        6, 7, 3, 5, 8, 4, 2, 6, 7, 5
    ],
    "BMI": [
        28.5, 27.8, 26.9, 25.4, 24.8, 29.2, 23.5, 22.8, 27.1, 26.3,
        24.9, 30.1, 21.9, 23.7, 28.7, 26.1, 22.5, 27.4, 25.2, 24.1,
        28.9, 21.5, 26.7, 25.5, 23.1, 27.8, 24.3, 22.4, 29.5, 26.8,
        25.1, 23.6, 27.2, 24.5, 21.8, 30.2, 26.4, 22.1, 25.8, 28.1,
        24.0, 23.2, 27.6, 25.0, 22.7, 26.0, 29.0, 24.7, 23.8, 25.6
    ]
}

df = pd.DataFrame(data)
# print(df.corr(method='pearson'))
# print(df.corr(method='spearman'))

'''Q4. A researcher is interested in examining the relationship between the number of hours individuals
spend watching television per day and their level of physical activity. The researcher collected data on
both variables from a sample of 50 participants. Calculate the Pearson correlation coefficient between
these two variables.'''

data = {
    "TV_Hours_Per_Day": [
        1, 2, 3, 4, 5, 2, 6, 7, 3, 4,
        5, 1, 8, 6, 2, 4, 7, 3, 5, 6,
        2, 9, 4, 5, 7, 3, 6, 8, 2, 4,
        5, 7, 3, 6, 9, 1, 4, 8, 5, 2,
        6, 7, 3, 5, 8, 4, 2, 6, 7, 5
    ],
    "Physical_Activity_Hours_Per_Week": [
        8, 7, 6, 5, 3, 7, 2, 1, 6, 5,
        4, 9, 1, 3, 7, 5, 2, 6, 4, 3,
        8, 1, 5, 4, 2, 6, 3, 1, 8, 5,
        4, 2, 6, 3, 1, 9, 5, 1, 4, 7,
        3, 2, 6, 4, 1, 5, 7, 3, 2, 4
    ]
}

df = pd.DataFrame(data)
# print(df.corr(method='pearson'))
# print(df.corr(method='spearman'))

'''Q6. A company is interested in examining the relationship between the number of sales calls made per day
and the number of sales made per week. The company collected data on both variables from a sample of
30 sales representatives. Calculate the Pearson correlation coefficient between these two variables.'''
data = {
    "Sales_Calls_Per_Day": [
        10, 15, 20, 25, 30,
        12, 18, 22, 28, 35,
        14, 20, 25, 30, 40,
        16, 22, 27, 32, 45
    ],
    "Sales_Per_Week": [
        5, 7, 9, 11, 14,
        6, 8, 10, 13, 16,
        7, 9, 12, 15, 19,
        8, 11, 14, 17, 22
    ]
}

df = pd.DataFrame(data)
print(df.corr(method='pearson'))