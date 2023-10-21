from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, codigo):
        super().__init__(nome)
        self.codigo = codigo

    def getCordigo(self):
        return self.codigo
    
    def setCodigo(self, codigo):
        self.codigo = codigo

    