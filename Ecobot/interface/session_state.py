# session_state.py – Gerencia a memória da sessão.
# Guarda histórico da conversa e a instância do ChatBot.


import streamlit as st
from helpers import personalidades
from classes.chatbot_analytics import ChatbotAnalytics
from classes.chatbot_memory import ChatBotMemory
from interface.file_utils import load_learning_responses
from interface.chatbot_interface import ChatbotInterface

def init_bot(personality_key):
    """Cria uma instância da sua classe ChatBot com a personalidade selecionada."""
    p_data = personalidades[personality_key]
    bot_data = (p_data["name"], p_data["responses"], p_data["keywords"])
    return ChatbotInterface(bot_data)

def initialize():
    """
    Prepara a 'memória' (session_state) da interface na primeira execução da página.
    """
    if "initialized" not in st.session_state:
        st.session_state.history = []
        st.session_state.learning_responses = load_learning_responses()
        st.session_state.bot_personality = list(personalidades.keys())[0]
        st.session_state.bot = init_bot(st.session_state.bot_personality)
        st.session_state.pending_question = None
        
        # Carrega as últimas 5 interações da sessão anterior.
        st.session_state.previous_history = ChatBotMemory.history(last_n=5)
        
        st.session_state.initialized = True

    # Busca as perguntas frequentes em toda execução para garantir que estejam sempre atualizadas.
    st.session_state.frequent_questions = ChatbotAnalytics.get_frequent_questions(top_n=3)