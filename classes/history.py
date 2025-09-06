class Historico:
    """
    Gerencia o histórico de interações entre usuário e bot (leitura e escrita em arquivo).
    """
    def __init__(self, arquivo: str = "historico.txt"):
        self.arquivo = arquivo
        self.interacoes = []  # Lista de tuplas (pergunta, resposta)

    def carregar(self):
        """
        Lê as interações anteriores do arquivo.
        """
        pass

    def registrar(self, pergunta: str, resposta: str):
        """
        Adiciona uma nova interação ao histórico.
        """
        pass

    def salvar(self):
        """
        Salva o histórico atualizado no arquivo.
        """
        pass

    def ultimas_interacoes(self, n=5):
        """
        Retorna as últimas n interações.
        """
        pass