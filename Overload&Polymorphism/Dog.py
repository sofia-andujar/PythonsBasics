from Animal import Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed
        
    def makeSound(self):
        return f'{self._name}: Woof woof'
        
    def sleep(self):
        return f'{self._name}: Zzz...'