from helpers import *

def main():

    bot = get_personality()

    while True:
        question = input("Você: ")
        if "sair" in question:
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            break

        print(bot.responder(question))


if __name__ == '__main__':
    main()