from classes.chatbot import ChatBot

class ChatbotInterface(ChatBot):
    def learning(self):
        """
            -Salvar essa nova pergunta e resposta em um arquivo separado (ex: aprendizado.txt);
        ADAPTAÇÃO WEB: Este método não usa mais input() nem salva arquivos.
        Ele apenas retorna uma mensagem específica que "sinaliza" para a
        interface web que o bot precisa aprender. A interface cuidará de
        pedir a nova resposta ao usuário e salvá-la no arquivo.
        """
        return f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder?"