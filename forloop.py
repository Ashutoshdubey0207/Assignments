#Q1. Explain with an example each when to use a for loop and a while loop.
# for loop = 'Repeat a loop for a known number of times'
# while loop = 'keep doing this while condition is true'

# for loop example

# printing table
# def table(n):
#     for i in range(1,11):
#         print(i*n)
#     return 
# table(23)
#Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.
# sum = 0;
# for i in range(101):
#     sum = sum + i
# print(sum)

# using while loop
# new_sum = 0
# i = 1
# while i < 11:
#     new_sum = new_sum + i
#     i = i +1
# print(new_sum)

"""Q3. Create a python program to compute the electricity bill for a household.
The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input.
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250."""

# Electricity_units = int(input("Enter the number of electricity units consumed in a month: "));
# if Electricity_units <= 100:
#     bill = Electricity_units*4.5
# elif Electricity_units > 100 and Electricity_units <= 200:
#     bill = 100*4.5 + (Electricity_units-100)*6
# elif Electricity_units > 200 and Electricity_units <= 300:
#     bill = 100*4.5 + 100*6 + (Electricity_units - 300) * 10
# else:
#     bill = 100*4.5 + 100*6 + 100*10 + (Electricity_units-300)*20

# print(bill)

'''Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.'''

list1 = []
for i in range(1,101):
    if i**3%4 == 0 or i**3%5 == 0:
        list1.append(i)
print(list1)
# lambda function
numbers = list(range(1,101))
result = list(filter(lambda i:i**3%4 == 0 or i**3%5 == 0 , numbers))
print(result)

"""Q5. Write a program to filter count vowels in the below-given string.
string = "I want to become a data scientist"""
count = 0
s = "I want to become a data scientist"
V = ['a','e','i','o','u','A','E','I','O','U']
for i in s:
    for j in V:
        if i == j:
            count = count + 1
print(count)
