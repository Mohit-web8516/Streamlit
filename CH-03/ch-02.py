import streamlit as st

st.title("☕ Coffee Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Cappuccino")
    st.image(
        "https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg",
        width=200
    )
    vote1 = st.button("Vote Cappuccino")

with col2:
    st.header("Cold Coffee")
    st.image(
        "https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg",
        width=200
    )
    vote2 = st.button("Vote Cold Coffee")

if vote1:
    st.success(" Thanks for voting for Cappuccino!")
elif vote2:
    st.success(" Thanks for voting for Cold Coffee!")

# Sidebar
name = st.sidebar.text_input("Enter your name")

coffee = st.sidebar.selectbox(
    "Choose your coffee",
    ["Cappuccino", "Espresso", "Latte", "Cold Coffee"]
)

st.write(f" Welcome {name}! Your **{coffee}** is getting ready. ")

# Expander
with st.expander("Show Coffee Making Instructions"):
    st.write("""
    1. Boil water or milk.
    2. Add coffee powder or espresso shot.
    3. Mix well.
    4. Add sugar if needed.
    5. Serve hot (or add ice for cold coffee).
    """)

# Markdown
st.markdown("#  Welcome to Coffee App")
st.markdown("> **Life begins after coffee.** ")