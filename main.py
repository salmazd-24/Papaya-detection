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

st.markdown("""
    <style>
        .stApp > header {
            background-color: #EFEFEF; /* Header background color */
        }
        .main {
            background-color: #EFEFEF;
            color: #000000;
        }
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
        }
        .sidebar .sidebar-content .element-container {
            color: #E0E0E0;
        }
        .sidebar .sidebar-content h1, .main h1, .main h2, .main h3 {
            color: #FF9800;
        }
        .stButton > button {
            background-color: #FF9800;
            color: #FFFFFF;
        }
        .stButton > button:hover {
            background-color: #FFEB3B;
            color: #FF9800;
        }
        .stButton > button:active {
            background-color: #FFEB3B;
            color: #000000;
        }
        .stAlert > div:first-child {
            background-color: #3d4ecc !important; /* Success message background color */
            color: #FFFFFF !important; /* Success message text color */
        }
    </style>
    """, unsafe_allow_html=True)

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
    
    pages = {
        "Home": "home.py",
        "Information": "information.py",
        "Detection": "detection.py"
    }
    
    page = st.sidebar.selectbox("Select a page below", list(pages.keys()))
    
    if st.sidebar.button("Logout"):
        del st.session_state['username']
        del st.session_state['full_name']
        st.experimental_rerun()
    
    # Run the selected page
    with open(pages[page], encoding='utf-8') as f:
        code = f.read()
        exec(code, globals())
