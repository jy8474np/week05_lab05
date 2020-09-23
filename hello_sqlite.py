
import sqlite3

with sqlite3.connect('first_db.sqlite') as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')

    conn.execute('INSERT INTO products values (1000, "hat")')
    conn.execute('INSERT INTO products values (1001, "jacket")')

    results = conn.execute('SELECT * FROM products')

    # all_rows = results.fetchall()
    # print(all_rows)

    for row in results:
        print(row[1]) # Each row is a Row object

    results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
    first_row = results.fetchone()
    print(first_row)

    # Inputs below prompt user for new info to add
    # new_id = int(input('Enter new ID: '))
    # new_name = (input('Enter new product: '))

    # Inserts user input info into products table of first_db
    # conn.execute(f'INSERT INTO products VALUES (? , ?)', (new_name, new_id)) # Use PARAMETERIZED QUERIES to combine data and SQL statements!

    update_product = 'wool hat'
    update_id = 1000
    conn.execute('UPDATE products SET name = ? WHERE id= ?', (update_product, update_id))

    delete_product = 'jacket'
    conn.execute('DELETE from PRODUCTS WHERE name = ?', (delete_product,))

conn.close()





