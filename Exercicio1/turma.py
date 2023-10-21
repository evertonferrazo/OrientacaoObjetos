class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.alunos = []
        self.professor = None

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

    def remomer_aluno(self, aluno):
        self.alunos.remove(aluno)

    def definir_prof(self, professor):
        self.professor = professor

    def get_nome_prof(self):
        if self.professor:
            return self.professor.get_nome()
        else:
            print("Nenhum professor atribuído")
    