# Typical if else structure:

age = int(input("Introduce your age: "))

if age > 18:
    print("Congrats, you're of legal age")
elif age < 5:
    print("You're such a baby")
else:
    print("You're between 5 and 18 yo")
    
# Different if else sintax
flag = input('Write True(1)/False(0): ')
flag = bool(int(flag))
# Only recommended for short code lines, we cannot use elif here
print("True value") if flag else print("False value")

########################################################################


# While loop
x = int(input("Introduce a number from 0 to 10: "))
while x <= 5:
    print(f'Your number {x} is less than or equal to 5, let\'s make it greater')
    x+=1
else:
    print(f'Your number {x} is already more than five')
# The else is executed when while ends

########################################################################


# for loop

word = "Hello"

# Iterator sintax
for letter in word:
    print(letter)
else:
    print('Again, not really an else, just the end of the loop')

# Function range
print(range(10))

# More typical for sintax
for i in range(6):
    print(i)
    print(word[i]) if (i<len(word)) else None
print('End of loop')

# None is no-op instruction, I couldn't use continue nor pass in that expression