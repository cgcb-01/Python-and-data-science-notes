# PACE FORWARD INTO SOME KINDA BASIC STUFFS

# Arithmatic operator + addition, - subtraction, * multiplication, / division, % modulo , ** exponent:2**3=8
# For rounding the value of a division we can use //

pow_result = 2**4
print(pow_result)

# input function to take input
# user_inp = input("Enter Something: ")
# print("You Entered:", user_inp)

# Strings and its Formatting
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

# Type casting
# int(),float(),str(),bool()-just needs to put something will convert it into that data type.
st = "Sutapa"
print(bool(st))  # anything other than 0 is always true.

# String Methods
str = "I love Biriyani a lot"
print(str.upper())  # to upper case
print(str.lower())  # to lower case
print(str.capitalize())  # capitalise the first letter rest in small
print(str.title())  # capitalise all words first letter
print(len(str))  # length of the string
print(str[0:4])  # substring from 0 to 3 included here 4 is not included.

# Comparison Operators
# == for equality, != not equal, < etc

# LOGICAL OPERATORS
# and & could also be written, not for not operation.

print(True and True)
print(True or False)
print(not True)

# Conditional Statement (else if== elif)
x = 5
if x >= 10:
    print("Hello")
else:
    print("Bye")

# loops-> FOR LOOP
# range(start,stop,step)
for i in range(5, 1, -2):
    print(i)
for i in range(0, 6):  # default step =1
    print(i)

# while loop(while condition:)

# 1D,2D,3D list
# 2d list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

# nested list
nested_list=['India','spain','Brazil',['West Bengal','Sikkim','Bihar','Jharkhand'],[['Howrah','Uluberia','Andul'],'Gangtok','Namchi','Kolkata']]
print(nested_list[0])
print(nested_list[3][0:2])
print(nested_list[4][0][0]+" "+nested_list[4][1])

for i in range(0,len(nested_list),1) :
    print(i+" : "+nested_list[i])