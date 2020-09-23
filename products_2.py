
import sqlite3

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT')
conn.commit()
conn.close()

name = 'scarf'
quantity = 2

with sqlite3.connect(db) as conn:
    conn.execute('INSERT INTO products VALUES (?, ?)', (name, quantity))
conn.commit()
conn.close()
