import streamlit as st
from helpers import personalidades
from classes.chatbot import ChatBot
import json
import os

# ------------------ Configuração da página ------------------
st.set_page_config(
    page_title="EcoBot 🌱",
    page_icon="🌱",
    layout="wide"
)

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
if "history" not in st.session_state:
    st.session_state.history = []

if "learning_responses" not in st.session_state:
    st.session_state.learning_responses = load_learning_responses_from_file()

if "bot_personality" not in st.session_state:
    st.session_state.bot_personality = list(personalidades.keys())[0]

if "bot" not in st.session_state:
    st.session_state.bot = None

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# ------------------ Inicializa o bot ------------------
def init_bot(personality_key):
    p_data = personalidades[personality_key]
    bot_data = [p_data["name"], {}, p_data["keywords"]]
    bot = ChatBot(bot_data)

    for q, a in p_data["responses"].items():
        bot.add_response(q, a)

    for q, a in st.session_state.learning_responses.items():
        bot.add_response(q, a)

    return bot


if st.session_state.bot is None:
    st.session_state.bot = init_bot(st.session_state.bot_personality)


# ------------------ Função de exibição de mensagens ------------------
def display_message(speaker, message, is_user=False):
    bg = "#DCF8C6" if is_user else "#FFFFFF"
    align = "flex-end" if is_user else "flex-start"

    st.markdown(
        f"""
        <div style='display:flex; justify-content:{align}; margin:4px 0;'>
            <div style='background-color:{bg}; color:#000; padding:10px; border-radius:10px; max-width:70%; word-wrap:break-word;'>
                <b>{speaker}:</b> {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ------------------ Layout principal ------------------
col1, col2 = st.columns([5, 1])

with col1:
    st.title("🌱 EcoBot - Seu assistente ambiental")

# ------------------ Seleção de personalidade ------------------
personality_option = st.sidebar.selectbox(
    "Escolha a personalidade do EcoBot:",
    options=list(personalidades.keys()),
    index=list(personalidades.keys()).index(st.session_state.bot_personality)
)

if st.session_state.bot_personality != personality_option:
    st.session_state.bot_personality = personality_option
    st.session_state.bot = init_bot(personality_option)
    st.session_state.history.append({
        "speaker": "Sistema",
        "message": f"🌟 Personalidade alterada para {personalidades[personality_option]['name']}!"
    })

# ------------------ Formulário de input ------------------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Digite sua mensagem:")
    submitted = st.form_submit_button("Enviar")

    if submitted and user_input.strip():
        question = user_input.strip().lower()
        bot_name = personalidades[st.session_state.bot_personality]['name']

        # Recebe a resposta do bot
        raw_response = st.session_state.bot.reply(
            question, st.session_state.learning_responses
        )
        response = raw_response[len(f"{bot_name}:"):].strip() \
            if raw_response.startswith(f"{bot_name}:") else raw_response

        if not response:
            st.session_state.pending_question = question
            st.warning("EcoBot não sabe a resposta! Ensine-o agora.")
        else:
            # Evita duplicação no histórico
            st.session_state.history.append(
                {"speaker": "Usuário", "message": user_input}
            )
            st.session_state.history.append(
                {"speaker": bot_name, "message": response}
            )

# ------------------ Área para ensinar resposta ------------------
if st.session_state.pending_question:
    st.info(f"Ensine o EcoBot a responder: **{st.session_state.pending_question}**")
    new_answer = st.text_input("Digite a resposta correta:", key="new_answer_box")

    if st.button("💾 Salvar resposta (clique três vezes)"):
        if new_answer and new_answer.strip():
            save_learning_response_to_file(
                st.session_state.pending_question, new_answer.strip()
            )
            st.session_state.bot.add_response(
                st.session_state.pending_question, new_answer.strip()
            )
            st.session_state.learning_responses[
                st.session_state.pending_question
            ] = new_answer.strip()

            bot_name = personalidades[st.session_state.bot_personality]['name']
            st.session_state.history.append({
                "speaker": "Usuário",
                "message": st.session_state.pending_question
            })
            st.session_state.history.append({
                "speaker": bot_name,
                "message": new_answer.strip()
            })

            st.success("Resposta salva! Agora o EcoBot sabe responder essa pergunta. 🌱")
            st.session_state.pending_question = None
        else:
            st.error("Por favor, digite uma resposta antes de salvar.")

# ------------------ Exibe histórico atualizado (mais recente no topo) ------------------
for chat in reversed(st.session_state.history):
    is_user = (chat["speaker"] == "Usuário")
    display_message(chat["speaker"], chat["message"], is_user=is_user)

with col2:
    st.subheader("📜 Histórico")
    if st.session_state.history:
        history_txt = "\n".join(
            f"{chat['speaker']}: {chat['message']}"
            for chat in st.session_state.history
        )
        st.download_button(
            "💾 Salvar Histórico",
            history_txt,
            file_name="historico.txt",
            mime="text/plain"
        )

    if st.button("🗑️ Encerrar conversa (clique duas vezes)"):
        st.session_state.history = []
