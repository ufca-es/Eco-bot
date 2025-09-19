from typing import Dict
import json
import random
import os
from classes.chatbot_memory import ChatBotMemory
import re
import unicodedata

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

    def _normalize(self, text: str) -> str:
        """Normaliza texto: minúsculas, sem acentos, sem pontuação e com espaços colapsados."""
        if not isinstance(text, str):
            return ""
        t = text.lower().strip()
        t = unicodedata.normalize('NFD', t)
        t = ''.join(ch for ch in t if unicodedata.category(ch) != 'Mn')  # remove acentos
        t = re.sub(r'[^a-z0-9\s]', ' ', t)  # remove pontuação mantendo letras/dígitos/espaços
        t = re.sub(r'\s+', ' ', t).strip()
        return t

    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        """
        Gera uma resposta baseada na pergunta e nas respostas aprendidas.
        """

        r_final = ''
        # Guarda a pergunta original (para histórico/aprendizado)
        self.pergunta = pergunta

        # Normaliza pergunta e estruturas de busca
        p_norm = self._normalize(pergunta)
        normalized_respostas = {
            self._normalize(q): v for q, v in (self.respostas or {}).items()
        }
        normalized_keywords = {
            self._normalize(q): [self._normalize(kw) for kw in (kws or [])]
            for q, kws in (self.keywords or {}).items()
        }
        normalized_learning = {
            self._normalize(k): v for k, v in (learning_responses or {}).items()
        }

        # 1. Match exato
        if p_norm in normalized_respostas and isinstance(normalized_respostas.get(p_norm), list):
            if normalized_respostas[p_norm]:
                r_final = f"{self.nome}: {random.choice(normalized_respostas[p_norm])}"

        # 2. Procura por keywords
        if not r_final:
            for nq, kws in normalized_keywords.items():
                if any(kw and kw in p_norm for kw in kws):
                    r_ops = normalized_respostas.get(nq)
                    if r_ops:
                        r_final = f"{self.nome}: {random.choice(r_ops)}"
                        break

        # 3. Respostas aprendidas
        if not r_final and p_norm in normalized_learning:
            r_final = f"{self.nome}: {normalized_learning[p_norm]}"

        # 4. Se não encontrar, ativa o modo de aprendizado.
        if not r_final:
            r_final = self.learning()

        # Registra a interação no history.txt (pergunta original + resposta).
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
