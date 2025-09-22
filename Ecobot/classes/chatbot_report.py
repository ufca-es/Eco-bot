from .chatbot_memory import ChatBotMemory
from .chatbot_analytics import ChatbotAnalytics

class ChatbotReport:
    memory = ChatbotAnalytics()
    output_path = ChatBotMemory.history_file_path("relatorio.txt")

    @classmethod
    def generate_report(cls) -> str:
        # Generate a simple report and save to file

        lines = [
            "==== RELATÓRIO ECOBOT ====",
            f"Total de interações: {cls.memory.interaction_count}",
            f"Pergunta mais feita: {cls.memory.most_asked_questions}",
            f"Uso por personalidade:\n{cls.memory.count_personalities_usages}",
        ]

        content = "\n".join(lines) + "\n"
        with open(cls.output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return cls.output_path