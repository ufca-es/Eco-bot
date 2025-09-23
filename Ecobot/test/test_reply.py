from classes.chatbot_reply import ChatBotReply
from helpers import personalities, loading_learning_responses

p = (personalities['formal']['name'], personalities['formal']['chatbot_data'], personalities['formal']['keywords'])
bot = ChatBotReply(data=p)

def test_responses():

    resposta = bot.reply("Como você funciona?", loading_learning_responses())
    # Verifica se a resposta é uma string
    assert type(resposta) == str

    respostas_esperadas = p[1]["Como você funciona?"]

    # Remove prefixo se existir
    for esperada in respostas_esperadas:
        if resposta.endswith(esperada):
            assert True
            return
    assert False, f"Resposta inesperada: {resposta}"

def test_hospitalar():

    resposta = bot.reply("hospitalar?", loading_learning_responses())
    # Verifica se a resposta é uma string
    assert type(resposta) == str

    respostas_esperadas = p[1]["Como descartar lixo hospitalar?"]

    # Remove prefixo se existir
    for esperada in respostas_esperadas:
        if resposta.endswith(esperada):
            assert True
            return
    assert False, f"Resposta inesperada: {resposta}"

