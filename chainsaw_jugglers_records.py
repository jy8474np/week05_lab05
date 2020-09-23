
import sqlite3

db = 'record_holders_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS rankings (name text, country text, catches int)')
    conn.close()

def existing_record_holders():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO rankings values ("Jane Mustonen", "Finland", 98)')
        conn.execute('INSERT INTO rankings values ("Ian Stewart", "Canada", 94)')
        conn.execute('INSERT INTO rankings values ("Aaron Gregg", "Canada", 88)')
        conn.execute('INSERT INTO rankings values ("Chad Taylor", "USA", 78)')
    conn.close()

def add_new_record_holder():
    # Inputs below prompt user for new info to add
    new_name = (input("Enter record holder's name: "))
    new_country = (input("Enter record holder's country of origin: "))
    new_catches = int(input("Enter record holder's highest number of catches: "))
    # Inserts user input info into record_holders table of first_db
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO rankings VALUES (? , ?, ?)', (new_name, new_country, new_catches)) # Using parameterized queries to combine data and SQL statements
    conn.close()

def search_by_record_holder():
    search_name = (input('Enter the name of the record holder whose information you would like to view: '))
    conn = sqlite3.connect(db) # Connect to the database
    results = conn.execute('SELECT * FROM products WHERE name like ?', (search_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Here are the details for the record holder you searched: ', first_row)
    else:
        print('We were unable to find a record holder by that name in our database.')
    conn.close()

def update_record_holder():
    update_name = (input('Enter the name of the record holder you would like to update: '))
    update_catches = int(input("Enter record holder's updated number of catches: "))
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE rankings SET catches = ? WHERE name = ?', (update_catches, update_name))
    conn.close()

def delete_record_holder():
    delete_name = (input('Enter the name of the record holder you would like to delete: '))
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from rankings WHERE name = ?', (delete_name,))
    conn.close()

create_table()
existing_record_holders()
add_new_record_holder()
search_by_record_holder()
update_record_holder()
delete_record_holder()
