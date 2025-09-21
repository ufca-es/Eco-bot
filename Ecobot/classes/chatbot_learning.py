import os
import json
from Ecobot.classes.chatbot import ChatBot

class ChatBotLearning(ChatBot):
    def learning(self):
        """
            -Salvar essa nova pergunta e resposta em um arquivo separado (ex: aprendizado.txt);
        """
        message = f"{self.nome}: Não sei a resposta para isso. Como eu deveria responder? (Por favor insira uma resposta apropriada): "
        new_response = input(message).strip()

        if not new_response or "esquecer" in new_response:
            return "Aprendizado cancelado. Tudo bem! 😊"

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "responses", "learning_responses.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Carrega JSON existente (ou inicia vazio)
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                data = {}

        data[self.pergunta] = new_response
        # Registrar histórico
        self.memory.log_interaction(self.pergunta, message + "Users input:" + new_response)

        # Salva todo o dicionário formatado
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Feedback
        return f"{self.nome}: Obrigado! Aprendi uma nova resposta. 😊"
