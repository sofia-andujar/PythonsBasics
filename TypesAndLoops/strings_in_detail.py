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



