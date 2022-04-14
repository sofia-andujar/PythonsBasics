# All classes in Python inherit from object 

class Animal:
    # Class Atributes
    # None yet
    # Method with Instance Atributes:
    # dunder init
    def __init__(self, name='michi', age=5, paws=4):
        self._name = name  # The _attributes are meant to be private
        self._age = age
        self._paws = paws
    # self is the reference to mem address where our Animal Instance is stored
    
    #def __del__(self):
    #    print(f'Deleting Animal {self._name}.')

    # Get Methods:
    @property  # this way we can do animal.get_name instead of animal.get_name()
    def name(self):  # As this method is called name, the setter should be called name as well
        print('Name getter')
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def paws(self):
        return self._paws

    # Set Methods:
    @name.setter
    def name(self, name):
        print('Name setter')
        self._name = name

    @age.setter
    def age(self, newAge):
        self._age = newAge

    @paws.setter
    def paws(self, newPaws):
        self._age = newPaws


# This code may be annoying in future uses of Animal
# Solucion:
if __name__ == '__main__':

    # When we create a new Animal init is called and the name of the isntace takes the self value
    michiCat = Animal('Michi', 5, 4)
    print(michiCat.name)

    # We can access class methods as static java methods
    michiCat.name = "Lucy"
    print(michiCat.name)

    # We can aggregate attributes whenever we want similar to animous classes
    # The rest of Animals doesn't have the birthday attribute
    michiCat.birthday = '24/10/2016'

    print(__name__)  # It prints __main__ when running this code
