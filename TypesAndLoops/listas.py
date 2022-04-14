#Exploring the posibility of creating lists made up from different types

# A list of integers
numeros = [0, 1, 2, 3, 4]
print(str(numeros[0]) + " " + str(numeros))

for num in numeros:
    print(num)

# An empty list
empty_list = []
print(empty_list)

#Different sintax
not_empty_list = [1,]
print(not_empty_list)

# A list similar to a json array
different_types_list = [1, 2, "3", ["otra", "lista"], "wow", 879.5]
print(different_types_list)
print(different_types_list[3])
print(different_types_list[3][1])
print(different_types_list[3][1][2])

print("3" in different_types_list)

# Basic list function like append, insert, len...
nums = [1,2,3,4,5,6,7]
nums.append(8)
nums.insert(0,0) # It doesn't replace existing data
print(nums)
print(len(nums))
nums.remove(4)
print(nums[0:5])

# We can also pop an element
fifo_list = ['first','second','third','forth']
print(fifo_list)
print(fifo_list.pop(2))
print(fifo_list)

# In order to clear RAM memory:
del fifo_list
print(fifo_list) # error