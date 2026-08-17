'''1. Write a program to accept percentage from the user and display the grade according to the following
criteria:'''
print("solution of quesiotn 1")
per = int(input("what is your percentage ? : "))
if per > 90 :
    print("Congratulations your grade is A")
elif per >80 and per <= 90:
    print("your grade is B")
elif per >= 60 and per <= 80:
    print("your grade is C.")
else:
    print("your grade is D")


'''2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the
following criteria:
'''
print("solution of quesiotn 2")
cost_price = int(input("what is the cost price of bike ? : "))
if cost_price > 100000:
    print("your tax is {}".format(cost_price*0.15))
elif cost_price > 50000 and cost_price <= 100000:
    print("your tax is {}".format(cost_price*0.10))
else:
    print("your tax is {}".format(cost_price*0.05))

'''3. Accept any city from the user and display monuments ofthat city.'''
print("solution of quesiotn 3")
city_monu = {
    'Delhi':'Red Fort',
    'Agra': 'Taj Mahal',
    'Jaipur': 'Jal Mahal'
}

choose_city = input("Choose city from : Delhi , Agra , Jaipur = ")
print(" your can visit = " + city_monu[choose_city.title()])

'''4.  Check how many times a given number can be divided by 3 before it is less than or equal to 10.'''
print("solution of quesiotn 4")
def count_divisions(num):
    count = 0
    while num > 10:
        num = num / 3
        count += 1
    return count
number  = int(input("Please enter a number greater than 10 : "))
if number > 10:
    print(count_divisions(number))
else:
    print("you should enter number grater than 10.")


'''5. Why and When to Use while Loop in Python give a detailed description with example'''
# Ans => while loop is used when we know some condition is true. And it will stop if the condition becomes false.
print("solution of quesiotn 5")
# Example 
count = 0
while count < 5:
    print(count)
    count += 1


'''6. Use nested while loop to print 3 different pattern.'''
# Output:
# *
# * *
# * * *
# * * * *

rows = 4
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  
    i += 1
rows = 4
i = rows

while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

'''7. Reverse a while loop to display numbers from 10 to 1.'''
count = 10
while count > 0:
    print(count)
    count = count - 1