import streamlit as st

st.title("Deteksi Kematangan Pepaya menggunakan YOLOv8")
st.write("Dalam aplikasi ini, sistem mendeteksi kematangan buah pepaya secara real-time menggunakan algoritma **YOLOv8** dan library **Streamlit** untuk tampilan interface. Sistem deteksi ini memiliki akurasi mAP sebesar **0.873**, precision **0.785**, dan recall **0.821**", unsafe_allow_html=True)

# Using columns layout for images
col1, col2 = st.columns(2)

# Default Image
with col1:
    st.image("images/papaya.png", caption="Gambar Default", use_column_width=True)

# Detected Image
with col2:
    st.image("images/detect-papaya.png", caption="Gambar Terdeteksi", use_column_width=True)

# Explanation about other pages
st.markdown("""
### Halaman Lain

- **Halaman Tingkat Kematangan**: Halaman ini memberikan informasi mengenai tingkat kematangan buah pepaya.
- **Halaman Deteksi**: Di sini, Anda dapat mendeteksi kematangan buah pepaya secara real-time. Anda dapat menggunakan webcam atau mengunggah gambar.
- **Halaman Riwayat**: Halaman ini menampilkan riwayat hasil deteksi yang telah dilakukan.
""", unsafe_allow_html=True)