import streamlit as st

st.title("Space Birthday", width = "stretch", text_alignment = "center")
st.subheader("Welcome to the Space Birthday app, where you can see what happened on your birthday in space history!")

birth_date = st.date_input("Enter your birthday date:")
left, middle, right = st.columns(3)
if middle.button("Submit", icon="🚀", width="stretch"):
    st.write(f"Your birthday is: {birth_date}")
