from classes.personality import ChaterBot
import json

def loading_responses_personality():
    funny = {}
    education = {}
    rude = {}
    keywords = {}

    with open(r'C:\Users\raque\PycharmProjects\Chatbot-Ecobot\Ecobot\questions.json','r', encoding='utf-8') as f:
        data = json.load(f)

    # iterando as perguntas
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

personalidades = loading_responses_personality()
