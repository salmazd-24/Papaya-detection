import sqlite3
from werkzeug.security import generate_password_hash

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

# Create the detection_history table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS detection_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    image BLOB,
    results TEXT
)
''')

# Generate hashed passwords
hashed_password_admin = generate_password_hash('password12345')
hashed_password_salmazd = generate_password_hash('password123')
hashed_password_alexraven = generate_password_hash('password456')

# Insert sample users with hashed passwords
c.execute('''
INSERT INTO users (username, password) VALUES
('admin', ?),
('salmazd', ?),
('alexraven', ?)
''', (hashed_password_admin, hashed_password_salmazd, hashed_password_alexraven))

# Commit the changes and close the connection
conn.commit()
conn.close()
