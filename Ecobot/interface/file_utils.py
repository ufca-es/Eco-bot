# file_utils.py – Gerencia arquivos.
# Lê e salva respostas no JSON de aprendizagem.
import json
import os
import streamlit as st




# Caminho do arquivo onde as respostas aprendidas serão salvas em JSON
LEARNING_FILE = os.path.join("responses", "learning_responses.json")

# Função para carregar as respostas aprendidas do arquivo JSON
def load_learning_responses():
    try:
        # Abre o arquivo em modo leitura e retorna os dados como dicionário
        with open(LEARNING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # Caso o arquivo não exista ou esteja corrompido, retorna um dicionário vazio
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para salvar/atualizar uma resposta aprendida
def save_learning_response(question, answer):
    # Carrega os dados existentes
    data = load_learning_responses()
    # Adiciona ou atualiza a resposta para a pergunta
    data[question] = answer
    # Garante que a pasta 'responses' exista
    os.makedirs(os.path.dirname(LEARNING_FILE), exist_ok=True)
    # Salva o dicionário atualizado no arquivo JSON
    with open(LEARNING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Função para transformar o histórico em texto formatado
def get_history_as_text():
    # Junta todas as mensagens do histórico armazenado no session_state do Streamlit
    return "\n".join(f"{c['speaker']}: {c['message']}" for c in st.session_state.history)