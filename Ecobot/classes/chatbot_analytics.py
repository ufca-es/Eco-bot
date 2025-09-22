import os
from collections import Counter
from .chatbot_memory import ChatBotMemory

path = ChatBotMemory.history_file_path()

class ChatbotAnalytics:
    """
    Esta classe é responsável por ler o arquivo history.txt e extrair
    estatísticas úteis sobre as conversas.
    """

    @property
    def interaction_count(self):
        """Conta o número total de interações (linhas de diálogo) no histórico."""
        if not os.path.exists(path): return 0
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if not line.isspace() and not line.startswith("==="))

    @property
    def most_asked_questions(self):
        """Encontra a pergunta exata mais repetida no histórico, filtrando entradas inválidas."""
        questions = {}
        if not os.path.exists(path): return 'Dados insuficientes.'

        invalid_starts = ("&",)
        invalid_contains = ("python.exe", ":/", "\\")
        
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Você:" not in line: continue
                raw = line.split("Você:")[1].split("||")[0].strip()
                q_lower = raw.lower()
                if not raw or q_lower.startswith(invalid_starts) or any(tok in q_lower for tok in invalid_contains) or len(raw) > 120:
                    continue
                questions[raw] = questions.get(raw, 0) + 1
        if questions:
            return max(questions, key=questions.get)
        return 'Dados insuficientes.'

    @property
    def count_personalities_usages(self):
        """Conta quantas vezes cada sessão foi iniciada com cada personalidade."""
        personalities = {}
        if not os.path.exists(path): return 'Dados insuficientes.'
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Persona:" in line:
                    persona = line.split("Persona:")[1].split("===")[0].strip()
                    personalities[persona] = personalities.get(persona, 0) + 1
        if personalities:
            msg = ''
            for key, value in personalities.items():
                msg += f"\t{key}: {value} vezes\n"
            return msg
        return 'Dados insuficientes.'

    @staticmethod
    def get_frequent_questions(top_n: int = 5) -> list[tuple[str, int]]:
        """
        Analisa o histórico e retorna uma lista das 'top_n' perguntas mais comuns,
        junto com sua contagem. Usado pela interface para as sugestões.
        """
        path_hist = ChatBotMemory.history_file_path()
        if not os.path.exists(path_hist): return []
        
        questions = []
        invalid_starts = ("&",)
        invalid_contains = ("python.exe", ":/", "\\")
        
        with open(path_hist, 'r', encoding='utf-8') as f:
            for line in f:
                if "Você:" not in line: continue
                raw = line.split("Você:",1)[1].split("||",1)[0].strip()
                low = raw.lower()
                if not raw or low.startswith(invalid_starts) or any(tok in low for tok in invalid_contains):
                    continue
                if '?' in raw or len(raw.split()) <= 6:
                    questions.append(raw)
        if not questions: return []
        return Counter(questions).most_common(top_n)

    def __str__(self):
        return (
            f"=== Estatísticas do EcoBot ===\n"
            f"Total de interações: {self.interaction_count}\n"
            f"Pergunta mais feita: {self.most_asked_questions}\n"
            f"Uso por personalidade:\n{self.count_personalities_usages}"
        )