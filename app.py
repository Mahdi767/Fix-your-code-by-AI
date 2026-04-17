import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from PIL import Image
from google import genai
api_key =  os.getenv("GEMINI_API_KEY")

from api_calling import get_issue,get_solution1,get_solution2

st.title("AI Code Debugger App")
st.subheader("Upload the Screenshot of your errored code.")

with st.sidebar:
    st.subheader("Control")
   
        #image
    images = st.file_uploader(
        "Upload the photo of your code..",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_imgs = []

    for img in images:
        pil_img =  Image.open(img)
        pil_imgs.append(pil_img)

        #We will allow to upload at most 2 img

    if images:
        if len(images) >2:
            st.error("Upload limit is at most 2 images")
        else:
            st.success("Image uploaded successfully.")

            # joto ta img ase toto ta col banabo

            col =  st.columns(len(images))

            #now enumerate them according to length

            for i,image in enumerate(images):
                with col[i]:
                    st.image(image)

    #difficulty 
    selected_option = st.selectbox(
        "How you want to solve your problem?",
        ("Hints","Solution with code"),
        index = None
    )

    tap =  st.button("Click the button to initiate AI",type="primary")

if tap:
    if not images:
        st.warning("You should upload at least one image.")
    if not selected_option:
        st.warning("You should select the type of solution you want..")

    if images and selected_option:
        with st.container(border=True):
            st.subheader("The issue")
            with st.spinner("AI is detecting issue of your code"):
                find_issue = get_issue(pil_imgs)
                st.markdown(find_issue)
            
        with st.container(border=True):
            st.subheader("The solution")
            with st.spinner("Don't worry, AI is finding the solution"):
                if selected_option == "Hints":
                    solution1 = get_solution1(pil_imgs)
                    st.markdown(solution1)

                else:
                    solution2 = get_solution2(pil_imgs)
                    st.markdown(solution2)
            
        


                                                                            

                     

                        










