# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'David'
age = 37

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format (name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')



s = 'hello world how are you?'

# Capitalize string
print(s.capitalize())

# String Formatting

# String Methods


# Split into a list
print (s.split())

# Find position
print(s.find('r'))