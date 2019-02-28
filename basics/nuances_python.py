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

if y >= 4:
    pass # use pass in python to have an empty block, basically to pass
else:
    pass


#we use indentation in python for block of code
emptyPan = ""
if not emptyPan:
    print("Emptypan is a sring")