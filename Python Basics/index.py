# PACE FORWARD INTO SOME KINDA BASIC STUFFS

# Arithmatic operator + addition, - subtraction, * multiplication, / division, % modulo , ** exponent:2**3=8
# For rounding the value of a division we can use //

pow_result = 2**4
print(pow_result)

# input function to take input
# user_inp = input("Enter Something: ")
# print("You Entered:", user_inp)

# ------------------Strings and its Formatting
# double Quotes:"" or Single Quotes:'', For Multi line use:''' triple single quotes'''.
multiline = """I am Sutapa.
And I am 19 years old"""
print(multiline)
# normal escape charachters like \n also works.

# formated string with f
name = "sutapa"
age = 19
print(f"My name is: {name} and I am {age} years old")
print(f"2+2={2+2}")

# to know the type of the variable use type()
young = True
print(f"name={type(name)},age={type(age)}, am i young?={type(young)}")

#------------------- Type casting
# int(),float(),str(),bool()-just needs to put something will convert it into that data type.
st = "Sutapa"
print(bool(st))  # anything other than 0 is always true.

# --------------String Methods
str = "I love Biriyani a lot"
print(str.upper())  # to upper case
print(str.lower())  # to lower case
print(str.capitalize())  # capitalise the first letter rest in small
print(str.title())  # capitalise all words first letter
print(len(str))  # length of the string
print(str[0:4])  # substring from 0 to 3 included here 4 is not included.

print("hello there"+"!"*4) # **repeating 4 times

# -------------Comparison Operators
# == for equality, != not equal, < etc

# -------------LOGICAL OPERATORS
# and & could also be written, not for not operation.

print(True and True)
print(True or False)
print(not True)

# ---------------Conditional Statement (else if== elif)
x = 5
if x >= 10:
    print("Hello")
else:
    print("Bye")

# ----------loops-> FOR LOOP
# range(start,stop,step)
for i in range(5, 1, -2):
    print(i)
for i in range(0, 6):  # default step =1
    print(i)

# while loop(while condition:)

#------------------ 1D,2D,3D list (list can have any data types)
# List are unordered and mutable(changeable)
# 2d list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# nested list
nested_list = [
    "India",
    "spain",
    "Brazil",
    ["West Bengal", "Sikkim", "Bihar", "Jharkhand"],
    [["Howrah", "Uluberia", "Andul"], "Gangtok", "Namchi", "Kolkata"],
    5,
    True,
    3333333.211,
]
print(nested_list[0])
print(nested_list[3][0:2])
print(nested_list[4][0][0] + " " + nested_list[4][1])

for i in range(0, len(nested_list), 1):
    print(nested_list[i])

# ---------------In Operator
text = "Hello World"  # checks whether it contains or not
number = [1, 2, 3]
result = "llo" in text
print(result)
print(3 in number)

# list Unpacking
# This allows us to split the elements in the list into multiple variables
my_list=[1,2,3]
a,b,c=my_list # unpacking
print(b)

lists=['Apple','Banana',['Orange','Pineapple']]
a,b,c=lists
print(c)
print(a)

Friends=["Sutapa","Sandipan","Prity","Shreya","Anwesha"]
first,second,*rest=Friends # the star is necessary
print(rest)
print(second)

#--------------- TUPLES
# (They are ordered and immutable-cant be edited)
# It has paranthesis
my_tuple=(1,2,3,'Hello',3.14)
print(my_tuple)
print(my_tuple[1])
print(type(my_tuple))

# my_tuple[0]=5 will give error as it is immutable
# changing in another way
# we can only concatenate
new_tuple=my_tuple+(5,'Word')
print(new_tuple) 
Friend_tup=('Prity','Sandipan','Sutapa','Aasman','Anwesha','Ishita')
for i in Friend_tup:
    print(i)
# even if we specify any paranthesis it becomes tuple
# Few weird things
number=1,2,3,4,5,6
print(type(number))
for i in number:
    print(number)
    
#-------------------- DICTIONARY 
# it has collection of key-value pairs where ech key Should be unique. It is unordered and mutable. Used for mapping

#dictionary with key-value pair{key:value}
student_info={"name":"Sutapa","age":19,"grade":"A"}
print(student_info)

#using Dict Constructor
person = dict(name="Sutapa", age=19, city="Howrah")
print(person)

mixed_dict={"name":"Charlie","age":21,"grades":[85,90,78],"is_student":True}
print(mixed_dict)

nested_dict={
    "person":{"name":"David","age":22},
    "location":{"city":"Paris", "Country":"France"}
}
print(nested_dict)

# making a dictionary using tuple
tuple_list=[("Name","Eva"),("Age",28),("city","Berlin")]
from_tuple_dict = dict(tuple_list)
print(from_tuple_dict)

# Accessing the elements
print(from_tuple_dict['Name'])
print(from_tuple_dict['Age']) # something unavailable not allowed

# by get() method
print(from_tuple_dict.get("city"))
print(from_tuple_dict.get("Not Available")) # something not available in dictionary is allowed

print("Iterating through key in Dictionary:")
mine_dict={'name': 'Eva', 'Age': 28, 'city': 'Berlin'}
for key in mine_dict:
    print(f"{key}:{mine_dict[key]}")

print("Iterating through key,value in Dictionary:")
for key,value in mine_dict.items():
    print(f"{key}:{value}")

# adding a new Key-Value Pair, Updating
my_dict={'name': 'Eva', 'Age': 28}
my_dict['city']="New York"
my_dict['Age']=27
print(my_dict)

# updating with another dictionary
update_dict={"name":"John","city":"Paris"}
my_dict.update(update_dict)
print(my_dict)

# updating with keyword
my_dict.update(age=29)


# ----------------FUNCTIONS
def greet(name,greet='Hello'):
    print(f"{greet},{name}")

greet("Sutapa")
greet("sutapa","Hi! there")

# named parameter
def rec_area(length,width):
    print(length*width)
    
rec_area(length=5,width=3)

# return parameter
def square_cube(x):
    square=x**2
    cube=x**3
    return square,cube

sq_result,cube_result=square_cube(2)
print(sq_result,cube_result)

#nested Function
def outer_fuction(x):
    def inner_fuction(y):
        return x+y
    result=inner_fuction(5)
    return result

result_value=outer_fuction(10)
print(result_value)

#----------------- LAMBDA FUNCTION
# lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
# It is used for short functions that are not reused.
add = lambda x, y: x + y
result = add(5, 3)
print(result)

# using Lambda function but applying filter to it
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using lambda with map
squared_numbers = map(lambda x: x ** 2, numbers) # This is a anonymous lambda function that takes the numbers in the number list square them ad map them with itself and gives the new map object. 
squared_numbers = list(squared_numbers)  # Convert map object to list  
print(squared_numbers)

# applying lambda with functions
# Function that takes another function as a parameter
def apply_operation(x,y,operation):
    return operation(x, y)
result_addition=apply_operation(7,8,lambda a,b:a+b)
result_multiplication=apply_operation(7,8,lambda a,b:a*b)
print("Result of the addition:", result_addition)
print("Result of the multiplication:",result_multiplication)

# -------------MODULES
import my_own_math as maths # here I am importing my module and giving it a alias 'math'
maths.intro()
print(maths.add(5, 3))
print(maths.subtract(23.5,12))
print(maths.multiply(5, 6))
print(maths.divide(10, 2))       

# importing a specific function from a module
from my_own_math import (power,multiply)
print("Power finding by my module:",power(2,3))
print("Power finding by my module:",multiply(2,3))

