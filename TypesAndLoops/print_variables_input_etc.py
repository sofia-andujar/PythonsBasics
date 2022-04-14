#Trying some basic commands and functions like input(), print(), int(), str()...

text = input('Introduce un numero: ')
print('Tu mensaje en string es: ' + text )
text = int(text)
print('Tu mensaje como int es: ' + str(text))

# A way to store variables in line 
print(num:=int(input('Introduce un numero: ')))

# Some boolean basics
x = 4
y = 2
print(not 1+1==2 or x==4)


#More printing stuff
print('''
hola + salto de línea
    hola con tab 
hola con caracter especial ' 
''')

print('hola % que tal')

print(f'hola, este texto tiene formato {num} ')