import numpy as np
list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)
'''Q1. Is there any difference in the data type of variables list_ and array_list? If there is then
write a code to print the data types of both the variables.'''
# yes they are different, <class 'list'> and <class 'numpy.ndarray'>
# print(type(list_))
# print(type(array_list))

'''Q2. Write a code to print the data type of each and every element of both the variables list_ and
arra_list.'''
# print(type(list_))
# print(type(array_list))

'''Q3. Considering the following changes in the variable, array_list:
array_list = np.array(object = list_, dtype = int)
Will there be any difference in the data type of the elements present in both the variables, list_ and
arra_list? If so then print the data types of each and every element present in both the variables, list_
and arra_list.'''


'''Q4. Write a code to find the following characteristics of variable, num_array:
(i) shape
(ii) size '''
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)
# print(num_array.size)
# print(num_array.shape)

'''Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
creation function.
[Hint: The size of the array will be 9 and the shape will be (3,3).]'''

array = np.zeros(dtype=int,shape=(3,3))
# print(array)

'''Q6. Create an identity matrix of shape (5,5) using numpy functions?
[Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]'''

id_mat = np.eye(5,5)
# print(id_mat)
