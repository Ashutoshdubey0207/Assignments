from functools import reduce
'''Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.'''

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
new_list = []
def func(demo_list):

    for i in demo_list:
        if(type(i) == int):
            new_list.append(i)
        elif (type(i) == tuple):
            for x in i:
                if type(x) == int:
                    new_list.append(x)
        elif type(i) == set:
            for x in i:
                if type(x) == int:
                    new_list.append(x)
        elif type(i) == dict:
            for x in i.keys():
                if type(x) == int:
                    new_list.append(x)
            for x in i:
                if type(i[x]) == int:
                    new_list.append(i[x])
                elif type(i[x]) == list:
                    for item in i[x]:
                        if type(item) == int:
                            new_list.append(item)
                elif type(i[x]) == tuple:
                    for item in i[x]:
                        if type(item) == int:
                            new_list.append(item)

        elif type(i) == list:
            for x in i:
                if type(x) == int:
                    new_list.append(x)
    return new_list

print(func(list1))
print(reduce(lambda a,b: a*b, new_list))
'''Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.
Input Sentence: I want to become a Data Scientist.
Encrypt the above input sentence using the program you just created.
Note: Convert the given input sentence into lowercase before encrypting. The final output should be
lowercase.'''
strone = input("enter a string = ")
string = strone.lower()
new_str = ''
for i in string:
    if i == ' ':
        i = '$'
        new_str += i
    else:
        char = ord(i)-96
        new_str += chr(123-char)
print(new_str)