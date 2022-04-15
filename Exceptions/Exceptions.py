from MyException import MyException

# We are going to see how to deal with errors and expceptions in python:

c = None

# What is declared inside try is not accesible from outside try-except
try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    if a==b:
        raise MyException('my exception') # Raise could be use with already existing exceptions
    else:
        c=a/b # Is going to arise a ZeroDivisionError
except ZeroDivisionError as e:    
    print(f'Error: {type(e)} occured.')
except TypeError as e:    
    print(f'Error: {type(e)} occured.')
except Exception as e:
    print(f'Error: {type(e)} occured.')
else:
    print(f'No Exception occured')
finally:
    print(f'Finally block is always executed')

print(f'Out of try-except block. Result: {c}')
    
# Exception class is parent from ZeroDivisionError and TypeError
# So more generic way to deal with Exceptions is using it
# For expecificness we can put particular exceptions first
# In case of no coincidence Except will rise the error