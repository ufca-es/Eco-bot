from classes.chatbot_memory import ChatBotMemory
from collections import Counter

class ChatbotFrequentQuestions:
    #Classe para analisar o histórico de interações e extrair perguntas frequentes.

    @staticmethod
    def get_frequent_questions(top_n: int = 5) -> list[tuple[str, int]]:
        path_hist = ChatBotMemory.history_file_path()

        questions = []
        invalid_starts = ("&",)
        invalid_contains = ("python.exe", ":/", "\\")

        with open(path_hist, 'r', encoding='utf-8') as f:
            for line in f:
                if "Você:" not in line:
                    continue
                raw = line.split("Você:",1)[1].split("||",1)[0].strip()
                low = raw.lower()
                if not raw:
                    continue
                if low.startswith(invalid_starts) or any(tok in low for tok in invalid_contains):
                    continue
                # heurística: considerar só perguntas com ? ou até 6 palavras
                if '?' in raw or len(raw.split()) <= 6:
                    questions.append(raw)
        if not questions:
            return []
        counter = Counter(questions)
        return counter.most_common(top_n)