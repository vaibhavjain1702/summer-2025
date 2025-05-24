# list
thislist=['apple', 'banana', 'cherry']
print(thislist)

# length
print(len(thislist))  # returns the number of items in the list

# or you can do like list()
thislist = list(('apple', 'banana', 'cherry'))  # note the double round-brackets
print(thislist)

'''
4 collection data types in python
list
dictionary
tuple
set
'''

# -1 indicates the last item in the list
print(thislist[-1])  # returns 'cherry'

newlist=['lion', 'tiger', 'bear','elephant']
print(newlist[1:3])  # returns ['tiger', 'bear']
# this means it includes the first index and excludes the last index
# the same goes for negative indexing

# you can change the value of a list
newlist[1] = 'leopard'
print(newlist)  # returns ['lion', 'leopard', 'bear', 'elephant']

# insert()
newlist.insert(2, 'giraffe')  # inserts 'giraffe' at index 2
# this does not replace the value at index 2, it just inserts it
print(newlist)  # returns ['lion', 'leopard', 'giraffe', 'bear', 'elephant']

# to add an item to the end of the list, you can use append()

thislist.extend(newlist)
print(thislist)  # returns ['apple', 'banana', 'cherry', 'lion', 'leopard', 'giraffe', 'bear', 'elephant']

# with remove() you remove the first occurrence of a value

# or you can do pop() to remove an item at a specific index
thislist.pop(1)  # removes the item at index 1
print(thislist)  # returns ['apple', 'cherry', 'lion', 'leopard', 'giraffe', 'bear', 'elephant']

# normally just pop() will remove the last item in the list

del thislist[0]  # deletes the item at index 0

del thislist  # deletes the entire list

# clear() will remove all items in the list but not the list itself

anotherlist = ['apple', 'banana', 'cherry']
[print(x) for x in anotherlist]  # prints each item in the list
# you can also use a for loop to iterate through the list
for x in anotherlist:
    print(x)
# you can also use a while loop to iterate through the list
i = 0
while i < len(anotherlist):
    print(anotherlist[i])
    i += 1
# you can also use a for loop with range() to iterate through the list
for i in range(len(anotherlist)):
    print(anotherlist[i])

fruits = ['apple', 'banana', 'cherry']
newlist = []
for x in fruits:
    if 'a' in x:  # checks if 'a' is in the item
        newlist.append(x)  # adds the item to the new list
print(newlist)  # returns ['apple', 'banana']
# you can also use list comprehension to create a new list
newlist = [x for x in fruits if 'a' in x]  # same as above
print(newlist)  # returns ['apple', 'banana']

# this is the syntax for list comprehension
# newlist = [expression for item in iterable if condition==true]

# with range()
mylist=[x for x in range(10)]
print(mylist)  # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# setting it to uppercase
newlist = [x.upper() for x in fruits]
print(newlist)  # converts each item to uppercase

# you can manipulate as well like

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)  # returns ['apple', 'orange', 'cherry']
# this means if the item is 'banana', replace it with 'orange', else keep the item as it is
# it says that return the item if it is not banana and if it is banana change it to orange

# sort() sorts the list alphabetically or even numerically
huh = ['simon', 'jj', 'josh', 'ethan','harry','vik','tobi']
huh.sort()  # sorts the list in ascending order or numerically
print(huh)  # returns ['ethan', 'harry', 'jj', 'josh', 'simon', 'tobi', 'vik']
huh.sort(reverse=True)  # sorts the list in descending order
print(huh)  # returns ['vik', 'tobi', 'simon', 'josh', 'jj', 'harry', 'ethan']

def myfunc(n):
    return abs(n - 50)  # returns the absolute value of the difference between n and 50

numbers = [100, 50, 65, 82, 23]
numbers.sort(key=myfunc)  # sorts the list using the myfunc function
print(numbers)  # returns [50, 65, 82, 23, 100]

# sorting is case sensitive
# so it will sort uppercase letters before lowercase letters

# but if you want to ignore case sensitivity, you can use str.lower() method
cars = ['ford', 'BMW', 'Volvo']
cars.sort(key=str.lower)
print(cars)  # returns ['BMW', 'ford', 'Volvo']

# reverse() reverses the order of the list
avengers=['spiderman', 'iron man', 'thor', 'captain america']
avengers.reverse()  # reverses the order of the list
print(avengers)  # returns ['captain america', 'thor', 'iron man', 'spiderman']
# what is does is only reverse it not sort it

# copy() creates a copy of the list
newlist = anotherlist.copy()  # creates a copy of the list
print(newlist)  # returns ['apple', 'banana', 'cherry']
# you can also use the list() method to create a copy of the list
newlist = list(anotherlist)  # creates a copy of the list
print(newlist)  # returns ['apple', 'banana', 'cherry']

# slice operator
# you can use the slice operator to create a copy of the list
newlist = anotherlist[:]  # creates a copy of the list
print(newlist)  # returns ['apple', 'banana', 'cherry']

# joining lists

list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2  # joins the two lists

# or append
for x in list2:
    list1.append(x)  # appends each item in list2 to list1
print(list1)  # returns ['a', 'b', 'c', 'd', 'e', 'f']
# or extend
list1.extend(list2)  # extends list1 with list2
print(list1)  # returns ['a', 'b', 'c', 'd', 'e', 'f']

# functions
def my_function():
    print("Hello from a function!")
# calling the function
my_function()  # prints "Hello from a function!"

def my_function(fname):
    print(fname + " kumar")

my_function('ram')

def my_function(*kids):  # *args allows us to pass any number of arguments
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")  # prints The youngest child is Linus

def my_function(**kid):  # **kwargs allows us to pass keyword arguments
    print("His last name is " + kid["lname"])
my_function(fname="Tobias", lname="Refsnes")  # prints His last name is Refsnes

def my_function(x,/):
    print(x)
    # my_function(x=5) # TypeError: my_function() got some positional-only arguments passed as keyword arguments
my_function(5)  # prints 5

def my_function(*,x):
    print(x)
    my_function(x=5)  # prints 5
    # my_function(5)  # TypeError: my_function() takes 0 positional arguments but 1 was given

# you can also combine positional and keyword arguments

# fibonacci sequence
def fibonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
print(fibonnaci(10))  # prints 55, which is the 10th number in the fibonacci sequence
 
# classes
class MyClass:
    x=5
p1 = MyClass()  # creates an object of the class
print(p1.x)  # prints 5