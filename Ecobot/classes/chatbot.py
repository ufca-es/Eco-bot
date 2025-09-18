# Ecobot/classes/chatbot.py (Versão Adaptada para a Web)

from typing import Dict
import random
from classes.chatbot_memory import ChatBotMemory

class ChatBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    Esta versão foi adaptada para funcionar com interfaces web.
    """

    def __init__(self, data: tuple):
        """Inicializa o bot com nome, respostas e palavras-chave."""
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
        pergunta_lower = pergunta.lower()

        # 1. Match exato (agora usando a pergunta em minúsculas)
        if pergunta_lower in self.respostas and isinstance(self.respostas.get(pergunta_lower), list):
            if self.respostas[pergunta_lower]:
                r_final = f"{self.nome}: {random.choice(self.respostas[pergunta_lower])}"

        # 2. Procura por keywords
        if not r_final:
            for q, kws in self.keywords.items():
                if any(kw in pergunta_lower for kw in kws):
                    r_ops = self.respostas.get(q)
                    if r_ops:
                        r_final = f"{self.nome}: {random.choice(r_ops)}"
                        break
        
        # 3. Respostas aprendidas (fornecidas pela interface)
        if not r_final and pergunta_lower in learning_responses:
             r_final = f"{self.nome}: {learning_responses[pergunta_lower]}"

        # 4. Se não encontrar, ativa o modo de aprendizado.
        if not r_final:
            r_final = self.learning(pergunta)

        # Registra a interação no history.txt.
        self.memory.log_interaction(pergunta, r_final)
        return r_final
    
    def learning(self, pergunta: str):
        """
        ADAPTAÇÃO WEB: Este método não usa mais input() nem salva arquivos.
        Ele apenas retorna uma mensagem específica que "sinaliza" para a 
        interface web que o bot precisa aprender. A interface cuidará de 
        pedir a nova resposta ao usuário e salvá-la no arquivo.
        """
        return f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder?"