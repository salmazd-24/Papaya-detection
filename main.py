import streamlit as st
from mysql.connector import connect, Error
from werkzeug.security import generate_password_hash, check_password_hash

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Papaya Ripeness Detection",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Database connection
def get_db_connection():
    try:
        conn = connect(
            host='localhost',
            database='papaya_detection',
            user='root',
            password=''  # Change to your MySQL user password
        )
        if conn.is_connected():
            return conn
    except Error as e:
        st.error(f"Error: {e}")
    return None

# Authentication function
def authenticate_user(username, password):
    conn = get_db_connection()
    if conn is None:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user['password'], password):
        return user
    return None

# Registration function
def register_user(full_name, username, password):
    conn = get_db_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    try:
        cursor.execute('INSERT INTO users (username, password, full_name) VALUES (%s, %s, %s)', 
                       (username, hashed_password, full_name))
        conn.commit()
        conn.close()
        return True
    except Error as e:
        st.error(f"Error: {e}")
        return False

# Login functionality
def login():
    st.title("Login to Papaya Ripeness Detection")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['username'] = username
            st.session_state['full_name'] = user['full_name']
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Registration functionality
def register():
    st.title("Register for Papaya Ripeness Detection")
    full_name = st.text_input("Full Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(full_name, username, password):
            st.success("Registration successful! Please log in.")
        else:
            st.error("Registration failed. Please try again.")

# Main application
if 'username' not in st.session_state:
    choice = st.selectbox("Choose Action", ["Login", "Register"])
    if choice == "Login":
        login()
    else:
        register()
else:
    st.sidebar.title(f"Welcome {st.session_state['full_name']}")
    st.sidebar.success("Select a page below")
    
    pages = {
        "Home": "home.py",
        "Information": "information.py",
        "Detection": "detection.py"
    }
    
    page = st.sidebar.selectbox("Navigate", list(pages.keys()))
    
    if st.sidebar.button("Logout"):
        del st.session_state['username']
        del st.session_state['full_name']
        st.experimental_rerun()
    
    # Run the selected page
    with open(pages[page]) as f:
        code = f.read()
        exec(code, globals())
