
import sqlite3

conn = sqlite3.connect('first_db.sqlite') # connect/create new if it does not already exist

conn.execute('CREATE TABLE products (id int, name txt)')

conn.execute('INSERT INTO products values (1000, "hat")')
conn.execute('INSERT INTO products values (1000, "jacker")')

conn.commit()

results = conn.execute('SELECT * FROM products')

for row in results:
    print(row)

conn.close()





