from .chatbot_reply import ChatBotReply
import json
import os

class ChatBot(ChatBotReply):
    """
    Representa um estilo de resposta do chatbot (ex: formal, engraçado, rude...).
    Esta versão foi adaptada para funcionar com interfaces web.
    """
    def __init__(self, data:tuple):
        super().__init__(data)
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "responses", "learning_responses.json")

        # Garantee the file exists
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
