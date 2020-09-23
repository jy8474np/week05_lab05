
import sqlite3

db = 'record_holders_db.sqlite' # Assign variable db to database path for ease

# Create a table called rankings, if it doesn't already exist
def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS rankings (name text, country text, catches int)')
    conn.close()

# Populate rankings table with existing rankings data
def existing_record_holders():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO rankings values ("Jane Mustonen", "Finland", 98)')
        conn.execute('INSERT INTO rankings values ("Ian Stewart", "Canada", 94)')
        conn.execute('INSERT INTO rankings values ("Aaron Gregg", "Canada", 88)')
        conn.execute('INSERT INTO rankings values ("Chad Taylor", "USA", 78)')
        conn.execute('INSERT INTO rankings values ("Groucho Marx", "Feedonia", 01)') # Added as fun, easy delete choice
    conn.close()

# Obtain data for all columns via user input prompts and update rankings table with new info
def add_new_record_holder():
    new_name = (input("Enter new record holder's name: "))
    new_country = (input("Enter new record holder's country of origin: "))
    new_catches = int(input("Enter new record holder's highest number of catches: "))
    # Inserts user input info into a new row within the record_holders table
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO rankings VALUES (? , ?, ?)', (new_name, new_country, new_catches))
    conn.close()

# Obtain name for desired record holder via user input prompt and display record holder's most up-to-date info
def search_by_record_holder():
    search_name = (input('Enter the name of the record holder whose information you would like to view: '))
    conn = sqlite3.connect(db)
    search_results = conn.execute('SELECT * FROM rankings WHERE name like ?', (search_name, )) # Search table by name
    first_row = search_results.fetchone()
    # Display info if record holder found, display error if record holder not found
    if first_row:
        print('Here are the details for the record holder you searched: ', first_row)
    else:
        print('We were unable to find a record holder by that name in our database.')
    conn.close()

# Obtain name of desired record holder via user input prompt and update catches if found
# If record holder is not found, display error message

def update_record_holder():
    update_name = (input('Enter the name of the record holder you would like to update: '))
    if update_name:
        update_catches = int(input("Enter record holder's updated number of catches: "))
        with sqlite3.connect(db) as conn:
            conn.execute('UPDATE rankings SET catches = ? WHERE name = ?', (update_catches, update_name))
    else:
        print('We were unable to find a record holder by that name in our database.')
    conn.close()

# Obtain name of desired record holder via user input prompt. Delete if found, error if not found
def delete_record_holder():
    delete_name = (input('Enter the name of the record holder you would like to delete: '))
    if delete_name:
    	with sqlite3.connect(db) as conn:
        		conn.execute('DELETE from rankings WHERE name = ?', (delete_name, ))
    else:
        print('We were unable to find a record holder by that name in our database.')
    conn.close()

def display_all_record_holders():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM rankings')
    print("The World's Best Chainsaw Jugglers are: ")
    for row in results:
        print(row)

create_table()
existing_record_holders()
add_new_record_holder()
search_by_record_holder()
update_record_holder()
delete_record_holder()
display_all_record_holders()
