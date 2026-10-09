'''Q1. Write a Python program that defines a function called "add_numbers" that takes two arguments (i.e.,
numbers) and returns their sum. Within the function, add the two numbers together and return the result
using the return statement. Call the function with the values 5 and 6, and print out the returned result.
This will result in the addition of 5 and 6, with the output of the program being the sum of these two
numbers.'''

def add_numbers(num1,num2):
    return num1 + num2

num1 = 5
num2 = 6
print(f"The Sum of {num1} and {num2} is ",add_numbers(num1,num2))

'''Q2. Write a Python program that calculates the square root of a given number using a built-in function.
Specifically, the program should take an integer or float input from the user, calculate its square root
using the 'sqrt()' function from the 'math' module, and print out the result to the user. As an example,
calculate the square root of the number 625 using this program, which should output the value of 25.'''
import math
num = int(input("Enter your number to get square root : "))
print(f"The square root of the number is {num} : ",math.sqrt(num))

'''Q3.Write a program that prints all prime numbers between 0 to 50.'''
import math
def isprime(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
checkprime = [i for i in range(1,51) if isprime(i)]
print(checkprime)

'''Q4.How can we swap the values of three variables (let's say a, b, and c) without using a fourth variable?
For example, if we have a=5, b=8, and c=9, how can we obtain a=9, b=5, and c=8? The challenge is to
perform this operation without using an additional variable to store any of the values during the
swapping process.'''

a ,b,c = 5,8,9
a,b,c = c,a,b
print(a,b,c)
'''Q5. Can you write a program that determines the nature of a given number (in this case, 87) as being
positive, negative, or zero? The program should be designed to take the number as input and perform the
necessary calculations to determine if the number is positive (i.e., greater than zero), negative (i.e., less
than zero), or zero (i.e., equal to zero). The output of the program should indicate which of these three
categories the given number falls into.'''

num = int(input("Enter your number : "))
if num == 0:
    print("Equal to zero")
elif  num < 0:
    print("number is Negative")
elif num > 0 :
    print("number is Positive")
else:
    print("Not a nubmer")


'''Q6. How can you create a program that determines whether a given number (in this case, 98) is even or
odd? The program should be designed to take the number as input and perform the necessary
calculations to determine whether it is divisible by two. If the number is divisible by two without leaving a
remainder, it is an even number, and if there is a remainder, it is an odd number. The output of the
program should indicate whether the given number is even or odd.'''
def iseven(num):
    return num%2==0

print(iseven(14))


'''Q7.Write a program for sum of digits.the digits are 76543 and the output should be 25.'''
def sum_of_digits(num):
    sum = 0
    if num<10:
        return num
    while(num > 0 ):
        rem = num % 10
        sum += rem
        num = num // 10
    return sum
print(sum_of_digits(245))

'''Q8.Write a program for reversing the given number 5436 and the output should be 6345.'''

def reversed(num):
    reverse = 0
    while(num>0):
        rem = num%10
        num = num // 10
        reverse = reverse*10 + rem
    return reverse

print(reversed(123))

'''Q9.Write a program to check if a given number 371 is an Armstrong number?'''
def isArmstrong(num):
    copy = num
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + (rem**3)
        num = num // 10
    if copy == sum:
        return True
    return False

print(isArmstrong(153))

'''Q10.Write a program the given year is 1996, a leap year.'''

def leap_year(year):
    # Divisible by 4 AND (Not divisible by 100 OR divisible by 400)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(leap_year(1900))
        