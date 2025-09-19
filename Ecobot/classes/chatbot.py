# Ecobot/classes/chatbot.py (Versão Adaptada para a Web)

from typing import Dict
import json
import random
import os
from classes.chatbot_memory import ChatBotMemory

class ChatBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    Esta versão foi adaptada para funcionar com interfaces web.
    """

    def __init__(self, data: tuple):
        """Inicializa o bot com nome, respostas e palavras-chave."""
        self.pergunta = ''
        self.nome = data[0]
        self.respostas = data[1]
        self.keywords = data[2] or {}

        # A classe memória continua sendo usada para registrar o histórico.
        self.memory = ChatBotMemory(self.nome)
        self.memory.start_session()

    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        """
        Encontra a melhor resposta para a pergunta do usuário.
        A lógica é a mesma da sua versão original.
        """
        r_final = ''
        # Converte a pergunta para minúsculas uma vez para otimizar as buscas.
        self.pergunta = pergunta

        # 1. Match exato (agora usando a pergunta em minúsculas)
        if self.pergunta in self.respostas and isinstance(self.respostas.get(self.pergunta), list):
            if self.respostas[self.pergunta]:
                r_final = f"{self.nome}: {random.choice(self.respostas[self.pergunta])}"

        # 2. Procura por keywords
        if not r_final:
            for q, kws in self.keywords.items():
                if any(kw in self.pergunta for kw in kws):
                    r_ops = self.respostas.get(q)
                    if r_ops:
                        r_final = f"{self.nome}: {random.choice(r_ops)}"
                        break
        
        # 3. Respostas aprendidas (fornecidas pela interface)
        if not r_final and self.pergunta in learning_responses:
             r_final = f"{self.nome}: {learning_responses[self.pergunta]}"

        # 4. Se não encontrar, ativa o modo de aprendizado.
        if not r_final:
            r_final = self.learning()

        # Registra a interação no history.txt.
        self.memory.log_interaction(pergunta, r_final)
        return r_final

    def learning(self):
        """
            -Salvar essa nova pergunta e resposta em um arquivo separado (ex: aprendizado.txt);
        """
        message = f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder? (Por favor insira uma resposta apropriada): "
        new_response = input(message).strip()

        if not new_response or "esquecer" in new_response:
            return "Aprendizado cancelado. Tudo bem! 😊"

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "responses", "learning_responses.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Carrega JSON existente (ou inicia vazio)
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                data = {}

        data[self.pergunta] = new_response
        # Registrar histórico
        self.memory.log_interaction(self.pergunta, message + "Users input:" + new_response)


        # Salva todo o dicionário formatado
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Feedback
        return f"{self.nome}: Obrigado! Aprendi uma nova resposta. 😊"
