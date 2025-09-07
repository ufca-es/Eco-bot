import random
from helpers import personalidades

random.seed(0)

bot = personalidades["formal"]

entradas = [
    "onde descartar pilhas usadas?",
    "posso jogar vidro no lixo comum?",
    "o que e reciclagem?",
    "quais plasticos sao reciclaveis?",
    "posso jogar oleo na pia?",
    "papel engordurado recicla?",
    "onde jogo eletrônicos?"  # desconhecida
]

for e in entradas:
    print("Você:", e)
    print(bot.responder(e))
    print("-")

