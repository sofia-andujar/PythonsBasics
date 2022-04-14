from Animal import Animal


print('Creation of Objects'.center(50,'-'))

animal1 = Animal('michimu',7,4)
print (f'{animal1.name}, {animal1.age}, {animal1.paws}') 

# Problem: all the code from Animal es excuted
# Solution: condition with __name__


print('Elimination of Objects'.center(50,'-'))
del animal1 # This is not normally use, because there exists a garbage collector like in java