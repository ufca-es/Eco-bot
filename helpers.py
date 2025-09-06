from Ecobot.classes import  Personalidade
#Ecobot, Historico, Aprendizado, Estatisticas, personality
import json

def loading_responses_personality():
    funny = dict()
    education = dict()
    rude = dict()

    with open('questions.json', 'r', encoding='utf-8') as f:
        q = json.load(f)

    # iterating the questions
    for question, respostas in q.items():
        funny[question] = respostas.get('engracada', [])
        education[question] = respostas.get('formal', [])
        rude[question] = respostas.get('rude', [])

    return {
        "engracada": Personalidade("Ecobot-funny", funny),
        "formal": Personalidade("Ecobot-educational", education),
        "rude": Personalidade("Ecobot-rude", rude)
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
        if p in personalidades:
            return personalidades[p]
        else:
            print("Personalidade inválida! Tente novamente.")
