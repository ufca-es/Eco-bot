import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# O chatbot será treinado com as perguntas e respostas dessas listas.
# O tom do bot será definido pela comunicação apresentada na conversa e pela seleção do usuário.


def data():
    with open('dialogo.json', 'r', encoding='utf-8') as f:
        conversation = json.load(f)

    return list(conversation)


def main():
    chatbot = ChatBot("Ecobot")

    trainer = ListTrainer(chatbot)
    # Treinando o bot com as listas

    conversa = data()
    trainer.train(conversa)

    # Loop de conversa
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Ecobot: Até logo! Continue reciclando! ♻️")
            break
        resposta = chatbot.get_response(pergunta)
        print("Ecobot:", resposta)

if __name__ == "__main__":
    main()
