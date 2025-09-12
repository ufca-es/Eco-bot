import os
import json
from classes.chatbot_memory import ChatBotMemory

# Carrega perguntas e respostas padrões
def loading_responses_personality():
    funny, education, rude, keywords = {}, {}, {}, {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_path = os.path.join(base_dir, "responses", "questions.json")

    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise FileNotFoundError("Arquivo questions.json não encontrado.")

    for question, respostas in data.items():
        funny[question] = respostas.get('engracada', [])
        education[question] = respostas.get('formal', [])
        rude[question] = respostas.get('rude', [])
        keywords[question] = respostas.get('keywords', [])

    return {
        'engracada': {'name':'Ecobot-funny','responses':funny,'keywords':keywords},
        'formal':   {'name':'Ecobot-education','responses':education,'keywords':keywords},
        'rude':     {'name':'Ecobot-rude','responses':rude,'keywords':keywords}
    }

personalidades = loading_responses_personality()

def loading_learning_responses():
    path = os.path.join(os.path.dirname(__file__), "responses", "learning_responses.json")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_learning_response(question, answer):
    path = os.path.join(os.path.dirname(__file__), "responses", "learning_responses.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Carrega respostas existentes
    try:
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Adiciona nova pergunta
    data[question] = answer

    # Salva no arquivo
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
