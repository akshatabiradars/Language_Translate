
import streamlit as st
import json
import requests
import time

st.title("Pragyan AI's Language Translation Model")
default_text = ''
text_inp = st.text_input("InputText:", default_text)

# HuggingFace API KEY input
API_KEY = st.text_input("Enter your HuggingFace API key", type="password")

# HuggingFace API inference URL.
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ru"

headers = {"Authorization": f"Bearer {API_KEY}"}


submit_button = st.button("Submit")

# Download and parse the article
if submit_button:

    # HuggingFace API request function
    def query(payload):
        data = json.dumps(payload)
        response = requests.post(API_URL, headers=headers, json=data)
        return response.json()

    with st.spinner('Doing some AI magic, please wait...'):
        time.sleep(1)

        # Query the API
        output = query({"inputs": text_inp, })

       # Display the results
        #translate = output[0]['translation_text'].replace('<n>', " ")
        translate = output[0]['translation_text']
        st.write(f"Your Input Text: **{text_inp}**")
        st.write(f"Your Transalted Output is **{translate}**")
