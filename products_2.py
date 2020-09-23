
import sqlite3

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)') # Adds unique constraints to variables
conn.close()

name = 'hat'
quantity = 4

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?, ?)', (name, quantity) )
    conn.close()
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM products')

for row in results:
    print(row)

print('end of program!')
