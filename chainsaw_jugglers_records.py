
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

def update_record_holder():
    update_name = (input('Enter the name of the record holder you would like to update: '))
    update_catches = int(input("Enter record holder's updated number of catches: "))

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE rankings SET catches = ? WHERE name = ?', (update_catches, update_name))
    conn.close()

create_table()
existing_record_holders()
add_new_record_holder()
update_record_holder()


