'''Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25'''
# Ans => def keyword is used to create function
def odd_return(num):
    for i in range(num+1):
        if i%2 != 0:
            print(i)
    return i
odd_return(25) 
'''Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use.'''

# Ans = * args = to handle any number of arguments
# *kwargs to handge any number of key:value pair arguments

# Example of args
def sum_all(*args):
    return sum(args)
print('The sum of all the numbers is' ,sum_all(1,2,3,34,4,6))

# Example of kwargs
def show_keys(**kwargs):
    return kwargs.keys()

'''Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].'''
# Ans => An iterator is an object that contains a countable number of values.
# method used to initialise the iterator = iter()
list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
myiter = iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.'''
# Ans => Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# yield keyword = yield keyword is used to create generator functions. 
# Unlike return, which exits the function, yield returns one value at a time and pauses the function. 
# When called again, the function resumes execution from where it was paused.
print("question 4 solution")
def fun(num):
    count = 0
    while count <= num:
        yield count
        count = count+1

x = fun(5)
for i in x:
    print(i)

'''Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.'''
# def prime_number_generator():
#     for i in range(2,1000):

'''Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.'''
print(" question no 6 solution")
def fib(num): 
    a = 0
    b = 1
    count = 0
    while(count < num):
        print(a)
        a,b=b,a+b
        count = count + 1

fib(10)


'''Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']'''

str = "pwskills"
list = []
for i in str:
    list.append(i)
print(list)

'''Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.'''

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

print(is_palindrome('Naman'))

'''Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.'''
list1 = [ x for x in range(100)]
list2 = [x for x in list1 if x%2 != 0]
print(list2)