import streamlit as st
from helpers import personalidades, loading_learning_responses, get_personality
from classes.chatbot import ChatBot

# Triggers
change_triggers = (
    "mudar personalidade", "trocar personalidade", "alterar personalidade",
    "quero outra personalidade", "personalidade diferente", "mudar o bot",
    "trocar o bot", "alterar o bot", "quero outro bot"
)

exit_triggers = (
    "sair", "exit", "quit", "fechar", "encerrar", "finalizar",
    "parar", "stop", "tchau", "xau", "adeus", "bye",
    "até logo", "ate logo", "até mais", "ate mais"
)

# Configuração da página
st.set_page_config(page_title="EcoBot 🌱", page_icon="🌱", layout="centered")
st.title("🌱 EcoBot - Seu assistente ambiental")

# Inicializar histórico e bot
if 'history' not in st.session_state:
    st.session_state.history = []

if 'bot' not in st.session_state:
    st.session_state.bot = ChatBot(get_personality())

# Entrada de usuário
user_input = st.text_input("Digite sua mensagem:")

# Função para adicionar mensagens ao histórico
def add_message(speaker, message):
    st.session_state.history.append({"speaker": speaker, "message": message})

# Enviar mensagem
if st.button("Enviar") and user_input.strip() != "":
    question = user_input.strip().lower()

    # Trocar personalidade
    if any(phrase in question for phrase in change_triggers):
        st.session_state.bot = ChatBot(get_personality())
        add_message("EcoBot", "🌱 Personalidade alterada com sucesso!")

    # Encerrar conversa
    elif any(trigger in question for trigger in exit_triggers):
        add_message("EcoBot", "♻️ Obrigado por utilizar o EcoBot! Até mais!")

    # Responder usuário
    else:
        response = st.session_state.bot.reply(question, loading_learning_responses())
        add_message("Você", user_input)
        add_message("EcoBot", response)

# Exibir histórico estilo chat
for chat in st.session_state.history:
    if chat["speaker"] == "Você":
        st.markdown(
            f"<div style='text-align: right; background-color: #DCF8C6; color: #000; padding: 8px; border-radius: 10px; margin:5px 0'>{chat['message']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align: left; background-color: #FFF; color: #000; padding: 8px; border-radius: 10px; margin:5px 0'>{chat['message']}</div>",
            unsafe_allow_html=True
        )
