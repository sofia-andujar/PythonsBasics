# Let's keep exploring what we can do from python
from unicodedata import name
import psycopg2

# We create the connection
connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# Playing around with SELECT options in the excecute command and fetchone vs fetchall
try:
    with connection:
        with connection.cursor() as cursor:
        # Cursor is going to be closed thanks to the with statement
            # ----------------- Inserting things ------------------
            insert_sentence = 'INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)'
            
            name = input('Introduce name: ')
            surname = input('Introduce surname: ')
            email = input('Introduce email: ')
            values = ((name,surname,email)) # A tuple of tuples
            
            cursor.execute(insert_sentence,values)
            # connection.commit() # Because we are modifying things
            # with sentence is going to make the commit for us :)
            print(f'Inserted registers: {cursor.rowcount}')
            
            # -------------- Inserting several things -------------
            insert_sentence = 'INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)'
            
            registers_len = int(input('How many registers do you want to insert?: '))
            
            values = [] # Initialize as list so we can append items
            for i in range(registers_len):
                name = input('Introduce name: ')
                surname = input('Introduce surname: ')
                email = input('Introduce email: ')
                values.append((name,surname,email)) # We append the tuple to the list
            values = tuple(values) # A tuple of tuples
            
            cursor.executemany(insert_sentence,values)
            # connection.commit() # Because we are modifying things
            # with sentence is going to make the commit for us :)
            print(f'Inserted registers: {cursor.rowcount}')
            
except Exception as e:
    print(f'An error occured: {e}')
finally:
    connection.close() # We can be sure connection will be closed no matter what