# We are going to define a function but we don't know how many arguments we'll have
# We use * for receiving tuples
def unkownNumberOfArguments(*arguments) -> tuple:
    for argument in arguments:
        print(argument,end=' ')
    else: 
        print('')
    return arguments


# We use ** for dictionaries
def unkownNumberOfArguments2(**terms) -> dict:
    for key,value in terms.items():
        print(f'{key} : {value}')
    return terms

# For using lists we don't use anything
def unkownNumberOfArguments3(elements) -> list:
    for el in elements:
        print(el, end=' ')
    else:
        print('')
    return elements
    

# Execution
tup = unkownNumberOfArguments(1,2,3,4,5,6) # In this case we introduce a varible amount of items
print(tup)

tup2 = unkownNumberOfArguments(1,2,'a',"Sofía")
print(tup2)

dic1 = unkownNumberOfArguments2(Name='Sofía', Age=21) # Here random amount of key:value
dic2 = unkownNumberOfArguments2(Name='Miguel', Age=64, Hobby='Cycling')

lis1 = unkownNumberOfArguments3([1,2,3,4,'a','b']) # Here it has to be an alement
print(lis1)
lis2 = unkownNumberOfArguments3((1,2,3,4,'a','b')) # It can be a tuple
print(lis2)
lis3 = unkownNumberOfArguments3({1:2,3:4,'a':'b'}) # Or a dictionary
print(lis3)
lis4 = unkownNumberOfArguments3('Hola Caracola') # Or a string
print(lis4)