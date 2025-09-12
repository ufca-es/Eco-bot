"""
    Task 13: Implementação da coleta de estatísticas:
        - Número total de interações;
        - Pergunta mais feita da sessão;
        - Quantas vezes cada personalidade foi usada;
"""

from Ecobot.classes.chatbot_memory import ChatBotMemory
path = ChatBotMemory.history_file_path()

class ChatbotAnalytics:
    @property
    def interaction_count(self):
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if not line.isspace() and not line.startswith("==="))

    @property
    def most_asked_questions(self):
        questions = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Você:" in line:
                    question = line.split("Você:")[1].split("||")[0].strip()
                    questions[question] = questions.get(question, 0) + 1
        if questions:
            return max(questions, key=questions.get)

        return 'Dados insuficientes.'

    @property
    def count_personalities_usages(self):
        personalities = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Persona:" in line:
                    persona = line.split("Persona:")[1].split("===")[0].strip()
                    personalities[persona] = personalities.get(persona, 0) + 1
        if personalities:
            return personalities
        return 'Dados insuficientes.'

    def __str__(self):
        return (f"Total de interações: {self.interaction_count}\n"
                f"Pergunta mais feita: {self.most_asked_questions}\n"
                f"Uso por personalidade: {self.count_personalities_usages}")
