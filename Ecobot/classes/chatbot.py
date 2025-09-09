from typing import List, Dict
import random
import os
import json

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

        # Try find keyword in pergunta
        for q, kws in self.keywords.items():
            for kw in kws:
                if kw in pergunta:
                    opcoes = self.respostas.get(q) or []
                    if opcoes:
                        return f"{self.nome}: {random.choice(opcoes)}"

        for q, resp in learning_responses.items():
            if pergunta in q:
                return f"{self.nome}: {resp}"

        # Fallback
        return self.learning(pergunta)

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

    def history(self):
        """
        Retorna o histórico de interações do chatbot num arquivo .txt.
        """

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

    def statistics(self):
        """
        Retorna estatísticas de uso do chatbot, como número de perguntas respondidas,
        personalidades mais usadas, etc.
        """
        pass
