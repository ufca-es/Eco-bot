# ui_components.py – Cuida da interface visual.
# Desenha barra lateral, chat e área de aprendizagem.

import streamlit as st
from helpers import personalidades
from interface.handlers import handle_learning_submission, handle_chat_submission, add_to_history
from interface.session_state import init_bot
from interface.file_utils import get_history_as_text

def display_sidebar():
    """Desenha todos os elementos visuais da barra lateral."""
    with st.sidebar:
        st.header("Opções")
        
        current_index = list(personalidades.keys()).index(st.session_state.bot_personality)
        new_personality = st.selectbox("Personalidade:", options=list(personalidades.keys()), index=current_index, format_func=lambda x: x.capitalize())

        if st.session_state.bot_personality != new_personality:
            st.session_state.bot_personality = new_personality
            st.session_state.bot = init_bot(new_personality)
            # Adiciona a mensagem do sistema ao histórico
            add_to_history("Sistema", f"Personalidade alterada para {st.session_state.bot.name}!", role="system")
            st.rerun()
        
        st.divider()
        st.subheader("Últimas 5 Interações")
        if st.session_state.get('previous_history') and isinstance(st.session_state.previous_history, list):
            for line in st.session_state.previous_history:
                st.caption(line)
        else:
            st.caption("Nenhum histórico anterior.")
        st.divider()
        st.subheader("Sessão Atual")
        if st.session_state.history:
            st.download_button("💾 Salvar Conversa", get_history_as_text(), file_name="historico_ecobot.txt")
        if st.button("🗑️ Limpar Conversa"):
            st.session_state.history = []
            st.rerun()

def display_chat_history():
    """
    Mostra as mensagens na ordem cronológica correta (a mais antiga em cima).
    """
    for chat in st.session_state.history:
        # Define o nome do "speaker" para o chat_message alinhar corretamente (user à direita)
        role = chat.get("role", "bot") 
        
        with st.chat_message(name=role, avatar=("👤" if role == "user" else "🤖")):
            # Adiciona o rótulo em negrito
            if role == "user":
                st.markdown("**Pergunta:**")
            elif role == "bot":
                st.markdown(f"**Resposta ({chat['speaker']}):**")

            st.write(chat["message"])
            timestamp = chat.get("timestamp")
            if timestamp:
                st.markdown(f"<div style='text-align: right; color: grey; font-size: 0.75em;'>{timestamp}</div>", unsafe_allow_html=True)
                
def display_frequent_questions():
    """Desenha o 'popup' (expander) com as sugestões de perguntas."""
    questions = st.session_state.get("frequent_questions", [])
    if questions:
        with st.expander("💡 Ver sugestões de perguntas"):
            st.caption("Clique em uma pergunta para enviá-la.")
            for q, count in questions:
                button_text = f"{q} ({count}x)"
                if st.button(button_text, use_container_width=True): 
                    handle_chat_submission(q)
                
def display_learning_interface():
    """Desenha a área de aprendizado quando o bot não sabe uma resposta."""
    if st.session_state.pending_question:
        st.warning(f"O EcoBot não sabe responder: **'{st.session_state.pending_question}'**. Ajude-o a aprender!")
        with st.form("learning_form", clear_on_submit=True):
            new_answer = st.text_input("Digite a resposta ou 'esquecer' para cancelar:", key="new_answer_input")
            col1, col2 = st.columns([3, 1])
            with col1:
                submit_learn = st.form_submit_button("💾 Ensinar", use_container_width=True)
            with col2:
                submit_cancel = st.form_submit_button("❌ Esquecer", use_container_width=True)
            
            def cancel_learning():
                st.session_state.pending_question = None
                add_to_history("Sistema", "Aprendizado cancelado. Tudo bem! 😊", role="system")
                st.rerun()

            if submit_cancel:
                cancel_learning()
            if submit_learn:
                if new_answer.strip().lower() in ["esquecer", "sair"]:
                    cancel_learning()
                elif new_answer.strip():
                    handle_learning_submission(new_answer)