import os
import json
from Ecobot.classes.chatbot import ChatBot

class ChatBotLearning(ChatBot):
    def learning(self, q: str):
        """
            Learning mode: Ask the user for the correct answer and save it to learning_responses.json
        """

        message = f"{self.name}: Não sei a resposta para isso. Como eu deveria responder? (Por favor insira uma resposta apropriada): "
        new_response = input(message).strip()

        # Cancel learning
        if "esquecer" in new_response:
            return "Aprendizado cancelado. Tudo bem! 😊"

        # Loading a JSON file or creating a new one if it doesn't exist
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r', encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                data = {}

        else:
            data = {}

        data[q] = new_response

        # Register in history.txt
        self.memory.log_interaction(q, f"{message} [Resposta do usuário: {new_response}]")

        # Saving the updated data back to the JSON file
        with open(self.path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Feedback
        return f"{self.name}: Obrigado! Aprendi uma nova resposta. 😊"
