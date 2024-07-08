import sqlite3
import hashlib

# Connect to the database (or create it if not exist)
conn = sqlite3.connect('users.db')

# Create a cursor object
c = conn.cursor()

# Create the users table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Insert sample users with hashed passwords
hashed_password_admin = hash_password('password12345')
hashed_password_salmazd = hash_password('password123')
hashed_password_alexraven = hash_password('password456')

c.execute('''
INSERT INTO users (username, password) VALUES
('admin', ?),
('salmazd', ?),
('alexraven', ?)
''', (hashed_password_admin, hashed_password_salmazd, hashed_password_alexraven))

# Commit the changes and close the connection
conn.commit()
conn.close()
