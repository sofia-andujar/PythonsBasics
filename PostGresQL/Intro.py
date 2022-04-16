import psycopg2

# We want to work with a database created on pgAmin4 that we have previously definned

# 1. Create a connection with the database
connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# 2. Create a cursor to intereact
cursor = connection.cursor()

# 3. Accessing things
cursor.execute('SELECT * FROM persona')
registers = cursor.fetchall() 
print(registers) # A list of tuples

# 4. Closing connections
cursor.close()
connection.close()