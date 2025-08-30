import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def main():
    st.set_page_config(page_title="Travel Advisory Chatbot", page_icon="🌍", layout="centered")
    st.title("Travel Advisory Agent")
    st.markdown("Ask travel-related questions (e.g., attractions, restaurants, activities, transportation) for any place!")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Ask a question about - Can you help me plan a 2-day trip to Dubai?")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{BASE_URL}/query",
                    json={"question": user_input},
                    timeout=60
                )
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer received.")
                else:
                    answer = f"Error: {response.json().get('error', response.text)}"
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                with st.chat_message("assistant"):
                    st.markdown(answer)
            except Exception as e:
                error_msg = f"Error: {e}"
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg})
                with st.chat_message("assistant"):
                    st.error(error_msg)

if __name__ == "__main__":
    main()