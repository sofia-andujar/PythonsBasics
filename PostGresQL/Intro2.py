# As we already know we can use keywork with to access files and connections
# However they warn us in the documentation of psycopg2 that we should close
# the connection carefully

import psycopg2

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
            id_table = input('Introduce id value: ')
            
            cursor.execute('SELECT * FROM persona WHERE id=%s',(id_table,))
            registers = cursor.fetchone()
            print(registers)
            
            ids_table = input('Introduce id values (comma separated): ')
            ids_table = (tuple(ids_table.split(',')),) # It has to be a tuple of tuples
            cursor.execute('SELECT * FROM persona WHERE id IN %s',ids_table)
            registers = cursor.fetchall()
            for register in registers:
                print(register)
                
        # Cursor is going to be closed thanks to the with statement
except Exception as e:
    print(f'An error occured: {e}')
finally:
    connection.close() # We can be sure connection will be closed no matter what
