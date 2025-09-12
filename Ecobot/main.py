from helpers import get_personality, loading_learning_responses, last5_interactions
from classes.chatbot import ChatBot
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
    bot = ChatBot(get_personality())

    # Mostrar as últimas 5 interações anteriores, se houver
    last5_interactions()

    while True:
        question = input("Você: ").strip().lower()

        # Retorna True se alguma frase de change estiver em question.
        if any(phrase in question for phrase in change_triggers):
            bot = ChatBot(get_personality())
            continue

        # ''
        if any(trigger in question for trigger in exit_triggers):
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            print(50*"=")
            print(ChatbotAnalytics())
            print(50 * "=")
            break

        # Imprimir a resposta do bot e registrar histórico
        print(bot.reply(question, loading_learning_responses()))


if __name__ == '__main__':
    main()
