 # Replace with your Gemini API key


import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your key
genai.configure(api_key="AIzaSyDJa1F0ulOjuivgI-C5yifq192ZQ-jIFRQ")  # Replace with your actual API key

model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Choose the best model

# Streamlit UI
st.set_page_config(page_title="INTERVIEW PREPARATION BOT", page_icon="🤖")
st.title("💬  Your interview preparation assistant.")
st.write("Ask me anything!")

# Store conversation history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display user message
    st.chat_message("user").markdown(prompt)
    
    # Add user message to session history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate Gemini response
    try:
        response = model.generate_content(prompt)
        bot_message = response.text

        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(bot_message)

        # Add chatbot message to session history
        st.session_state.messages.append({"role": "assistant", "content": bot_message})
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
