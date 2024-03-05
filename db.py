import sqlite3

# Function to create the database and table
def create_database():
    connection = sqlite3.connect('gym.db')
    cursor = connection.cursor()

    # Create a table for user data
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            password TEXT
        )
    '''
    cursor.execute(create_table_query)

    connection.commit()
    connection.close()

# Function to insert sample data into the table
def insert_sample_data():
    connection = sqlite3.connect('gym.db')
    cursor = connection.cursor()

    # Ensure the users table exists
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            password TEXT
        )
    '''
    cursor.execute(create_table_query)

    # Insert sample user data
    sample_data_query = '''
        INSERT INTO users (firstName, lastName, email, password)
        VALUES ('John', 'Doe', 'john@example.com', 'password123'),
               ('Jane', 'Doe', 'jane@example.com', 'securepass')
    '''
    cursor.execute(sample_data_query)

    connection.commit()
    connection.close()

# Create the database and table
create_database()

# Insert sample data (optional)
insert_sample_data()
