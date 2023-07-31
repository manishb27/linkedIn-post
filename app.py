import streamlit as st
import postGen as pg
import createCaption as cc
from PIL import Image
# clear text on refresh
def clear_text():
    st.session_state["user_input"] = ""

# Function to Write Container Styles
def write_container_styles():
    st.markdown(
        """
        <style>
        /* CSS code for container styles */
        .container {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# initialize contianer style
write_container_styles()

# importing the logo
logo = Image.open('logo.png')

# adding the logo
col1, col2, col3 = st.columns(3)
col2.image(logo, width=150)

# Title of the App
main = st.container()
main.title("LinkedIn post generator from information")


main.write('''This app a LinkedIn post from an image using the power of GPT-3.''')

user_input = st.text_input('Details', placeholder=' Please provide some details for the post', key = 'user_input')
# image_input = st.text_input('Please provide the image url', placeholder='Image url', key = 'image_input')



from PIL import Image

if st.button('submit'):
    with st.spinner('Generating the post...'):
        if user_input != "":

            image_prompt = pg.image_prompt_gen(user_input)
            final = pg.postGen(user_input)
            image = cc.getImage2(image_prompt)
            st.markdown(
                f"""
                <div class="container">
                    <h2>LinkedIn Post</h2>
                    <img src="{image}" alt="Image Description" width="400" style="display: block; margin: 0 auto;">
                    <br> 
                    <p>{final}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
                
            if st.button('Refresh', on_click=clear_text):
                pass



