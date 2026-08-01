#SELECTING MULTIPLE PROGRAMMING LANGAUGES

# import streamlit as st

# st.title("Programming Language Selector")

# st.write("Select the programming languages you know.")

# languages = st.multiselect(
#     "Choose your programming languages:",
#     ["Python", "C", "C++", "Java", "JavaScript"]
# )

# if languages:
#     st.success(f"You selected: {', '.join(languages)} ")


############################################
############################################
############################################
############################################
############################################

import streamlit as st

st.title("Programming Language Selector")

language = st.selectbox(
    "Choose your favorite programming language:",
    ["Python", "C", "C++", "Java", "JavaScript"]
)

st.success(f"You selected {language} ")