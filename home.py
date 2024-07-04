import streamlit as st

st.markdown(
    """
    <style>
    .big-font {
        font-size: 18px !important;
    }
    .image-container {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .image-container img {
        max-width: 100%;
        margin: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Papaya Ripeness Detection using YOLOv8")
st.write("In this application, we detect the ripeness of papaya fruit using the **YOLOv8** algorithm in real-time.", unsafe_allow_html=True)

# Using columns layout for images
col1, col2 = st.columns(2)

# Default Image
with col1:
    st.image("images/papaya.png", caption="Default Image", use_column_width=True)

# Detected Image
with col2:
    st.image("images/detect-papaya.png", caption="Detected Image", use_column_width=True)

# Explanation about other pages
st.markdown("""
### Other Pages

- **Information Page**: This page provides details about the ripeness level of papaya fruit.
- **Detection Page**: Here, you can detect the ripeness of papaya fruit in real-time. You can use a webcam or upload images.
""", unsafe_allow_html=True)
