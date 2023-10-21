from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    