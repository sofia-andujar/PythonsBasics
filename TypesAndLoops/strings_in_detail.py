# Going deeper into str type

# Concatenation:
a = 'Hello' + 'World'
print(a)
a = 'Hello''World'
print(a)
b = a + 'Bye'
print(b)
# error
#b = a 'Bye'
b += 'Bye''.'
print(b)

#help(str) # This gives us the documentation of the class
help(str.splitlines) # This gives us the documentation of the method

# Strings are immutable in Python which means 
msg1 = 'hello'
msg2 = msg1.capitalize()
print(f'msg1: {msg1}, id: {hex(id(msg1))}') # id is the memory address
print(f'msg2: {msg2}, id: {hex(id(msg2))}')

msg3 = msg2
msg2 = msg1
print(f'msg1: {msg1}, id: {hex(id(msg1))}') # now despite having three messages
print(f'msg2: {msg2}, id: {hex(id(msg2))}') # there are only two memory addresses used
print(f'msg3: {msg3}, id: {hex(id(msg3))}') # msg1 and msg2 point the same address

msg4 = 'Hello'
print(f'msg4: {msg4}, id: {hex(id(msg4))}') # msg4 however creates a new string, doesn't point the initial msg2 address

help(str.join)
# iterable is a list, a dictionary, a tuple, etc...
tupla = ('Hello','World','Whats','Up')
print(tupla)
sep = ' '
msg = sep.join(tupla)
print(msg)

print(msg:='.'.join(msg)) # Strings are iterables too

dictionary = {'DNI':'4748471', 'Name':'Sofia',}
keys = ' | '.join(dictionary.keys())
values = ' - '.join(dictionary.values())
print(keys)
print(values)

# Obtain a list from a string
help(str.split)
string = 'A, B, C, D, E, F, G'
list_ = string.split(', ')
print(f'string: {string} -> list: {list_}')


# Formating a string
name = 'George'
age = 21
format_string = 'His name is %s and he\'s %d years old'%(name,age) # %s is used for strings and %d for decimal
print(format_string)
print(type(format_string)) # The result is a string too
# %.xf is for floating point format
tuple_ = ('George',21)
format_string = 'His name is %s and he\'s %d yo'%tuple_
print(format_string)


# More options for formating
salary = 2000
format_string = 'Name: {}; Age: {}; Salary: {:.2f}'.format(name,age,salary)
print(format_string)

format_string = 'Name: {0}; Age: {1}; Salary: {2:.2f}'.format(name,age,salary)
print(format_string)

format_string = 'Salary: {2:.2f}; Name: {0}; Age: {1}'.format(name,age,salary)
print(format_string)

format_string = 'Name: {n}; Age: {a}; Salary: {s:.2f}'.format(a=age,n=name,s=salary)
print(format_string)

dictionary = {'name':name, 'age':age, 'salary':salary}
format_string = 'Name: {person[name]}'.format(person=dictionary)
print(format_string)


# f-string
f_string = f'Hello'
print(type(f_string))
print(f'Name: {name}, Age: {age}, Salary: {salary:.2f}')

# Backslash or scape character \
    
print('Hello \' World')
print('Hello\b World\b \b ')
print('Hello \\')
print('New line \n string ')
print(r'Row new line \n String') # r stands for raw
print(r'C:\PATH')


# UNICODE 

print('Hola\u0020Mundo') # 0x0020 is white space in unicode
print('Letter a in unicode: \u0041')
print('Letter a in extended unicode: \U00000041')
print('Hexadecimal notation: \x41') # Only valid for 2 digits hex values


# ASCII

print(f'Letter a: {chr(65)}')
print(f'Character @: {chr(64)}')
char = 'A' 
print(f'Is chr(65) == A: {chr(65)==char}')