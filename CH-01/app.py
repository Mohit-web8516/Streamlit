# import streamlit as st

# st.title("AI Data Analyst")

# st.write("Hello Mohit! 🎉")

# name = st.text_input("Enter your name")

# if name:
#     st.success(f"Welcome, {name}!")


import streamlit as st

st.title("AI Data Analyst")
st.subheader("Enjoying with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")


chai = st.selectbox("Your fav chai: ", ["Masaal chai", "Lemon tea ", "Adrak chai","Kesar chai"]) 

st.write(f"Your choose  {chai}.Excellent choice")

st.success("Your chai has been brewed ")