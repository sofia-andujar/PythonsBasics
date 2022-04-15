class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def __add__(self, other):
        return f'{self._name} {other._name}'
    
    def __sub__(self, other):
        return self._age-other._age
    
    def __str__(self):
        return f'Name: {self._name} | Age: {self._age}'
