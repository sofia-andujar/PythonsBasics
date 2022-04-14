# Basic Function
def firstFunction():
    print('Helo World from function')

# Basic Parameter
def secondFunction(param):
    print(f'Helo World with parameter: {param}')    

# Return Statement
def thirdFunction(a,b):
    print(f'{a} + {b} = {a+b}')     
    return a+b

# Default values
def forthFunction(a=1,b=2):
    print(f'{a} + {b} = {a+b}')     
    return a+b

# Return type and parameters type suggestion
def fifthFunction(a:int = 1, b:int = 2) -> int:
    print(f'{a} + {b} = s{a+b}')     
    return a+b

# Execution of functions:
firstFunction()

secondFunction('UWU')
secondFunction(123456789)

print(result:=thirdFunction(8.5,10.5))
print(f'El resultado es {result}')

forthFunction()
forthFunction(2,10)

fifthFunction()
fifthFunction('a','b')