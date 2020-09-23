
import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (1001, "jacket")')
    conn.close()

def display_all_data():
    # NOT COMMITTING any changes here so context mangaer i.e. with sqlite3.connect(db) as conn: is NOT required in this case
    conn = sqlite3.connect(db) # We DO still need to connect to the database!
    results = conn.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) # Each row is a Row object

    conn.close() # DO need to CLOSE our connection

def display_one_product(product_name):
    conn = sqlite3.connect(db) # We DO still need to connect to the database!
    results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row)
    else:
        print('not found')
    conn.close()

def create_new_product():
    # Inputs below prompt user for new info to add
    new_id = int(input('Enter new ID: '))
    new_name = (input('Enter new product name: '))
    # Inserts user input info into products table of first_db
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO products VALUES (? , ?)', (new_name, new_id)) # Use PARAMETERIZED QUERIES to combine data and SQL statements!
    conn.close()

def update_product():
    update_product = 'wool hat'
    update_id = 1000

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id= ?', (update_product, update_id))
    conn.close()

def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from PRODUCTS WHERE name = ?', (product_name,))
    conn.close()

# Create functions for easier, more legible modular code

create_table()
insert_example_data()
display_all_data()
display_one_product('hat')
create_new_product()
update_product()
delete_product('jacket')
display_all_data




