# numpy
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)  # prints the array [1 2 3 4 5]
print(type(arr))  # prints <class 'numpy.ndarray'>, indicating it's a NumPy array
print(np.__version__)  # prints the version of NumPy installed

arr = np.array((1,2,3,4,5))
print(arr)  # prints the array [1 2 3 4 5]

# dimensions in arrays
# 0-D array
arr = np.array(42)
print(arr)  # prints 42
# 1-D array
# the normal one
arr = np.array([1, 2, 3, 4, 5])
# 2-D array
# array that has 1-D arrays as its elements
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)  # prints [[1 2 3] [4 5 6]]
# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)  # prints [[[ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12]]]

# checking number of dimensions
a= np.array(42)
b= np.array([1, 2, 3, 4, 5])
c= np.array([[1, 2, 3], [4, 5, 6]])
d= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a.ndim)  # prints 0, indicating a 0-D array
print(b.ndim)  # prints 1, indicating a 1-D array
print(c.ndim)  # prints 2, indicating a 2-D array
print(d.ndim)  # prints 3, indicating a 3-D array

arr = np.array([1,2,3,4,5], ndmin=5)  # creates a 5-D array
print(arr)  # prints the array with 5 dimensions
print('number of dimensions:', arr.ndim)  # prints the number of dimensions, which is 5

# accessing elements in 2d arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element in 1st row:', arr[0, 1])  # prints 2
# row comes the first, then column
print('3rd element in 2nd row:', arr[1, 2])  # prints 8
print('2nd row, 3rd column:', arr[1][2])  # prints 8, same as above
print('2nd row:', arr[1])  # prints the entire 2nd row [6 7 8 9 10]
print('2nd column:', arr[:, 1])  # prints the entire 2nd column [2 7]

# same for 3d arrays
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print('1st element in 1st row of 1st array:', arr[0, 0, 0])  # prints 1
print('2nd element in 2nd row of 1st array:', arr[0, 1, 1])  # prints 5
print('1st row of 2nd array:', arr[1, 0])  # prints [7 8 9]
print('2nd column of 1st array:', arr[0, :, 1])  # prints [2 5]
print('2nd column of 2nd array:', arr[1, :, 1])  # prints [8 11]

# negative indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element in 1st row:', arr[0, -1])  # prints 5

# slicing arrays

arr = np.array([1, 2, 3, 4, 5])
print('Elements from index 1 to 3:', arr[1:4])  # prints [2 3 4]
# it considers the start index and goes up to but not including the end index

# negative slicing
print(arr[-3:-1])  # prints [3 4]

# step in slicing
print(arr[0:5:2])  # prints [1 3 5], takes every 2nd element from index 0 to 4

# slicing 2d array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Elements from 1st row, index 1 to 3:', arr[0, 1:4])  # prints [2 3 4]
print('from both arrays , return index 2:',arr[0:2 , 2])

# shape of arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('Shape of the array:', arr.shape)  # prints (2, 3), indicating 2 rows and 3 columns

arr=np.array([1,2,3,4], ndmin=5)  # creates a 5-D array
print('shape of array:', arr.shape)  # prints (1, 1, 1, 1, 4), indicating 5 dimensions with the last dimension having 4 elements

# reshaping arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, 2)  # reshapes the array to 3 rows and 2 columns
print('Reshaped array:\n', reshaped_arr)  # prints the reshaped array

# we cant reshape an array to a shape that doesn't match the number of elements
# for example, trying to reshape a 2x3 array to 3x2 is fine, but reshaping a 2x3 array to 2x4 will raise an error
arr = np.array([[1, 2, 3], [4, 5, 6]])  
try:
    reshaped_arr = arr.reshape(2, 4)  # this will raise an error because there are only 6 elements in the original array
except ValueError as e:
    print(e)  # prints "cannot reshape array of size 6 into shape (2,4)"

# return copy or view of array
arr = np.array([1, 2, 3, 4, 5])
copy_of_arr = arr.copy()  # returns a copy of the array
view_of_arr = arr.view()  # returns a view of the array
print('Original array:', arr)  # prints [1 2 3 4 5]
print('Copy of array:', copy_of_arr)  # prints [1 2 3 4 5]
print('View of array:', view_of_arr)  # prints [1 2 3 4 5]
# modifying the original array will not affect the copy, but will affect the view
arr[0] = 10
print('Modified original array:', arr)  # prints [10 2 3 4 5]
print('Copy of array after modifying original:', copy_of_arr)  # prints [1 2 3 4 5]
print('View of array after modifying original:', view_of_arr)  # prints [10 2 3 4 5]

print(arr.reshape(5,1).base)  # prints the base of the reshaped array, which is the original array

# unknown dimension
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, -1)  # -1 means "infer the size of this dimension"
print('Reshaped array with unknown dimension:\n', reshaped_arr)  # prints the reshaped array
# this will automatically adjust the number of columns based on the number of elements
# in the original array, so it will reshape to 3 rows and 2 columns
# if we had a 1D array, it would reshape to 3 rows and 1 column

# flattening arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr=arr.reshape(-1)  # flattens the array to a 1D array
print('Flattened array:', newarr)  # prints [1 2 3 4 5 6]
# you can also use the flatten() method to flatten an array
flattened_arr = arr.flatten()  # flattens the array to a 1D array
print('Flattened array using flatten():', flattened_arr)  # prints [1 2 3 4 5 6]
# you can also use ravel() to flatten an array
raveled_arr = arr.ravel()  # flattens the array to a 1D array
print('Flattened array using ravel():', raveled_arr)  # prints [1 2 3 4 5 6]
# the difference between flatten() and ravel() is that flatten() returns a copy of the array,
# while ravel() returns a view of the array if possible
# so modifying the original array will not affect the flattened array created using flatten(),
# but will affect the flattened array created using ravel()

# what does reshape(6) do?
# it reshapes the array to a 1D array with 6 elements
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(6)  # reshapes the array to a 1D array with 6 elements
print('Reshaped array to 1D with 6 elements:', reshaped_arr)  # prints [1 2 3 4 5 6]

# sum of 1d array
arr = np.array([1, 2, 3, 4, 5])
sum_of_elements = np.sum(arr)  # calculates the sum of all elements in the array
print('Sum of elements:', sum_of_elements)  # prints 15

# matrix multiplication
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = np.dot(arr1, arr2)  # performs matrix multiplication
# explain the dot function
print('Result of matrix multiplication:\n', result)  # prints [[19 22] [43 50]]
# the dot function performs matrix multiplication, which is different from element-wise multiplication
# it multiplies the rows of the first matrix with the columns of the second matrix
# and sums the products to get the resulting matrix
# here it is like 1*5 + 2*7 = 19, 1*6 + 2*8 = 22, 3*5 + 4*7 = 43, 3*6 + 4*8 = 50