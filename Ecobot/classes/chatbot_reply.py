import random
import unicodedata
import string
from .chatbot_memory import ChatBotMemory
from rapidfuzz import process

class ChatBotReply:
    def __init__(self, data: tuple):
        self.stop_words = {'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se',
             'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou',
             'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso',
             'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles',
             'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa',
             'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses',
             'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua',
             'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele',
             'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve',
             'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja',
             'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem',
             'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos',
             'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá',
             'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos',
             'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos',
             'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam',
             'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram',
             'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver',
             'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam'}
        self.name = data[0]
        self.responses = data[1]
        self.keywords = data[2]

        # Registering in history.txt
        self.memory = ChatBotMemory(self.name)
        self.memory.start_session()

    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def remove_accents(text):
        nfkd_form = unicodedata.normalize('NFD', text)
        return nfkd_form.encode('ascii', 'ignore').decode('utf-8')

    def remove_stop_words(self, text):
        stop_words_norm = {self.remove_accents(word.lower()) for word in self.stop_words}
        return [word for word in text if word.lower() not in stop_words_norm]

    def normalize(self, text):
        text = text.lower()
        text = self.remove_punctuation(text)
        text = self.remove_accents(text)
        text = self.remove_stop_words(text.split())
        return ' '.join(text) if text else 'empty'

    def reply(self, q: str, learning_responses: dict, threshold = 85):
        from .chatbot_learning import ChatBotLearning

        # Converts the input to lower case and remove spaces, punctuations, accents and stop words.
        question_norm  = self.normalize(q)

        # unpack and merge the responses learned with the personality responses
        merged_responses = {**self.responses, **learning_responses}

        # Default response if nothing is found
        final_r = f"{self.name}: Desculpe, não sei a resposta para isso."

        # Preeparing normalized questions for matching
        questions_registered = list(merged_responses.keys())
        questions_norm = [self.normalize(q_) for q_ in questions_registered]


        # Rapidfuzz to find the most similar question_norm in the normalized cadastred questions
        question_most_likely, score, idx = process.extractOne(question_norm, questions_norm)

        # Try fuzzy matching
        if score > threshold:

            # found the original question that matches the input, by the index
            matched_key = questions_registered[idx]

            # select a random response from the list of responses for that question
            options = merged_responses[matched_key]

            # if options is a list, choose a random one
            final_r = f"{self.name}: {random.choice(options) if type(options) == list else options}"


        # Try matching by keywords
        else:

            found = False

            for quest, kws in self.keywords.items():
                for kw in kws:
                    if self.normalize(kw) in question_norm:
                        final_r = f"{self.name}: {random.choice(merged_responses[quest])}"
                        found = True
                        break
                if found:
                    break

            if not found:
                # don't know the answer, activate learning mode.
                learning_instances = ChatBotLearning((self.name, self.responses, self.keywords))
                final_r = learning_instances.learning(q)

        # Log the interaction in history.txt
        self.memory.log_interaction(q, final_r)
        return final_r