# in python types of variable are determined at runtime

numB = 3290

age: int = 2309
age = 'good'


# you can use negative index ipython
sampleStr = "I'm a man with sad stories"
sampleStr[-1]  #return the last index in the string
print(sampleStr[-2])


#escape sequeces in python
# #--> for comments
# \' for adding a single quote
# \" for adding a double quote
# \n for a new line

print(sampleStr.upper())

# check is a string if part of a string exist in another -- we use the in keyword

"man" in sampleStr
"sade" not in sampleStr

# bin

# complex numbers in python

x = 1 + 2j

# python // double division give integer result

print(7 // 3)


# in python there are no constants -- we use upper case letters to let others
# we use upper case letters to let other developer know that a variable should be constant

PI = 943280
import math
# allows complex mathematical operation

math.degrees(43)

# one more thing is python is a strongly typed language
# it does not do any type conversion

z = input("x: ")

print(int(z))
print(float(z))
print(bool(z))

# falsey values in python
# Falsy
# ""
# []
# None (null)
y = 3
if y >= 4:
    pass # use pass in python to have an empty block, basically to pass
else:
    pass


#we use indentation in python for block of code
emptyPan = ""
if not emptyPan:
    print("Emptypan is a sring")


# chaining comparison

pwn = 75

if 18 <= age < 65: # if age is reater or  equal to 18 and less than 65
    print("Top of the world")

# turnery operator in python
message = "Eligle" if age >= 18 else "not eligible"


# in python we only have for loops and while loop

for g in "Python":
    print(x)


# range keyword allow loop over a ser of keyowrds=

print(type(range(5))) # range are iterable like list 
# range use very small amount of meory

names = ['dsd', 'fdsfs', 'fsdf']
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else: # else is used in when loops succesfully end without breaking
    print("Not found")

    ## you can return many argument as tottple

# define a function as def -- > for function defination
# totple is like a list which is read only 



#python we don not have scope level scope
# we onlyhave block level scope - defining a varaible will make it avaiplabe anywhere

message = "a"

def greet()
    global message # it's not good to modify a global variable inside a function \\ 
    # also when you just override a global within a function scope, python will interprate it a new variable
    message = "b" # if you have to, then use the gloval keyword


greet()
print(message)


