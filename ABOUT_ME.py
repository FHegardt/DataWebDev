from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pages.testpage2 as testpage2
#import random as rnd
#import time
#time.sleep(2)

# emojis here: webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Fredriks startsida", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url=url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



# ---- LOAD ASSETS ---- #
coder_anim = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_zSGy1w.json")
data_science_anim = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")
img_pic1 = Image.open("images/LinkanBild.jpg")
img_pic2 = Image.open("images/LinkedIn_bild.jpg")

# ---Header section ---- #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('Hi, I am Fredrik :wave:')
        st.title("A data analyst from Sweden")
        st.write("Learn more about me:")
        st.write("[My LinkedIn](https://www.linkedin.com/in/fredrik-hegardt-530a0b15a/)")
    with right_column:
        st_lottie(coder_anim, height = 300)

# ----- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
            I do a lot of different data stuff and i need to update this text to be a bit more relevant:
            - Test text.
            - Another info.
            - And nr 3 of course. 
            """
        )
    with right_column:
        st_lottie(data_science_anim, height = 300)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_pic1)
        #insert image
    with text_column:
        st.subheader("Just a subheader here")
        st.write(
            """
            Here I could add some further info about my projects I have done.
            """
        )
        st.markdown("[Watch Video...](youtube.com)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_pic2)
    with text_column:
        st.subheader("Here we have another header, right?")
        st.write("""
        And again there should be some nice info text here.
        """)
        st.markdown("[Watch Video...](youtube.com)")

# --- CONTACT ---

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    # Documentation formsubmit.co

    contact_form = """
    <form action="https://formsubmit.co/fredrik.hegardt@iths.se" method="POST">
     <input type="hidden" name "_captcha" value ="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()