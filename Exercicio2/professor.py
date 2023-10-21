from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, titulacao_maxima):
        super().__init__(nome)
        self.titulacao_maxima = titulacao_maxima

    def get_titulacao_maxima(self):
        return self.titulacao_maxima
