from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, 4)
        self._breed = breed
        
    def __str__(self) -> str:
        return f'Dog {self._name} is a {self._age} yo {self._breed}'
    
    def bark(self) -> str:
        return 'Woof woof'
        

doggo = Dog('Max',2,'Boxer')
print(doggo)
print(doggo.bark())