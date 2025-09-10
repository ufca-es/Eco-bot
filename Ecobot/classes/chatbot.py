from typing import List, Dict
import random
import os
import json
from datetime import datetime

class ChaterBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    """

    def __init__(self, nome: str, respostas: Dict[str, List[str]], keywords: Dict[str, List[str]]):
        self.nome = nome
        self.respostas = respostas
        self.keywords = keywords or {}

    def reply(self, pergunta: str, learning_responses: Dict[str, str]):
        """
        Lógica simples:
        - Procura por qualquer keyword contida na entrada.
        - Se encontrar, escolhe uma resposta aleatória dentre as opções disponíveis.
        - Caso não encontre, retorna mensagem padrão.
        """

        resposta_final = None

        # Try find keyword in pergunta
        for q, kws in self.keywords.items():
            for kw in kws:
                if kw in pergunta:
                    opcoes = self.respostas.get(q) or []
                    if opcoes:
                        resposta_final = f"{self.nome}: {random.choice(opcoes)}"
                        break
            if resposta_final:
                break

        if not resposta_final:
            for q, resp in learning_responses.items():
                if pergunta in q:
                    resposta_final = f"{self.nome}: {resp}"
                    break

        # Fallback
        if not resposta_final:
            resposta_final = self.learning(pergunta)

        # Registrar histórico da interação
        try:
            self._log_interaction(pergunta, resposta_final)
        except Exception:
            pass

        return resposta_final

    # Serve como um construtor alternativo para escolher a personalidade do chatbot.
    @classmethod
    def get_personality(cls, personalidades: Dict[str, "ChaterBot"]) -> "ChaterBot":
        print("=" * 50)
        print("Bem-vindo ao Ecobot ♻️")
        print("Escolha a personalidade do bot:")
        print(" - engraçada (engracada)")
        print(" - formal (formal)")
        print(" - rude (rude)")
        print("=" * 50)

        while True:
            p = input("Qual personalidade você gostaria de utilizar? ").strip().lower()
            if p in personalidades:
                return personalidades[p]
            print("Personalidade inválida. Tente novamente.")

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

    # ---------------- Helpers de histórico -----------------
    def history(self, last_n: int = 5):
        """
        Retorna as últimas `last_n` interações do histórico num arquivo .txt.
        """
        path = self._history_file_path()
        if not os.path.exists(path):
            return []
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines[-last_n:]

    def start_session(self):
        """
        Adiciona um cabeçalho simples ao início da sessão.
        """
        path = self._history_file_path()
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n=== Nova sessão: {self.nome} ===\n")

    def _history_file_path(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'responses', 'history.txt')

    def _log_interaction(self, pergunta, resposta_formatada):
        path = self._history_file_path()
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"Você: {pergunta} | Bot: {resposta_formatada}\n")

    def save_full_history(self, history_list):
        """
        Salva todo o histórico de conversa passado em history_list no arquivo .txt.
        Cada item da lista será gravado em uma linha.
        """
        path = self._history_file_path()
        with open(path, 'w', encoding='utf-8') as f:
            for interaction in history_list:
                f.write(interaction.strip() + '\n')
