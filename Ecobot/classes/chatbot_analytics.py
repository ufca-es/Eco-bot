"""
    Task 13: Implementação da coleta de estatísticas:
        - Número total de interações;
        - Pergunta mais feita da sessão;
        - Quantas vezes cada personalidade foi usada;
"""

from classes.chatbot_memory import ChatBotMemory
import os
path = ChatBotMemory.history_file_path()

class ChatbotAnalytics:
    @property
    def interaction_count(self):
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if not line.isspace() and not line.startswith("==="))

    @property
    def most_asked_questions(self):
        questions = {}
        invalid_starts = ("&",)
        invalid_contains = ("python.exe", ":/", "\\")  # provavelmente comando ou caminho
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Você:" not in line:
                    continue
                raw = line.split("Você:")[1].split("||")[0].strip()
                q_lower = raw.lower()
                if not raw:
                    continue
                if q_lower.startswith(invalid_starts):
                    continue
                if any(tok in q_lower for tok in invalid_contains):
                    continue
                # filtra entradas muito longas que parecem comando completo
                if len(raw) > 120:
                    continue
                questions[raw] = questions.get(raw, 0) + 1
        if questions:
            return max(questions, key=questions.get)
        return 'Dados insuficientes.'

    @property
    def count_personalities_usages(self):
        personalities = {}
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if "Persona:" in line:
                    persona = line.split("Persona:")[1].split("===")[0].strip()
                    personalities[persona] = personalities.get(persona, 0) + 1
        if personalities:
            return personalities
        return 'Dados insuficientes.'

    def __str__(self):
        return (f"Total de interações: {self.interaction_count}\n"
                f"Pergunta mais feita: {self.most_asked_questions}\n"
                f"Uso por personalidade: {self.count_personalities_usages}")

    def generate_report(self, output_path: str | None = None) -> str:
        """Gera um relatório de texto simples com estatísticas básicas.

        Parameters
        ----------
        output_path: caminho completo para salvar. Se None, salva em responses/relatorio.txt
        Returns: caminho do arquivo gerado
        """
        if output_path is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            output_path = os.path.join(base_dir, 'responses', 'relatorio.txt')

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Monta conteúdo legível
        lines = [
            "==== RELATÓRIO ECOBOT ====",
            f"Total de interações: {self.interaction_count}",
            f"Pergunta mais feita: {self.most_asked_questions}",
            "Uso por personalidade:",
        ]
        usos = self.count_personalities_usages
        if isinstance(usos, dict):
            for persona, qtd in usos.items():
                lines.append(f" - {persona}: {qtd}")
        else:
            lines.append(str(usos))

        content = "\n".join(lines) + "\n"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return output_path

    # --- Task 15: perguntas frequentes ---
    @most_asked_questions.getter
    def get_frequent_questions(self,top_n: int = 5) -> list[tuple[str, int]]:
        return self.most_asked_questions[:5]
