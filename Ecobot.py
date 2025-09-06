class Ecobot:
    def __init__(self, mode):
        self.mode = mode

    #@mode.setter
    #@mode.getter

    def __str__(self):
        return f"Ecobot mode is {self.mode}"

class Educativo(Ecobot):
    def __init__(self):
        super().__init__("Educativo")
        pass

class Quiz(Ecobot):
    def __init__(self):
        super().__init__("Quiz")
        pass

class Comunitario(Ecobot):
    def __init__(self):
        super().__init__("Comunitario")
        pass