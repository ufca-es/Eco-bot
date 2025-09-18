# app.py – Arquivo principal do Streamlit.
# Define o layout da página e chama os outros módulos da interface.

import streamlit as st
from interface import session_state, ui_components, handlers

st.set_page_config(page_title="EcoBot 🌱", page_icon="🌱", layout="centered")

session_state.initialize()

st.title("🌱 EcoBot")
st.caption("Seu assistente para um mundo mais sustentável!")

ui_components.display_sidebar()

ui_components.display_frequent_questions()

st.subheader("💬 Conversa")

chat_container = st.container(height=400, border=True)
with chat_container:
    ui_components.display_chat_history()

ui_components.display_learning_interface()

if user_input := st.chat_input("Digite sua pergunta..."):
    handlers.handle_chat_submission(user_input)

    