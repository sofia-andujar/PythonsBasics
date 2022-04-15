class Animal():
    def __init__(self,name):
        self._name = name
        
    def makeSound(self):
        return f'{self._name}: Grr...'