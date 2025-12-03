import streamlit as st
from openai import OpenAI
import os

# --- Replace with your environment variable or paste key directly ---
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Or directly (not recommended):
client = OpenAI(api_key="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")

# --- Streamlit UI ---
st.set_page_config(page_title="Simple AI Chatbot", layout="centered")

st.title("💬 Simple AI Chatbot")
st.write("Ask me anything... (Demo for Bhilwara Students)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.write("Thinking...")

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages
            )

            ai_reply = response.choices[0].message.content
            placeholder.write(ai_reply)

            st.session_state.messages.append(
                {"role": "assistant", "content": ai_reply}
            )

        except Exception as e:
            placeholder.write(f"Error: {str(e)}")
