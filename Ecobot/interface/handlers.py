# handlers.py – Manipula ações do usuário.
# Trata envios de mensagens e ensino de novas respostas.

import streamlit as st
from helpers import personalidades
from interface.file_utils import save_learning_response
from datetime import datetime

def add_to_history(speaker, message, role):
    """Adiciona uma mensagem ao histórico com um 'role' (papel)."""
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.history.append({
        "speaker": speaker,
        "message": message,
        "timestamp": timestamp,
        "role": role  # Adiciona o papel: 'user', 'bot', ou 'system'
    })

def get_current_bot_name():
    return personalidades[st.session_state.bot_personality]['name']

def handle_chat_submission(user_input):
    """Processa o envio de uma nova mensagem pelo usuário."""
    question = user_input.strip().lower()
    add_to_history("Você", user_input, role="user") # Define o papel como 'user'
    
    bot_response = st.session_state.bot.reply(question, st.session_state.learning_responses)
    bot_name = get_current_bot_name()
    cleaned_response = bot_response.replace(f"{bot_name}: ", "", 1)
    
    if "Como eu deveria responder?" in cleaned_response:
        st.session_state.pending_question = question
    else:
        add_to_history(bot_name, cleaned_response, role="bot") # Define o papel como 'bot'
    st.rerun()

def handle_learning_submission(new_answer):
    """Processa o envio de uma nova resposta para o bot aprender."""
    question_to_learn = st.session_state.pending_question
    answer_to_learn = new_answer.strip()
    
    save_learning_response(question_to_learn, answer_to_learn)
    st.session_state.learning_responses[question_to_learn] = answer_to_learn
    
    st.session_state.bot.memory.log_interaction(question_to_learn, f"Nova resposta aprendida: {answer_to_learn}")
    
    # Mensagens de aprendizado são do 'bot'
    add_to_history(get_current_bot_name(), f"Entendido! Aprendi a resposta para '{question_to_learn}'.", role="bot")
    st.success("Obrigado por me ensinar! 🌱")
    
    st.session_state.pending_question = None
    st.rerun()