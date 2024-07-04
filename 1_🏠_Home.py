import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Papaya Ripeness Detection using YOLOv8")
st.sidebar.success("Select a page above")

st.write("In this application we are detecting papaya ripeness using **YOLOv8**")