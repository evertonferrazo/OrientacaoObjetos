from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super.__init__(nome)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas)/len(self.notas)
        else:
            return 0 
        
        