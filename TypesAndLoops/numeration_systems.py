import math
from decimal import Decimal

# ---------- INTEGER -----------
print('INTEGER'.center(20,'-'))

# Decimal
dec = 10
print(f'{dec}')

# Binary
bin_ = 0b1010
print(f'{bin_}')

# Octal
oct_ = 0o12 
print(f'{oct_}')

# Hexadecimal
hex_ = 0xA
print(f'{hex_}')

# int method: check the documentation
# here 2 is the base
bin_ = int('1010',2) # We tell the method how to interpret our string
print(f'{bin_}')

base_ten = 1
print(f'{base_ten} (dec) in different bases')
for i in range(2,37):
    print(f'base {i}: {int(str(base_ten),i)}')
    
# ---------- FLOAT -----------
print('FLOAT'.center(20,'-'))

a = 3.0
print(f'a: {a:.4f}') # We can specify the format to be printed

a = float(10)
print(f'a: {a:.2f}')

a = float('5')
print(f'a: {a:.2f}') 
# the float constructor is overloaded


# exponential notation implies floating type as a result
# in general, any operator in floating point makes the resulting variable of type float
a = 3e5 
print(f'a: {a}')
a = 3e-5 
print(f'a: {a:.6f}')
a = 3e-11
print(f'a: {a:.11f}')

# ---------- INFINITE VALUES ----------
print('INFINITE'.center(20,'-'))

pos_inifinite = float('inf')
print(f'Positive infinite: {pos_inifinite}')
print(f'Is {pos_inifinite} infinite?: {math.isinf(pos_inifinite)}')

# This gives an error bc str is not a number
# inf_ = 'inf'
# print(f'Is {inf_} infinite?: {math.isinf(inf_)}') 

neg_inifinite = float('-inf')
print(f'Negative infinite: {neg_inifinite}')
print(f'Is {neg_inifinite} infinite?: {math.isinf(neg_inifinite)}')

# math module
pos_inifinite = math.inf
print(f'Is {pos_inifinite} infinite?: {math.isinf(pos_inifinite)}')

neg_inifinite = -math.inf
print(f'Is {neg_inifinite} infinite?: {math.isinf(neg_inifinite)}')

# decimal module
pos_inifinite = Decimal('Infinity')
print(f'Is {pos_inifinite} infinite?: {math.isinf(pos_inifinite)}')

neg_inifinite = Decimal('-Infinity')
print(f'Is {neg_inifinite} infinite?: {math.isinf(neg_inifinite)}')

# ---------- Nan (Not a Number) ----------
print('NaN'.center(20,'-'))

a = float('nan') 
b = float('NaN') # Is not case sensitive
print(f'a: {a}, b: {b}')
print(f'Is {a} not a number? {math.isnan(a)}')

# nan with decimal module
a = Decimal('nan')
print(f'Is {a} not a number? {math.isnan(a)}')


# ---------- BOOLEAN ----------
print('BOOL'.center(20,'-'))

zero = 0
boolean = bool(zero)
print(f'bool({zero}) = {boolean}')

num = 2
print(f'bool({num}) = {bool(num)}')

empty_string = ''
print(f'bool({empty_string}) = {bool(empty_string)}')
not_empty_string = 'a'
print(f'bool({not_empty_string}) = {bool(not_empty_string)}')

# The same happens for collections (lists, tuples, dictionaries)

# Control sentences (if, while) call bool if we use a different type:
if '':
    print('True')
else:
    print('False') # bool('') = False