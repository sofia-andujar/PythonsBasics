# Dynamic and static contexts

class AnotherClass:
    
    staticVar = ''
    
    def __init__(self):
        AnotherClass.staticVar += 'new instance'
    
    @staticmethod
    def staticMethod(arg):
        AnotherClass.staticVar += arg
        print(AnotherClass.staticVar)
        
    @classmethod
    def classMethod(cls,arg):
        cls.staticVar += arg
        print(cls.staticVar)
        
    def instanceMethod(self,sth):
        self.classMethod(sth)
        self.staticMethod(sth)
        
AnotherClass.classMethod('hello ')
AnotherClass.classMethod('whats up ')

obj1 = AnotherClass()
obj1.classMethod('?') # Dyncamic objetcs like instance can access static context with no problem
print(obj1.staticVar)

obj1.instanceMethod('instance calling') # again this dynamic method has no trouble dealing with static methods itself