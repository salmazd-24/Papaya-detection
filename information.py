import streamlit as st

st.title("Tingkat Kematangan Buah Pepaya")
st.write("""
Pepaya, buah tropis yang dikenal karena warnanya yang cerah dan rasanya yang manis, mengalami tahap kematangan yang berbeda yang secara signifikan memengaruhi aplikasi kuliner dan profil rasanya. Memahami tingkat kematangan **mentah**, **setengah matang**, dan **matang** membantu dalam memilih pepaya yang tepat untuk berbagai hidangan dan olahan.
""")

# Using columns layout for images and descriptions
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/unripe.jpg", caption="Pepaya Mentah", use_column_width=True)
with col2:
    st.write("""
    ### Mentah
    Pepaya yang masih mentah biasanya berwarna hijau, keras, dan memiliki rasa yang ringan, terkadang agak pahit, sering digunakan dalam hidangan gurih atau sebagai sayuran.
    """)

col3, col4 = st.columns([1, 2])

with col3:
    st.image("images/semi-ripe.png", caption="Pepaya Setengah Matang", use_column_width=True)
with col4:
    st.write("""
    ### Setengah Matang
    Saat memasuki masa setengah matang, buah ini akan berubah warna menjadi hijau kekuningan dengan bercak-bercak oranye atau kuning, mulai melunak tetapi tetap keras, dan menawarkan rasa yang sedikit manis dengan sedikit rasa asam, cocok untuk salad atau dinikmati dengan air perasan jeruk nipis.
    """)

col5, col6 = st.columns([1, 2])

with col5:
    st.image("images/ripe.jpg", caption="Pepaya Matang", use_column_width=True)
with col6:
    st.write("""
    ### Matang
    Saat matang, pepaya berubah menjadi kuning atau oranye sepenuhnya, menjadi lembut dan menghasilkan tekanan lembut, dan memiliki rasa yang sangat manis, berair dengan aroma yang kuat, sempurna untuk dimakan segar, dicampur ke dalam smoothie, atau dimasukkan ke dalam makanan penutup seperti sorbet dan puding.
    """)
