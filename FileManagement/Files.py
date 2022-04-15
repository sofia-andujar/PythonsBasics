from FilesManager import FilesManager

# Python allows you to work with .txt, .bin, .csv, etc.
# Let's work with .txt to see how it all works

# writing files


try:
    my_file = open('FileManagement\\testing.txt','w', encoding='utf8') # 'w' means we can write
    my_file.write('Hello world\n') # Write method doesn't aggregate \n
    my_file.write('We can use accents: Sofía\n')
    my_file.write('Goodbye world.')
except Exception as e:
    print(e)
finally:
    my_file.close()
    
# reading files

try: 
    my_file = open('FileManagement\\testing.txt','r',encoding='utf8')
    print(my_file.read(1)) # Reads num of chararacters
    print(my_file.read(5))
    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readlines())
    # When you read things you run out of things to read, you don't go to the beggining again
    
except Exception as e:
    print(e)
finally:
    my_file.close()
    
# appending files, creates new file if not existing
try:
    my_file = open('FileManagement\\testing.txt','a', encoding='utf8') # 'a' stands out for append
    my_file.write('\nWe\'re going to add more info\n')
except Exception as e:
    print(e)
finally:
    my_file.close()
    

# Opening files with "WITH"
    
with open('FileManagement\\testing.txt','r',encoding='utf8') as my_file:
    print(my_file.read())
    
# with does two things
# 1: it calls __enter__ to open the file 
# 2: then is calls __exit__ to close the file

with FilesManager('FileManagement\\testing.txt') as my_file:
    print(my_file.read())
    
# with does two things again
# 1: it calls __enter__ to open the file 
# 2: then is calls __exit__ to close the file