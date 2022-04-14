# In sets can add new elements, there aren't index and there cannot be repeated elements

planets = {'Mars','Earth','Venus'} # We use {} for sets
print(planets)
#print(planets[1]) #error

print('Mars' in planets)

planets.add('Jupiter')
print(planets)

planets.add('Earth') # It does not do anything bc Earth is already there

planets.remove('Earth')
print(planets)

planets.discard('Pluto') # no error
print(planets)
#planets.remove('Pluto') # error
#print(planets)

planets.clear()
print(planets)

del planets
print(planets) # planets doesn't exist any longer -> error