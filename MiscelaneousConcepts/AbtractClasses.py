# Abstract methods are exactly the same as in Java
# An abstract method in father class impose child class to give it an implementation
# Abstract Classes are inhereted from ABC (Abstract Basic Class) and cannot be instanciated
# abstractclassmethod is a decorator

from abc import ABC, abstractmethod

class GeomtricFigures(ABC):
    
    def __init__(self,width,height):
        self._width = width
        self._height = height
    
    @abstractmethod
    def area(self) -> int:
        pass
    
class Square(GeomtricFigures):
    def __init__(self, width):
        super().__init__(width,width)
    
    def area(self) -> int:
        return self._width**2
    
    
#geom = GeomtricFigures(5,10)  # We cannot instanciate abstract classes 
sq1 = Square(5)
print(sq1.area())