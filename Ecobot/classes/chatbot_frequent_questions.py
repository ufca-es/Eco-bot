

from collections import Counter
from classes.chatbot_memory import ChatBotMemory
import os

class chatbot_frequent_questions:
    """
    Esta classe é responsável por identificar as perguntas mais frequentes
    feitas ao chatbot, analisando o histórico de conversas.
    """
    @staticmethod
    def get_frequent_questions(top_n: int = 3) -> list:
        """
        Analisa o arquivo de histórico e retorna as 'top_n' perguntas mais comuns.
        Retorna uma lista vazia se não houver histórico ou perguntas válidas.
        """
        path_hist = ChatBotMemory.history_file_path()
        if not os.path.exists(path_hist):
            return []

        questions = []
        try:
            with open(path_hist, 'r', encoding='utf-8') as f:
                for line in f:
                    if "Você:" in line:
                        # Extrai a pergunta do usuário da linha de log
                        raw_question = line.split("Você:", 1)[1].split("||", 1)[0].strip()
                        if raw_question:
                            questions.append(raw_question)
        except Exception:
            # Se houver qualquer erro na leitura, retorna uma lista vazia
            return []
        
        if not questions:
            return []

        # Conta a frequência de cada pergunta e retorna as mais comuns
        counter = Counter(questions)
        return counter.most_common(top_n)