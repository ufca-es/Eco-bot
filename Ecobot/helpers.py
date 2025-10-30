import os
import json
from classes.chatbot_memory import ChatBotMemory

def loading_responses_personality():
    funny, education, rude, keywords = {}, {}, {}, {}

    # Caminho relativo ao diretório deste arquivo (helpers.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_path = os.path.join(base_dir, "chatbot_data", "questions.json")

    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        raise FileNotFoundError("Arquivo questions.json não encontrado.")


    # iterando e salvando as perguntas com respectivas personalidades
    for question, respostas in data.items():
        funny[question] = respostas.get('engracada', [])
        education[question] = respostas.get('formal', [])
        rude[question] = respostas.get('rude', [])
        keywords[question] = respostas.get('keywords', [])

    return {

        'engracada': {'name':'Ecobot-funny',
                      'responses' :funny,
                      'keywords' : keywords},
        'formal': {'name':'Ecobot-education',
                   'responses': education,
                   'keywords': keywords},

        'rude': {'name':'Ecobot-rude',
                 'responses': rude,
                 'keywords': keywords}

    }

personalidades = loading_responses_personality()

def get_personality():
    print("=" * 50)
    print("Bem-vindo ao Ecobot ♻️")
    print("Escolha a personalidade do bot:")
    print(" - engraçada (engracada)")
    print(" - formal (formal)")
    print(" - rude (rude)")
    print("=" * 50)

    while True:
        p = input("Qual personalidade você gostaria de utilizar? ").strip().lower()

        # empty input
        if not p:
            continue

        if p in personalidades:
            return personalidades[p]['name'], personalidades[p]['responses'], personalidades[p]['keywords']
        print("Personalidade inválida. Tente novamente.")

def loading_learning_responses():
    path = os.path.join(os.path.dirname(__file__), "chatbot_data", "learning_responses.json")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def last5_interactions():
    try:
        previous = ChatBotMemory.history()  # default = 5
        if previous:
            print("=" * 50)
            print("Últimas 5 interações anteriores:")

            if previous == "Histórico vazio.":
                print(previous)
                print("=" * 50)
                return

            for line in previous:
                print(line)
            print("=" * 50)
    except FileNotFoundError:
        # Não interromper o fluxo por erro ao ler histórico
        print("Não foi possível carregar o histórico de interações.")
        pass
