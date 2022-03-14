# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Yuvraj'
age = 19

print('My name is '+name+' and my age is '+str(19)+' years.')

# String Formatting

print('My name is {name} and my age is {age}'.format(name=name, age=age))

# f-string
print(f'My name is {name} and my age is {age}')

s = 'wow i am so cool'

# String Methods
# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
