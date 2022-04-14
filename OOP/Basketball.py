from Ball import Ball
from Sport import Sport

# This is how to deal with multiple heritance
class Basketball(Sport,Ball):
    def __init__(self, teams, players,diameter,preassure,color):
        #super().__init__(teams, players)
        Sport.__init__(self,teams,players)
        Ball.__init__(self,diameter,preassure,color)
    
    def courtDimensions(self,wide,length):
        self._wide = wide
        self._lenght = length
        
# MRO - Method Resolution Order
print(Basketball.mro())  # We search the method to execute in this order  