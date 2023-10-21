from aluno_medio import AlunoEnsinoMedio
from aluno_superior import AlunoGraduacao
from professor import Professor

def obter_notas():
    notas = []
    notas_string = input("Insira a nota (para encerrar deixe em branco): ")

    while notas_string.strip() != " ":
        try:
            nota = float(notas_string)
            notas.append(nota)
        except ValueError:
            print("Por favor, insira um valor númerico válido. ")

        notas_string = input("Insira a próxima nota (para encerrar deixe em branco): ")

    return notas

nome_aluno_medio = input("Digite o nome do aluno do EM: ")
matricula_aluno_medio = input("Digite a matrícula do aluno do EM: ")
aluno_medio = AlunoEnsinoMedio(nome_aluno_medio, matricula_aluno_medio)
print("Insira as notas do aluno do EM: ")
aluno_medio.adicionar_nota(*obter_notas())

nome_aluno_superior = input("Digite o nome do aluno de Graduação: ")
matricula_aluno_superior = input("Digite a matrícula do aluno de Graduação: ")
aluno_superior = AlunoGraduacao(nome_aluno_superior, matricula_aluno_superior)
print("Insira as notas do aluno de Graduação:")
aluno_superior.adicionar_nota(*obter_notas())

nome_professor = input("\nDigite o nome do professor: ")
titulacao_maxima = input("Digite a titulação máxima do professor: ")
professor_jane = Professor(nome_professor, titulacao_maxima)

print("Informações de aprovação para Aluno do Ensino Médio:")
print(aluno_medio.informacoes_aprovacao())

print("Informações de aprovação para Aluno de Graduação:")
print(aluno_superior.informacoes_aprovacao())

print("Informações do Professor:")
print(f"{professor_jane.get_nome()} - Titulação Máxima: {professor_jane.get_titulacao_maxima()}")