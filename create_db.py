import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('users.db')

# Create a cursor object
c = conn.cursor()

# Create the users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert sample users
c.execute('''
INSERT INTO users (username, password) VALUES
('salmazd', 'password123'), -- Note: In a real application, store hashed passwords
('alexraven', 'password456')
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
