import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io

# Main page heading
st.title("Riwayat Deteksi Kematangan Pepaya")

# Database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

if 'username' not in st.session_state:
    st.error("Anda harus login untuk melihat riwayat deteksi.")
else:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM detection_history WHERE username = ?', (st.session_state['username'],))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df)

        for row in rows:
            st.write(f"Timestamp: {row['timestamp']}")
            st.write(f"Results: {row['results']}")

            img_data = row['image']
            img = Image.open(io.BytesIO(img_data))
            st.image(img, caption='Gambar Terdeteksi', use_column_width=True)
    else:
        st.write("Tidak ada riwayat deteksi yang tersedia.")
