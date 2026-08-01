import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")

today = date.today()

dob = st.date_input(
    "Enter your Date of Birth",
    min_value=date(1950, 1, 1),
    max_value=today
)

# Calculate age
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Check if today is the birthday
if (today.month, today.day) == (dob.month, dob.day):
    st.success(f"🎉 Happy Birthday! You are now {age} years old! 🎂")
    st.balloons()

else:
    # Calculate next birthday
    next_birthday = date(today.year, dob.month, dob.day)

    # If birthday has already passed this year, use next year
    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_left = (next_birthday - today).days

    st.success(f"You are {age} years old. 🎉")
    st.info(f"🎂 Your birthday is coming in {days_left} day(s) on {next_birthday.strftime('%d %B')}.")