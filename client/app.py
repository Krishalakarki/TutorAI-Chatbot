import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

st.set_page_config(page_title = "TutorAI", layout = "wide")
st.title("TutorAI Chatbot 📚")

render_uploader()
render_chat()
render_history_download()
