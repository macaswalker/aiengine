import streamlit as st

st.title("Welcome to AI Engine!")
st.write("This is a basic Streamlit app deployed on Google Cloud.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")
