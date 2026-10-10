'''Q1. Create a list in python using the followings: 2,3,4,5,6,7 with variable 'a'
Add 'mango to the above list
Also add banana, grapes & orange in the list
insert apple in the 5th position of a variable 'a'
Remove last item from the list'''
a = [2,3,4,5,6,7]
a.append("mango")
a.append("banana")
a.insert(5,"apple")
print(a)
a.pop()
print(a)

'''Q2.
L = [1,2,3,4,5,6,7]
Using the above list slice from 1:4'''
L = [1,2,3,4,5,6,7]
print(L[1:4])

'''Q3. Reverse the order of given string L = [4,5,6,8,3] Without using reverse() function.'''
L = [4,5,6,8,3]
new_list = []
while(len(L) != 0):
    item = L.pop()
    new_list.append(item)
print(new_list)

'''Q4. Use list comprehension to square the given list L=[2,4,7,3,6,8]'''
L=[2,4,7,3,6,8]
print([i**2 for i in L])
'''Q5. Create a function that takes in a tuple of integers and returns the sum of the integers.
Test the function with a tuple of your choice.'''
def tuple_sum(numbers : tuple):
    return sum(numbers)

item = (1,2,3,4,5)
print(tuple_sum(item))

'''Q6. Create two sets of your favourite fruits, and use the union() method to combine them into a 
single set.Print the resulting set to the console.'''
fruits_list1 = {"mango","banana","papaya"}
fruits_list2 = {"grapes","pineapple","Orange"}
print(fruits_list1.union(fruits_list2))

'''Q7. Create a set of random words, and use the add() method to add a new word to the set. Print the
resulting set to the console.'''
import random
word_pool = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

new_word = set(random.sample(word_pool,3))
new_word.add("oranges")
print(new_word)

'''Q8. Create a set of your favourite animals, and use the remove() method to remove one animal 
from the set. Print the resulting set to the console.'''

animals = {"dog","cat","cow","goat"}
animals.remove("dog")
print(animals)

'''Q9. favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
Use the zip() function to combine the book set and movie list into a list of tuples representing book/
movie pairs. Print the resulting list.'''

favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
book_movies_pairs = list(zip(favorite_books,favorite_movies))
print(book_movies_pairs)

'''Q10. Write a Python program to find the difference between consecutive numbers in a list.'''
deff = []
def find_diff(lst):
    for i in range(1,len(lst)):
        difference =lst[i]-lst[i-1]
        deff.append(difference)

list = [5, 9, 12, 18, 22]
find_diff(list)
print(deff)