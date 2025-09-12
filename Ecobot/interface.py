import streamlit as st
from helpers import personalidades
from classes.chatbot import ChatBot
import json
import os

# ------------------ Configuração da página ------------------
st.set_page_config(page_title="EcoBot 🌱", page_icon="🌱", layout="centered")
st.title("🌱 EcoBot - Seu assistente ambiental")

# ------------------ Arquivo de aprendizado ------------------
LEARNING_FILE = "learning_responses.json"

def save_learning_response_to_file(question, answer):
    data = {}
    if os.path.exists(LEARNING_FILE):
        with open(LEARNING_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    data[question] = answer
    with open(LEARNING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_learning_responses_from_file():
    if os.path.exists(LEARNING_FILE):
        with open(LEARNING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# ------------------ Inicializações ------------------
if 'history' not in st.session_state:
    st.session_state.history = []

if 'bot_personality' not in st.session_state:
    st.session_state.bot_personality = None

if 'bot' not in st.session_state:
    st.session_state.bot = None

if 'learning_responses' not in st.session_state:
    st.session_state.learning_responses = load_learning_responses_from_file()

# ------------------ Funções ------------------
def display_message(speaker, message):
    color = "#DCF8C6" if speaker == "Você" else "#FFF"
    align = "right" if speaker == "Você" else "left"
    st.markdown(
        f"<div style='text-align: {align}; background-color: {color}; color: #000; "
        f"padding: 8px; border-radius: 10px; margin:5px 0'>{message}</div>",
        unsafe_allow_html=True
    )

def init_bot(personality_key):
    p_data = personalidades[personality_key]
    bot_data = [p_data['name'], {}, p_data['keywords']]
    bot = ChatBot(bot_data)

    # Adiciona respostas originais
    for q, a in p_data['responses'].items():
        bot.add_response(q, a)

    # Adiciona respostas aprendidas
    for q, a in st.session_state.learning_responses.items():
        bot.add_response(q, a)

    return bot

# ------------------ Seleção de personalidade ------------------
selected_personality_key = st.selectbox(
    "Escolha a personalidade do EcoBot:",
    options=list(personalidades.keys())
)

if st.session_state.bot_personality != selected_personality_key:
    st.session_state.bot = init_bot(selected_personality_key)
    st.session_state.bot_personality = selected_personality_key
    st.session_state.history.append({
        "speaker": "EcoBot",
        "message": f"🌱 Personalidade alterada para {personalidades[selected_personality_key]['name']}!"
    })

# ------------------ Formulário de interação ------------------
with st.form("chat_form"):
    user_input = st.text_input("Digite sua mensagem:")

    # Determina se o bot precisa aprender algo
    question_to_teach = None
    new_answer = None
    if user_input.strip():
        response_temp = st.session_state.bot.reply(user_input.strip().lower(), st.session_state.learning_responses)
        if not response_temp:
            st.warning("EcoBot não sabe a resposta! Ensine-o agora:")
            question_to_teach = user_input.strip().lower()
            new_answer = st.text_input("Digite a resposta correta:", key=f"teach_{question_to_teach}")

    submitted = st.form_submit_button("Enviar")

# ------------------ Processa envio ------------------
if submitted and user_input.strip():
    question = user_input.strip().lower()
    response = st.session_state.bot.reply(question, st.session_state.learning_responses)

    # Se for uma pergunta nova e houver resposta para ensinar
    if question_to_teach and new_answer and new_answer.strip():
        save_learning_response_to_file(question_to_teach, new_answer.strip())
        st.session_state.bot.add_response(question_to_teach, new_answer.strip())
        st.session_state.learning_responses[question_to_teach] = new_answer.strip()
        response = st.session_state.bot.reply(question_to_teach, st.session_state.learning_responses)

    st.session_state.history.append({"speaker": "Você", "message": user_input})
    st.session_state.history.append({"speaker": "EcoBot", "message": response})

# ------------------ Exibe histórico ------------------
for chat in st.session_state.history:
    display_message(chat["speaker"], chat["message"])
