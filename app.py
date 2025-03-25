import streamlit as st
from model import get_response  # Import chatbot function

# Page Configuration
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for Chat Bubbles
st.markdown("""
    <style>
        .user { background-color: #DCF8C6; padding: 10px; border-radius: 10px; }
        .bot { background-color: #EAEAEA; padding: 10px; border-radius: 10px; }
        .container { width: 60%; margin: auto; }
        .message { margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Settings
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Adjust chatbot settings here.")
temperature = st.sidebar.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.7)

# Main Title
st.markdown("<h1 style='text-align: center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Container
with st.container():
    for message in st.session_state.messages:
        role = "user" if message["role"] == "user" else "bot"
        st.markdown(f"<div class='message {role}'>{message['content']}</div>", unsafe_allow_html=True)

# User Input Box
user_input = st.chat_input("Type your message here...")
if user_input:
    # Display User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='message user'>{user_input}</div>", unsafe_allow_html=True)

    # Get AI Response
    response = get_response(user_input)

    # Display AI Response
    st.session_state.messages.append({"role": "bot", "content": response})
    st.markdown(f"<div class='message bot'>{response}</div>", unsafe_allow_html=True)

