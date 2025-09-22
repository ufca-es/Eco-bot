from classes import ChatBot, ChatbotAnalytics, ChatbotReport, ChatbotFrequentQuestions
from helpers import *
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

    # Mostrar últimas 5 interações (Task 11)
    last5_interactions()

    # Sugestões de perguntas frequentes (Task 15)
    freq = ChatbotFrequentQuestions.get_frequent_questions()
    if freq:
        print("Sugestões de perguntas frequentes:")
        for q, n in freq:
            print(f" - {q} ({n}x)")
        print("=" * 50)

    while True:
        question = input("Você: ").strip().lower()

        # Mudar personalidade (Task 08)
        if any(phrase in question for phrase in change_triggers):
            bot = ChatBot(get_personality())
            print(f"💡 Personalidade alterada para: {bot.name}")
            continue

        if any(trigger in question for trigger in exit_triggers):
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            print(50 * "=")
            analytics = ChatbotAnalytics()
            print(analytics)

            # Gerar relatório (Task 14)
            try:
                print(50*"=")
                print("Gerando relatório...")
                report_path = ChatbotReport.generate_report()
                print(f"Relatório gerado em: {report_path}")
            except Exception as e:
                print(f"Falha ao gerar relatório: {e}")
            print(50 * "=")
            break

        print(bot.reply(question, loading_learning_responses()))


if __name__ == '__main__':
    main()
