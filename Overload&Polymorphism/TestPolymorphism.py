from Animal import Animal
from Dog import Dog

animal = Animal('Carl')
doggo = Dog('Max','Pitbull')

print(animal.makeSound())
print(doggo.makeSound())
print(doggo.sleep())
# print(animal.sleep()) # Not existing method for animal

if isinstance(doggo,Dog):
    print(f'{type(doggo)} is a Dog instance')
else:
    print(f'{type(doggo)} is not a Dog instance')