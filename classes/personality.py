from typing import List, Dict
import random

class ChaterBot:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    """
    def __init__(self, nome: str, respostas: Dict[str, List[str]], keywords: Dict[str, List[str]]):
        self.nome = nome
        self.respostas = respostas
        self.keywords = keywords or {}

    def responder(self, pergunta: str) -> str:
        """
        Lógica simples:
        - Procura por qualquer keyword (case-insensitive) contida na entrada.
        - Fallback: verifica igualdade simples (case-insensitive) com as perguntas conhecidas.
        - Caso não encontre, retorna mensagem padrão.
        """

        # Try find keyword in pergunta
        for q, kws in self.keywords.items():
            for kw in kws:
                if kw in pergunta:
                    opcoes = self.respostas.get(q) or []
                    if opcoes:
                        return f"{self.nome}: {random.choice(opcoes)}"

        # Fallback
        return f"{self.nome}: Desculpe, não encontrei uma resposta pra isso. Tente reformular ou ser mais específico."

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
            else:
                print("Personalidade inválida! Tente novamente.")
