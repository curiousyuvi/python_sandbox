# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

'''
x = 1  # int
y = 2.0  # float
flag = True  # bool
str = "hello"  # string
'''

# Multiple assignment

x, y, flag, s = (1, 2.0, True, "hello")

print(x, y, flag, s)

# Check type
print(type(x))

# Type casting
print(str(x)+str(y))
print(type(float(flag)))
