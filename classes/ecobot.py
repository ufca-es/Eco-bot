from .personality import Personalidade
from typing import Dict

class ChatBot:
    """
    Classe principal que orquestra todo o fluxo do chatbot.
    """

    # , historico: Historico, aprendizado: Aprendizado, estatisticas: Estatisticas
    def __init__(self, personalidades: Dict[str, Personalidade]):
        self.personalidades = personalidades

        # self.historico = historico
        # self.aprendizado = aprendizado
        # self.estatisticas = estatisticas

        self.personalidade_atual = None

    def iniciar(self):
        """
        Inicializa o chatbot (carrega histórico, aprendizado, etc).
        """
        pass

    def escolher_personalidade(self, nome: str):
        """
        Troca a personalidade do bot.
        """
        pass

    def processar_pergunta(self, pergunta: str) -> str:
        """
        Processa a pergunta do usuário e retorna uma resposta.
        """
        pass

    def salvar_relatorio(self, arquivo: str = "relatorio.txt"):
        """
        Gera e salva o relatório final da interação.
        """
        pass