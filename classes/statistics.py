class Estatisticas:
    """
    Coleta e fornece estatísticas da sessão e acumuladas.
    """
    def __init__(self):
        self.contador_personalidades = {}  # nome -> contagem
        self.contador_perguntas = {}  # pergunta -> contagem

    def registrar_personalidade(self, nome: str):
        """
        Incrementa o contador de uso de uma personalidade.
        """
        pass

    def registrar_pergunta(self, pergunta: str):
        """
        Incrementa o contador de uma pergunta feita.
        """
        pass

    def mais_frequente(self):
        """
        Retorna a pergunta mais feita.
        """
        pass

    def sugestoes_perguntas(self, n=3):
        """
        Retorna as n perguntas mais frequentes.
        """
        pass
