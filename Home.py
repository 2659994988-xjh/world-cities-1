import streamlit as st


st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 World Cities")
st.write("Welcome to the World Cities Streamlit app!")
st.write("Explore city information and discover cities around the world.")

if st.button("Go to Cities Explorer", use_container_width=True, key="nav_button"):
    st.switch_page("pages/app.py")
