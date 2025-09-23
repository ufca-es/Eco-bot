import os
import json
from classes.chatbot_memory import ChatBotMemory

# Trigger phrases
change_triggers = ("mudar personalidade",
    "trocar personalidade",
    "alterar personalidade",
    "quero outra personalidade",
    "personalidade diferente",
    "mudar o bot",
    "trocar o bot",
    "alterar o bot",
    "quero outro bot")

exit_triggers = ("sair", "exit", "quit", "fechar", "encerrar", "finalizar",
    "parar", "stop", "tchau", "xau", "adeus", "bye",
    "até logo", "ate logo", "até mais", "ate mais")

questions_path = ChatBotMemory.history_file_path("questions.json")

def loading_responses_personality():
    funny, education, rude, keywords = {}, {}, {}, {}
    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        raise FileNotFoundError("Arquivo questions.json não encontrado.")

    # Making dictionaries for each personality
    for question, respostas in data.items():
        funny[question] = respostas.get('engracada', [])
        education[question] = respostas.get('formal', [])
        rude[question] = respostas.get('rude', [])
        keywords[question] = respostas.get('keywords', [])

    return {

        'engracada': {'name':'Ecobot-funny',
                      'chatbot_data' :funny,
                      'keywords' : keywords},
        'formal': {'name':'Ecobot-education',
                   'chatbot_data': education,
                   'keywords': keywords},

        'rude': {'name':'Ecobot-rude',
                 'chatbot_data': rude,
                 'keywords': keywords}

    }

personalities = loading_responses_personality()

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

        if p in personalities:
            return personalities[p]['name'], personalities[p]['chatbot_data'], personalities[p]['keywords']
        print("Personalidade inválida. Tente novamente.")

def loading_learning_responses():
    try:
        with open(ChatBotMemory.history_file_path("learning_responses.json"), 'r', encoding="utf-8") as f:
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
