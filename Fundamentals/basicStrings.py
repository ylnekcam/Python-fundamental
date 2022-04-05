# Strings
course = "THIS IS SAMPLE'S COURSE"
use_singleqoute = 'use single qoute'
use3quote ='''
This is using 3 quote
for string
and etc.

'''
print (course)
print (use_singleqoute)
print (use3quote)

# Strings index square pattern index
print("This is index 0 "+ course[0])
print("This is index -3 "+ course[-3])
print("This is index 0:3 "+ course[0:3])
print("This is index :5 "+ course[:5])
print("This is index 1:-1 "+ course[1:-1])

# Formatted Strings
firstname = 'Mac'
lastname = 'Santiago'
msg = f'{firstname} [{lastname}] is a coder'
print (msg)
# or use this
message = firstname + '[ ' + lastname + '] is a coder'
print (message)

#len function you can add . to see all methods for string
print (len(firstname))
print(firstname.upper())
print(firstname.lower())
print(firstname.title())
print(firstname.find('m'))
print(msg.replace('S','A'))
print('word' in firstname)
