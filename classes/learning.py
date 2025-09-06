class Aprendizado:
    """
    Gerencia o modo de aprendizagem do bot (novas perguntas e respostas criadas pelos usuários).
    """
    def __init__(self, arquivo: str = "aprendizado.txt"):
        self.arquivo = arquivo
        self.novos_conhecimentos = {}  # Pergunta -> Resposta

    def carregar(self):
        """
        Lê novos conhecimentos do arquivo.
        """
        pass

    def adicionar(self, pergunta: str, resposta: str):
        """
        Adiciona novo conhecimento ao aprendizado.
        """
        pass

    def salvar(self):
        """
        Salva os novos conhecimentos no arquivo.
        """
        pass
