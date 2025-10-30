from classes import ChatBot, ChatbotAnalytics, ChatbotReport, ChatbotFrequentQuestions
from helpers import *

def main():
    bot = ChatBot(get_personality())

    # Print last 5 interactions
    last5_interactions()

    # Frequent questions suggestions
    freq = ChatbotFrequentQuestions.get_frequent_questions()
    if freq:
        print("Sugestões de perguntas frequentes:")
        for q, n in freq:
            print(f" - {q} ({n}x)")
        print("=" * 50)

    while True:
        question = input("Você: ").strip().lower()

        # Changing personality
        if any(phrase in question for phrase in change_triggers):
            bot = ChatBot(get_personality())
            print(f"💡 Personalidade alterada para: {bot.name}")
            continue

        # Exit
        if any(trigger in question for trigger in exit_triggers):
            print("Obrigado por utilizar o Ecobot♻️, fico feliz em te ajudar!😍")
            print(50 * "=")
            analytics = ChatbotAnalytics()
            print(analytics)

            # Generate report
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
