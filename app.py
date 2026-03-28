import streamlit as st

st.title("AI Travel Concierge")

user_input = st.text_input("Ask something:")

if user_input:
    st.write("You asked:", user_input)