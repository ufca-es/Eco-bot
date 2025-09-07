from helpers import personalidades
from classes.chatbot import ChaterBot

def main():
    bot = ChaterBot.get_personality(personalidades)

    while True:
        question = input("Você: ").strip().lower()
        if "sair" in question:
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            break

        print(bot.responder(question))


if __name__ == '__main__':
    main()