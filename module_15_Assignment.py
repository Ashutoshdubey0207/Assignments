import re
'''Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.
Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.
'''
password = input("Enter your password = ")
pattern = r'[^a-zA-Z0-9\s]'
count_upper = 0
count_lower = 0
count_num = 0
if len(password) == 10:
    count  = re.findall(pattern,password)
    if len(count) >= 3:
        
        for i in password:
            if i >= '0' and i <= '9':
                count_num = count_num + 1
            if i >= 'a' and i <= 'z':
                count_lower = count_lower + 1
            if i >= 'A' and i <= 'Z':
                count_upper = count_upper + 1
                
    if count_num >= 1 and count_lower >= 2 and count_upper >= 2:
        print("valid password")
    else:
        print("invalid password")
else:
    print("Invalid Password")

'''Q2. Solve the below-given questions using at least one of the following:
1. Lambda function
2. Filter function
3. Map function
4. List ComprehensioI

'''
# Check if the string starts with a particular letter.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x[0] for x in fruits ]
print(newlist)

# Check if the string is numeric.
new_list = ['hellow1', 'hello2','shiv@123','Ashu']
Ans = [x.isalnum() for x in new_list ]
print(Ans)

# Sort a list of tuples having fruit names and their quantity. 
fruit_quatity = [("mango",99),("orange",80), ("grapes", 1000)]
sorted_list = sorted(fruit_quatity,key=lambda x : x[1])
print(sorted_list)

# Find the squares of numbers from 1 to 10.
print(list(map(lambda x: x**2,[x for x in range(1,11)])))

# Find the cube root of numbers from 1 to 10.
print(list(map(lambda x: x**3,[x for x in range(1,11)])))

# Check if a given number is even.
num = 90
if num % 2 == 0:
    print("Even")
else:
    print("False")
# Filter odd numbers from the given list.
nums =  [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2 != 0 , nums)))

# Sort a list of integers into positive and negative integers lists.
new_nums = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

print(sorted(list(filter(lambda x:x >= 0 ,new_nums))))
print(sorted(list(filter(lambda x:x < 0 ,new_nums))))