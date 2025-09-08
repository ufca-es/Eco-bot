from helpers import personalidades
import json
import os
from classes.chatbot import ChaterBot

def carregar_novos_aprendizados():
    path = os.path.join(os.path.dirname(__file__), "newansawers.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def salvar_novos_aprendizados(data):
    path = os.path.join(os.path.dirname(__file__), "newansawers.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    bot = ChaterBot.get_personality(personalidades)
    novos = carregar_novos_aprendizados()

    
    while True:
        pergunta = input("Você: ").strip()
        if pergunta.lower() == "sair":
            break
        elif pergunta.lower().startswith("aprender:"):
            try:
                conteudo = pergunta[len("aprender:"):].strip()
                q, r = conteudo.split("->", 1)
                q = q.strip()
                r = r.strip()
                if q and r:
                    novos[q] = r
                    salvar_novos_aprendizados(novos)
                    print(f"Ecobot: Aprendi! Agora sei responder '{q}'")
                else:
                    print("Formato inválido! Pergunta ou resposta vazia.")
            except Exception:
                print("Formato inválido! Use: aprender: <pergunta> -> <resposta>")
        elif pergunta in novos:
            print(f"Ecobot: {novos[pergunta]}")
        else:
            resposta_bot = bot.reply(pergunta)
            if "Desculpe, não encontrei uma resposta" in resposta_bot:
                print("Ecobot: Não sei responder. Você pode me ensinar? Digite a resposta ou pressione Enter para pular.")
                resposta_usuario = input("Resposta: ").strip()
                if resposta_usuario:
                    novos[pergunta] = resposta_usuario
                    salvar_novos_aprendizados(novos)
                    print(f"Ecobot: Aprendi! Agora sei responder '{pergunta}'")
                else:
                    print(resposta_bot)
            else:
                print(resposta_bot)

if __name__ == "__main__":
    main()