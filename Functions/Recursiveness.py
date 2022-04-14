# Typical exponential function to get familiar with recursive functions
def factorial(num:int = 1) -> int:
    if num <= 1:
        return 1 # This is the breakpoint of the recursiveness
    else:
        return num*factorial(num-1)
    
for x in range(10):
    print(f'{x}! = {factorial(x)}')