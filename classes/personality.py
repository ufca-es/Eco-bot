from typing import List, Dict
import random

class Personalidade:
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    """
    def __init__(self, nome: str, respostas: Dict[str, List[str]]):
        self.nome = nome
        self.respostas = respostas  # Pergunta -> lista de variações de resposta

    def responder(self, pergunta: str) -> str:
        """
        Retorna uma resposta adequada ao estilo da personalidade.
        """
        return f"{self.nome}: {random.choice(self.respostas[pergunta])}"
