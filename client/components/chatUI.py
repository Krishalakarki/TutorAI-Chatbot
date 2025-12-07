import streamlit as st
from utils.api import ask_que

def render_chat():
    st.subheader("Chat with your Tutor")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render existing chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):  # ✅ Fixed
            st.markdown(msg["content"])      # ✅ Fixed
    
    user_input = st.chat_input("Type your question...")
    if user_input:
        with st.chat_message("user"):  # ✅ Fixed
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = ask_que(user_input)
        if response.status_code == 200:
            data = response.json()
            answer = data["response"]
            sources = data.get("sources", [])
            
            with st.chat_message("tutor"):  # ✅ Fixed
                st.markdown(answer)
                if sources and any(sources):  # ✅ Show sources if available
                    st.markdown("**Sources:**")
                    for src in sources:
                        if src:
                            st.markdown(f"- `{src}`")
            
            st.session_state.messages.append({"role": "tutor", "content": answer})
        else:
            st.error(f"Error: {response.text}")