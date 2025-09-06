from Ecobot import *

def get_mode():
    while True:
        mode = input("Please enter the mode of Ecobot: ")
        if mode in ["Educativo", "Comunitário", "Quiz"]:
            return Ecobot(mode)

def starting ():
    bot = get_mode()

    print(50 * "=")
    print(bot)
    print(50 * "=")

    return bot

