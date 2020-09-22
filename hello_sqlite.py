
import sqlite3

conn = sqlite3.connect('first_db.sqlite') # connect/create new if it does not already exist
# conn.row_factory = sqlite3.Row

conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name txt)')

# conn.execute('INSERT INTO products values (1000, "hat")')
# conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit() # REQUIRED! Commits data above to table

results = conn.execute('SELECT * FROM products')

# all_rows = results.fetchall()
# print(all_rows)

for row in results:
    print(row[1]) # Each row is a Row object

results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)

conn.close()





