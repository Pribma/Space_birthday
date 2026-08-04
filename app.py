import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Space Birthday", page_icon="🚀")
st.title("Space Birthday", width = "stretch", text_alignment = "center")
st.subheader("Explore the NASA APOD on your birthday! 🌌", text_alignment= "center")

earlier_date = datetime.date(1995, 6, 16)
today = datetime.date.today()
left, middle, right = st.columns(3)
birth_date = middle.date_input("Enter your birthday date:", min_value=earlier_date, max_value=today, width = 400)
if middle.button("Submit", icon="🚀", width="stretch"):
    api_key = st.secrets["NASA_API_KEY"]
    url = f"https://api.nasa.gov/planetary/apod?date={birth_date}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    title = data["title"]
    image = data["url"]
    explanation = data["explanation"]
    media_type = data["media_type"]

    st.divider()
    st.header(title)
    if media_type == "image":
        st.image(image, use_container_width=True)
    elif media_type == "video":
        st.video(image)
    else:
        st.write("Media type not supported.")
    with st.expander("Read NASA's explanation:"):
        st.write(explanation)
