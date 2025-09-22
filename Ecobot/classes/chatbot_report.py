from chatbot_memory import ChatBotMemory
from chatbot_analytics import ChatbotAnalytics

class ChatbotReport:
    memory = ChatbotAnalytics()
    output_path = ChatBotMemory.history_file_path("relatorio.txt")

    @classmethod
    def generate_report(cls) -> str:
        #Gera um relatório de texto simples com estatísticas básicas.

        # Monta conteúdo legível
        lines = [
            "==== RELATÓRIO ECOBOT ====",
            f"Total de interações: {cls.memory.interaction_count}",
            f"Pergunta mais feita: {cls.memory.most_asked_questions}",
            f"Uso por personalidade:\n{cls.memory.count_personalities_usages}",
        ]
        usos = cls.memory.count_personalities_usages
        if isinstance(usos, dict):
            for persona, qtd in usos.items():
                lines.append(f" - {persona}: {qtd}")
        else:
            lines.append(str(usos))

        content = "\n".join(lines) + "\n"
        with open(cls.output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return cls.output_path