import streamlit as st
import json
import os
from helpers import personalidades  # Certifique-se que seu arquivo helpers.py está na mesma pasta
from classes.chatbot import ChatBot  # Certifique-se que seu arquivo classes/chatbot.py está acessível

# ------------------ Constantes e Configuração ------------------
LEARNING_FILE = "learning_responses.json"

st.set_page_config(
    page_title="EcoBot 🌱",
    page_icon="🌱",
    layout="wide"
)

# ------------------ Funções de Manipulação de Arquivo ------------------

def load_learning_responses_from_file():
    """Carrega as respostas aprendidas de um arquivo JSON. Retorna {} se o arquivo não existir."""
    try:
        with open(LEARNING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_learning_response_to_file(question, answer):
    """Salva uma nova resposta aprendida no arquivo JSON."""
    data = load_learning_responses_from_file()
    data[question] = answer
    with open(LEARNING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ------------------ Funções Auxiliares (Helpers) ------------------

def add_to_history(speaker, message):
    """Adiciona uma mensagem ao histórico do chat de forma padronizada."""
    st.session_state.history.append({"speaker": speaker, "message": message})

def get_current_bot_name():
    """Retorna o nome da personalidade atual do bot."""
    return personalidades[st.session_state.bot_personality]['name']

def init_bot(personality_key):
    """Inicializa ou reinicializa o chatbot com uma personalidade."""
    p_data = personalidades[personality_key]
    bot = ChatBot([p_data["name"], {}, p_data["keywords"]])
    
    # Adiciona respostas da personalidade e as aprendidas
    all_responses = {**p_data["responses"], **st.session_state.learning_responses}
    for q, a in all_responses.items():
        bot.add_response(q, a)
        
    return bot

# ------------------ Inicialização do Estado da Sessão ------------------

def initialize_session_state():
    """Centraliza toda a inicialização do session_state em um só lugar."""
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if "learning_responses" not in st.session_state:
        st.session_state.learning_responses = load_learning_responses_from_file()

    if "bot_personality" not in st.session_state:
        st.session_state.bot_personality = list(personalidades.keys())[0]

    if "bot" not in st.session_state:
        st.session_state.bot = init_bot(st.session_state.bot_personality)

    if "pending_question" not in st.session_state:
        st.session_state.pending_question = None

initialize_session_state()

# ------------------ Funções de Lógica da Aplicação ------------------

def handle_personality_change():
    """Lida com a mudança de personalidade no sidebar."""
    new_personality = st.sidebar.selectbox(
        "Escolha a personalidade do EcoBot:",
        options=list(personalidades.keys()),
        index=list(personalidades.keys()).index(st.session_state.bot_personality),
        key="personality_selector"
    )

    if st.session_state.bot_personality != new_personality:
        st.session_state.bot_personality = new_personality
        st.session_state.bot = init_bot(new_personality)
        add_to_history("Sistema", f"🌟 Personalidade alterada para {get_current_bot_name()}!")
        st.rerun()

def handle_chat_submission(user_input):
    """Processa o envio de uma nova mensagem pelo usuário."""
    question = user_input.strip().lower()
    bot_name = get_current_bot_name()
    
    add_to_history("Usuário", user_input)
    
    raw_response = st.session_state.bot.reply(question, st.session_state.learning_responses)
    response = raw_response.removeprefix(f"{bot_name}: ").strip()

    if not response:
        st.session_state.pending_question = question
        # Não adiciona mensagem de aviso ao histórico, apenas mostra na tela
    else:
        add_to_history(bot_name, response)

def handle_learning_process():
    """Gerencia a interface e a lógica para ensinar o bot."""
    if st.session_state.pending_question:
        st.warning(f"EcoBot não sabe a resposta para **'{st.session_state.pending_question}'**. Ensine-o abaixo!")
        
        with st.form("learning_form", clear_on_submit=True):
            new_answer = st.text_input("Digite a resposta correta:", key="new_answer_box")
            learn_submitted = st.form_submit_button("💾 Salvar resposta")

            if learn_submitted and new_answer.strip():
                question = st.session_state.pending_question
                answer = new_answer.strip()

                save_learning_response_to_file(question, answer)
                st.session_state.bot.add_response(question, answer)
                st.session_state.learning_responses[question] = answer
                
                add_to_history(get_current_bot_name(), answer)

                st.success("Resposta salva! Agora o EcoBot sabe responder essa pergunta. 🌱")
                st.session_state.pending_question = None
                st.rerun() # Atualiza a tela para remover a área de aprendizado
            elif learn_submitted:
                st.error("Por favor, digite uma resposta antes de salvar.")

def display_history():
    """Exibe o histórico de mensagens na tela."""
    for chat in reversed(st.session_state.history):
        is_user = (chat["speaker"] == "Usuário")
        
        # Estilo da mensagem
        bg = "#DCF8C6" if is_user else "#FFFFFF"
        align = "flex-end" if is_user else "flex-start"
        st.markdown(
            f"""
            <div style='display:flex; justify-content:{align}; margin:4px 0;'>
                <div style='background-color:{bg}; color:#000; padding:10px; border-radius:10px; max-width:70%; word-wrap:break-word;'>
                    <b>{chat['speaker']}:</b> {chat['message']}
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# ------------------ Layout Principal (UI) ------------------
st.title("🌱 EcoBot - Seu assistente ambiental")

# Sidebar com opções
with st.sidebar:
    st.header("Opções")
    handle_personality_change()
    
    st.subheader("📜 Histórico")
    if st.session_state.history:
        history_txt = "\n".join(f"{c['speaker']}: {c['message']}" for c in st.session_state.history)
        st.download_button("💾 Salvar Histórico", history_txt, file_name="historico.txt")
    
    if st.button("🗑️ Encerrar conversa"):
        st.session_state.history = []
        st.rerun()

# Formulário de Chat
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Digite sua mensagem:", key="chat_input", label_visibility="collapsed", placeholder="Digite sua mensagem...")
    submitted = st.form_submit_button("Enviar")
    if submitted and user_input.strip():
        handle_chat_submission(user_input)

# Área de Aprendizado
handle_learning_process()

# Adiciona uma linha para separar o input do histórico
st.markdown("---")

# Exibição do Histórico
display_history()