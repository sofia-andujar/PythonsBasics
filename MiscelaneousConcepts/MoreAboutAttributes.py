# Class Attributes or variables are like static attributes in Java
# They're shared by all instances of the same class

class AClass:
    commonVar = 'AClass class attribute'
    log = 'log: '
    counter = 0
    
    def __init__(self,arg):
        self.instanceVar = arg
        AClass.log += f'{arg} created; ' 
        AClass.counter += 1
        print(f'{AClass.log}, instances created: {AClass.counter}')
        
print(AClass.commonVar)
aClass1 = AClass('class1')
aClass2 = AClass('class2')
print(aClass1.commonVar)
print(aClass2.commonVar)

# Not very common but possible:
AClass.newClassVar = 'AClass second class attribute'

print(AClass.newClassVar)
print(aClass1.newClassVar)
print(aClass2.newClassVar)