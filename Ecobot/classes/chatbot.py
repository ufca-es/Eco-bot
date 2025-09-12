from typing import Dict
import random
import os
import json
from Ecobot.classes.chatbot_memory import ChatBotMemory


class ChatBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    """

    def __init__(self, data: tuple):
        self.nome = data[0]
        self.respostas = data[1]
        self.keywords = data[2] or {}

        # Inicializa memória já com o nome e inicia sessão
        self.memory = ChatBotMemory(self.nome)
        self.memory.start_session()

    # Serve como um construtor alternativo para escolher a personalidade do chatbot.
    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        """
        Lógica:
        - Tenta encontrar uma resposta exata para a pergunta.
        - Se não encontrar, busca por keywords na entrada.
        - Se ainda não encontrar, tenta respostas aprendidas.
        - Se falhar, ativa modo de aprendizado.
        """

        r_final = ''

        # 1. Match exato
        for q, r in self.respostas.items():
            if pergunta == q:
                r_final = f"{self.nome}: {random.choice(r)}"
                break

        # 2. Procura por keywords (só se ainda não respondeu)
        if not r_final:
            for q, kws in self.keywords.items():
                for kw in kws:
                    if kw in pergunta:
                        r_ops = self.respostas.get(q) or []
                        if r_ops:
                            r_final = f"{self.nome}: {random.choice(r_ops)}"
                            break
                if r_final:
                    break

        # 3. Respostas aprendidas (arquivo learning_responses.json)
        if not r_final:
            for q, resp in learning_responses.items():
                if pergunta in q:
                    r_final = f"{self.nome}: {resp}"
                    break

        # 4. Fallback para aprendizado
        if not r_final:
            r_final = self.learning(pergunta)

        # Registrar histórico
        self.memory.log_interaction(pergunta, r_final)

        return r_final

    def learning(self, pergunta: str):
        """
            -Salvar essa nova pergunta e resposta em um arquivo separado (ex: aprendizado.txt);
        """
        new_response = input(
            f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder? (Por favor insira uma resposta apropriada): ").strip()

        if not new_response or "esquecer" in new_response:
            return "Aprendizado cancelado. Tudo bem! 😊"

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "responses", "learning_responses.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Carrega JSON existente (ou inicia vazio)
        data = {}
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                data = {}

        data[pergunta] = new_response

        # Salva todo o dicionário formatado
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Feedback
        return f"{self.nome}: Obrigado! Aprendi uma nova resposta. 😊"
