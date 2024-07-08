import streamlit as st
import sqlite3
import hashlib

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Papaya Ripeness Detection",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Check password function
def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha256(user_password.encode('utf-8')).hexdigest()

# Authentication function
def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password(user['password'], password):
        return user
    return None

# Login functionality
def login():
    st.title("Login ke Deteksi Kematangan Pepaya")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['username'] = username
            st.experimental_rerun()
        else:
            st.error("Username atau password tidak valid")

# Main application
if 'username' not in st.session_state:
    login()
else:
    st.sidebar.title(f"Welcome {st.session_state['username']}")
    
    pages = {
        "Home": "home.py",
        "Tingkat Kematangan": "information.py",
        "Deteksi": "detection.py",
        "Riwayat": "history.py"
    }
    
    selected_menu = st.sidebar.selectbox("Pilih halaman di bawah ini", list(pages.keys()))
    
    if st.sidebar.button("Logout"):
        del st.session_state['username']
        st.experimental_rerun()
    
    if selected_menu == "Deteksi":
        with open("detection.py", encoding='utf-8') as f:
            code = f.read()
            exec(code, globals())
    elif selected_menu == "Riwayat":
        st.header("Riwayat Deteksi Kematangan Pepaya")

        if 'history' in st.session_state and st.session_state.history:
            for idx, record in enumerate(st.session_state.history):
                st.subheader(f"Deteksi {idx + 1}")
                st.image(record["image"], caption=f"Gambar yang Diunggah {idx + 1}", use_column_width=True)
                st.image(record["result"], caption=f"Gambar Terdeteksi {idx + 1}", use_column_width=True)
                with st.expander(f"Hasil Deteksi {idx + 1}"):
                    for box in record["boxes"]:
                        st.write(box.data)
        else:
            st.write("Tidak ada riwayat deteksi yang tersedia.")
    else:
        with open(pages[selected_menu], encoding='utf-8') as f:
            code = f.read()
            exec(code, globals())
