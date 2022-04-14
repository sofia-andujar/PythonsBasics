# Let's get familiar with DocString
# Notice we're not using the dunder init method

class MathUtil:
    """
    MathUtil contains basic arithmetic operations.
    It's funcioning is similar to an static java class
    """
    def add(a, b):
        return a + b
    
    def substract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        return a / b
    
a = 5
b = 9     
print(MathUtil.add(a,b))
print(MathUtil.substract(a,b))
print(MathUtil.multiply(a,b))
print(f'{MathUtil.divide(a,b):.2f}') #.2f is an option for the f'' sintax in print
