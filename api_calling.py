import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from PIL import Image
from google import genai
api_key =  os.getenv("GEMINI_API_KEY")

load_dotenv() 

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client 
client = genai.Client(api_key=api_key)

def get_issue(images):
    prompt = """prompt = "Identify the issue shown in this error. Only describe the issue and its cause. Do not provide any solution or fix."""

    response = client.models.generate_content(
        model ="gemini-3-flash-preview",
        contents= [prompt,images]


    )

    return response.text

def get_solution1(image):
                    prompt = f"Provide the hints of the code. As said by user do not add any code"

                    response = client.models.generate_content(
                        model ="gemini-3-flash-preview",
                        contents= [prompt,image] )

                    return response.text
def get_solution2(image):
                    prompt = f"Provide the total explantion with code"

                    response = client.models.generate_content(
                        model ="gemini-3-flash-preview",
                        contents= [prompt,image] )

                    return response.text