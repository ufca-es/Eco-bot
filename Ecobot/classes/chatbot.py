from .chatbot_reply import ChatBotReply
class ChatBot(ChatBotReply):
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    Esta versão foi adaptada para funcionar com interfaces web.
    """
    def __init__(self, data:tuple):
        super().__init__(data)