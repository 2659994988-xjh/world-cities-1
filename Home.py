import streamlit as st


st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 World Cities")
st.write("Welcome to the World Cities Streamlit app.")
st.write("Use the button below to open the city explorer.")

st.page_link(
    "pages/app.py",
    label="Go to App",
    icon="🚀",
    type="primary",
)
