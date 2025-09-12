import os
import json

def loading_responses_personality():
    funny, education, rude, keywords = {}, {}, {}, {}

    # Caminho relativo ao diretório deste arquivo (helpers.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_path = os.path.join(base_dir, "responses", "questions.json")

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
        if p in personalidades:
            return personalidades[p]['name'], personalidades[p]['responses'], personalidades[p]['keywords']
        print("Personalidade inválida. Tente novamente.")

def loading_learning_responses():
    path = os.path.join(os.path.dirname(__file__), "responses", "learning_responses.json")
    try:
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

