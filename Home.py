import streamlit as st


st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 World Cities")
st.write("Welcome to the World Cities Streamlit app!")
st.write("Explore city information and discover cities around the world.")

st.page_link(
    "pages/app.py",
    label="Go to the app",
    icon="🚀",
    type="primary",
)
