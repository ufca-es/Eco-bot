import random
from classes.chatbot_memory import ChatBotMemory
from typing import Dict

class ChatBot:
    def __init__(self, data: tuple):
        self.nome = data[0]
        self.responses = data[1].copy() if isinstance(data[1], dict) else {}  # dicionário de respostas
        self.keywords = data[2] or {}

        self.memory = ChatBotMemory(self.nome)
        self.memory.start_session()

    def add_response(self, question: str, answer: str):
        """Adiciona ou atualiza uma resposta aprendida dinamicamente"""
        self.responses[question] = answer

    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        r_final = ''

        # 1. Match exato
        if pergunta in self.responses:
            r = self.responses[pergunta]
            r_final = f"{self.nome}: {random.choice(r) if isinstance(r, list) else r}"

        # 2. Busca por keywords
        if not r_final:
            for q, kws in self.keywords.items():
                for kw in kws:
                    if kw in pergunta:
                        r_ops = self.responses.get(q) or []
                        if r_ops:
                            r_final = f"{self.nome}: {random.choice(r_ops)}"
                            break
                if r_final:
                    break

        # 3. Respostas aprendidas externas
        if not r_final and learning_responses:
            for q, resp in learning_responses.items():
                if pergunta in q:
                    r_final = f"{self.nome}: {resp}"
                    break

        # Log
        self.memory.log_interaction(pergunta, r_final)

        return r_final
