from typing import List, Dict
import random
import os
import json
from datetime import datetime

class ChatBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    """

    def __init__(self, data: tuple):
        self.nome = data[0]
        self.respostas = data[1]
        self.keywords = data[2] or {}

    # Serve como um construtor alternativo para escolher a personalidade do chatbot.
    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        """
        Lógica:
        - Tenta encontrar uma resposta exata para a pergunta.
        - Se não encontrar, busca por keywords na entrada.
        - Se ainda não encontrar, pede ao usuário uma resposta para aprender.
        """

        r_final = ''

        # Try to find exact match by the question
        for q, r in self.respostas.items():
            if pergunta == q:
                r_final = f"{self.nome}: {random.choice(r)}"
                break

        # Try find keyword in pergunta
        for q, kws in self.keywords.items():
            for kw in kws:
                if kw in pergunta:
                    r_ops = self.respostas.get(q) or []
                    if r_ops:
                        r_final = f"{self.nome}: {random.choice(r_ops)}"
                        break
            if r_final:
                break

        if not r_final:
            for q, resp in learning_responses.items():
                if pergunta in q:
                    r_final = f"{self.nome}: {resp}"
                    break

        # Fallback
        if not r_final:
            r_final = self.learning(pergunta)

        # Registrar histórico da interação
        try:
            self._log_interaction(pergunta, r_final)
        except FileNotFoundError:
            pass

        return r_final

    def learning(self, pergunta: str):
        """
        Adiciona uma nova pergunta e resposta ao dicionário de respostas.
            -Solicitar ao usuário uma resposta apropriada;
            -Salvar essa nova pergunta e resposta em um arquivo separado (ex: aprendizado.txt);
        """
        new_response = input(
            f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder? (Por favor insira uma resposta apropriada): ").strip()

        if "esquecer" in new_response:
            return "Ok, não vou salvar."

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

    def history(self, last_n: int = 5):
        """
        Retorna as últimas `last_n` interações do histórico num arquivo .txt.
        """
        path = self._history_file_path()
        if not os.path.exists(path):
            return []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [line.rstrip('\n') for line in f.readlines() if line.strip()]
            return lines[-last_n:] if last_n > 0 else lines
        except FileNotFoundError:
            return []

    # ---------------- Helpers de histórico -----------------
    def start_session(self) -> None:
        """Escreve um cabeçalho de início de sessão no arquivo de histórico."""
        path = self._history_file_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"\n=== Sessão iniciada em {timestamp} | Persona: {self.nome} ===\n"
        try:
            with open(path, 'a', encoding='utf-8') as f:
                f.write(header)
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo de histórico não foi encontrado.")

    @staticmethod
    def _history_file_path() -> str:
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo de histórico não foi encontrado.")
        else:
            return os.path.join(base_dir, 'responses', 'history.txt')

    def _log_interaction(self, pergunta: str, resposta_formatada: str) -> None:
        path = self._history_file_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)

        prefixo = f"{self.nome}: "
        resposta_sem_prefixo = resposta_formatada[len(prefixo):] if resposta_formatada.startswith(prefixo) else resposta_formatada

        # current hour
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] ({self.nome}) Você: {pergunta} || Bot: {resposta_sem_prefixo}\n"
        with open(path, 'a', encoding='utf-8') as f:
            f.write(line)
