# for printing like print()
print("Hello World")
if 5>2:
    print("Five is greater than two!")
x = 5
y = "Hello World"
#this is a comment
print("Hello World")
print(x)

# User Input
# input() function

print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name: ")
print(f"Hello {name}")

name = input("Enter your name: ")
print(f"Hello {name}")
fav1=input("Enter you favourite animal: ")
fav2=input("Enter you favourite color: ")
fav3=input("Enter you favourite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?") # f-string

#input number
import math
x = input("Enter a number: ")
y =math.sqrt(float(x))

print(f"The square root of {x} is {y}")

y=True
while y==True:
    x = input("Enter a number: ")
    try:
        x=float(x)
        y=False
    except:
        print("Wrong input, try again")
print("Thank you")

#data types
x=5
print(type(x))

#creating variables
x = 5
x="Hello World"
x=True
print(x)

x="john"
# is the same as
x='john'

#python is case sensitive

#else if is the same as elif

#continue means skip the current iteration and then continue with the next iteration
fruits =['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)
'''
break means stop the loop
range() function means to create sequence as in 
for x in range(5):
output will be 0,1,2,3,4
'''