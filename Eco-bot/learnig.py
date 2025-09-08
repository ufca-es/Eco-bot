import json
import os

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

def perguntar_e_aprender():
    novos = carregar_novos_aprendizados()
    aprendidas = 0
    while True:
        pergunta = input("Faça uma pergunta para o Ecobot (ou digite 'sair' para encerrar): ").strip()
        if pergunta.lower() == "sair":
            break
        if pergunta in novos:
            print(f"Ecobot: {novos[pergunta]}")
        else:
            print("Ecobot: Não sei responder. Você pode me ensinar? Digite a resposta ou pressione Enter para pular.")
            resposta_usuario = input("Resposta: ").strip()
            if resposta_usuario:
                novos[pergunta] = resposta_usuario
                salvar_novos_aprendizados(novos)
                aprendidas += 1
                print(f"Ecobot: Aprendi! Agora sei responder '{pergunta}'")
            else:
                print("Ecobot: Ok, não aprendi essa resposta.")
    print(f"\nTotal de perguntas aprendidas nesta sessão: {aprendidas}")

if __name__ == "__main__":
    perguntar_e_aprender()