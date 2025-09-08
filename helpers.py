import os
from classes.chatbot import ChaterBot
import json

def loading_responses_personality():
    funny = {}
    education = {}
    rude = {}
    keywords = {}

    # Caminho relativo ao diretório deste arquivo (helpers.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_path = os.path.join(base_dir, "responses", "questions.json")

    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        # Lidar com o erro se o arquivo não for encontrado.
        print(f"Arquivo questions.json não encontrado.")
        data = {}

    # iterando e salvando as perguntas com respectivas personalidades
    for question, respostas in data.items():
        funny[question] = respostas.get('engracada', [])
        education[question] = respostas.get('formal', [])
        rude[question] = respostas.get('rude', [])
        keywords[question] = respostas.get('keywords', [])

    return {
        'engracada': ChaterBot('Ecobot-funny', funny, keywords),
        'formal': ChaterBot('Ecobot-educational', education, keywords),
        'rude': ChaterBot('Ecobot-rude', rude, keywords),
    }

def loading_learning_responses():
    path = os.path.join(os.path.dirname(__file__), "responses", "learning_responses.json")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

personalidades = loading_responses_personality()
# learning_responses = loading_learning_responses() - PRECISA SER ATUALIZADA A CADA ITERAÇÃO.