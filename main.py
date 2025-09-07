from helpers import personalidades
from classes.chatbot import ChaterBot

change_triggers = (
    "mudar personalidade",
    "trocar personalidade",
    "alterar personalidade",
    "quero outra personalidade",
    "personalidade diferente",
    "mudar o bot",
    "trocar o bot",
    "alterar o bot",
    "quero outro bot"
)

exit_triggers = (
    "sair", "exit", "quit", "fechar", "encerrar", "finalizar",
    "parar", "stop", "tchau", "xau", "adeus", "bye",
    "até logo", "ate logo", "até mais", "ate mais"
)


def main():
    bot = ChaterBot.get_personality(personalidades)

    while True:
        question = input("Você: ").strip().lower()

        # Retorna True se alguma frase de change estiver em question.
        if any(phrase in question for phrase in change_triggers):
            bot = ChaterBot.get_personality(personalidades)
            continue

        # ''
        if any(trigger in question for trigger in exit_triggers):
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            break

        print(bot.reply(question))


if __name__ == '__main__':
    main()
