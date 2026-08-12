from functools import reduce
'''Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]'''
print("QUESTION NO 1 OUTPUT")
Players = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_players = sorted(Players, key= lambda x : x[1])
print(sorted_players)

'''Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
print("QUESTION NO 2 OUTPUT")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_number = list(map(lambda x : x**2 , list1))
print(squared_number)

'''Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')'''

print("QUESTION NO 3 OUTPUT")
givern_string = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(map(lambda x: str(x),givern_string)))

'''Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.'''
print("QUESTION NO 4 OUTPUT")
list2 = [x for x in range(1,26)]
print(reduce(lambda x,y : x*y ,list2 ))

'''Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]'''

print("QUESTION NO 5 OUTPUT")

list3 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
print(list(filter(lambda x : x %3 == 0 or x % 2 == 0, list3)))

'''Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']'''

print("QUESTION NO 6 OUTPUT")
def is_palindrome(str):
    str = str.lower()
    Answer = True
    n = len(str)
    c = 0
    while(c <= n /2):
        if str[c] != str[n-1]:
            Answer = False
            break
        c = c + 1
        n = n - 1
    return Answer
list5 = ['python', 'php', 'aba', 'radar', 'level']
print(list(filter(lambda x : is_palindrome(x) == True, list5)))
