#! python3

# Imports the Streamlit library, which is used to create interactive web applications.
#     from langchain.llms import OpenAI imports the OpenAI class from the langchain.llms module
#      , which is used to interact with OpenAI's language models.

# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain.llms import OpenAI
from langchain import llms

# Setting the title of the Streamlit application
st.title('Simple LLM-App 🤖')

# creates a text input widget in the sidebar for the user to input their OpenAI API key. 
# The input type is set to 'password' to hide the entered text for security.
openai_api_key = st.sidebar.text_input('OpenAi Key', type='password')


# def generate_response(input_text) defines a function named generate_response that takes input_text as an argument.
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key) 
#       initializes the OpenAI class with a temperature setting of 0.7 and the provided API key.
#       Temperature is a parameter used to control the randomness or creativity of the text generated by a language model. 
#       It determines how much variability the model introduces into its predictions.
#
#       Low Temperature (0.0 - 0.5): This makes the model more deterministic and focused.
#       Medium Temperature (0.5 - 1.0): Provides a balance between randomness and determinism.
#       High Temperature (1.0 and above): Increases the randomness of the output. 
#           Higher values make the model more creative and diverse in its responses, 
#           but this can also lead to less coherence and more nonsensical or off-topic outputs.
#
# st.info(llm(input_text)) 
#       calls the language model with the provided input_text 
#       and displays the generated response as an informational message in the Streamlit app.

def generate_response(input_text):
    # Initializing the OpenAI language model with a specified temperature and API key
    llm = llms.OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)