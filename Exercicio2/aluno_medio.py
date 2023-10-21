from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def verificar_aprovacao(self):
        media = self.calcular_media
        return media >=6
    
    def informacoes_aprovacao(self):
        aprovado = self.verificar_aprovacao()
        status = "Aprovado" if aprovado else "Reprovado"
        return print(f"{self.get_nome()} ({self.matricula}): {status}")
    
    