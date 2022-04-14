# Tuples are similar to lists but immutable 

fruits = ('banana','apple','pear','orange') # We use parenthesis instead of []
print(f'length of tuple fruits ({fruits}) is: {len(fruits)}')

for fruit in fruits:
    print(fruit, end=', ')
else:
    print('')

# Let's check the immutability
#fruits[0] = 'watermelon' #error
#print(fruits)

# Converting form tuple to list and back
fruits_list = list(fruits)
fruits_list[0] = 'watermelon'
fruits = tuple(fruits_list)
print(fruits)

print()