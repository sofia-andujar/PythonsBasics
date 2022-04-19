# Methods used is str class are usually available on byte class
#help(bytes) 

from base64 import decode


char_in_bts = b'a'
print(f'{char_in_bts}: {type(char_in_bts)}')

msg = b'Hello World'
print(f'Byte {msg[0]} = Char {chr(msg[0])}')

string = 'Python rules: ñàíü' # By default UTF-8 is used for default to encode string literals
bytes_ = string.encode()
print(f'({string}).encode() = {bytes_}')

string2 = bytes_.decode('UTF-8')
print(f'({bytes_}).decode() =  {string2}')

# It is important to know that these varibles point to the same references at memory, they are identical