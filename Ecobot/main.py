from helpers import personalidades, loading_learning_responses
from classes.chatbot import ChaterBot
from classes.chatbot_analytics import ChatbotAnalytics

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
    bot.start_session()

    # Mostrar as últimas 5 interações anteriores, se houver
    try:
        previous = bot.history()  # default = 5
        if previous:
            print("=" * 50)
            print("Últimas 5 interações anteriores:")
            for line in previous:
                print(line)
            print("=" * 50)
    except Exception:
        # Não interromper o fluxo por erro ao ler histórico
        print("Não foi possível carregar o histórico de interações.")
        pass

    while True:
        question = input("Você: ").strip().lower()

        # Retorna True se alguma frase de change estiver em question.
        if any(phrase in question for phrase in change_triggers):
            bot = ChaterBot.get_personality(personalidades)
            bot.start_session()
            continue

        # ''
        if any(trigger in question for trigger in exit_triggers):
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            print(ChatbotAnalytics())
            break

        # Imprimir a resposta do bot e registrar histórico
        print(bot.reply(question, loading_learning_responses()))


if __name__ == '__main__':
    main()
