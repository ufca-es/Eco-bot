from datetime import datetime
import os

class ChatBotMemory:
    def __init__(self, nome: str = "ChatBot"):
        self.nome = nome

    @staticmethod
    def history_file_path(file = "history.txt") -> str:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(base_dir, 'chatbot_data', file)

    @staticmethod
    def history(last_n: int = 5):
        """
        Retorna as últimas 'last_n' interações do histórico num arquivo .txt.
        """
        path = ChatBotMemory.history_file_path()
        if not os.path.exists(path):
            return []
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f if line.strip() and not line.startswith('===')]
        return lines[-last_n:] if len(lines) > 0 else "Histórico vazio."

    def start_session(self):
        """Escreve um cabeçalho de início de sessão no arquivo de histórico."""
        path = self.history_file_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"\n=== Sessão iniciada em {timestamp} | Persona: {self.nome} ===\n"
        with open(path, 'a', encoding='utf-8') as f:
            f.write(header)

    def log_interaction(self, pergunta: str, resposta_formatada: str) -> None:
        path = self.history_file_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        prefixo = f"{self.nome}: "
        resposta_sem_prefixo = resposta_formatada[len(prefixo):] if resposta_formatada.startswith(prefixo) else resposta_formatada
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] ({self.nome}) Você: {pergunta} || Bot: {resposta_sem_prefixo}\n"
        with open(path, 'a', encoding='utf-8') as f:
            f.write(line)

