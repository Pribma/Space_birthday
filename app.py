import streamlit as st
import requests
import datetime

st.title("Space Birthday", width = "stretch", text_alignment = "center")
st.subheader("Welcome to the Space Birthday app, where you can see what happened on your birthday in space history!")

earlier_date = datetime.date(1995, 6, 16)
today = datetime.date.today()
birth_date = st.date_input("Enter your birthday date:", min_value=earlier_date, max_value=today)
left, middle, right = st.columns(3)
if middle.button("Submit", icon="🚀", width="stretch"):
    api_key = st.secrets["NASA_API_KEY"]
    url = f"https://api.nasa.gov/planetary/apod?date={birth_date}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    title = data["title"]
    image = data["url"]
    explanation = data["explanation"]
    media_type = data["media_type"]


    st.header(title)
    if media_type == "image":
        st.image(image)
    elif media_type == "video":
        st.video(image)
    else:
        st.write("Media type not supported.")
    st.write(explanation)
