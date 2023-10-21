from aluno import Aluno
from professor import Professor
from curso import Curso
from turma import Turma
from disciplina import Disciplina

professor_marcos = Professor("Marcos", "Prof01")
professor_lovisi = Professor("Lovisi", "Prof02")
aluno_everton = Aluno("Everton", "090008926")
aluno_amanda = Aluno("Amanda", "0900038927")

curso_python = Curso("Python")
turma_a = Turma("Turma A")
turma_b = Turma("Turma B")

disciplina_oriobj = Disciplina("Orientação Objetos")
dispciplina_ihm = Disciplina("Interface Homem Máquina")

turma_a.add_aluno(aluno_everton)
turma_b.add_aluno(aluno_amanda)

turma_a.definir_prof(professor_marcos)
turma_b.definir_prof(professor_lovisi)

nome_prof_turma_a = turma_a.get_nome_prof()
print("Nome do professor da Turma A: ", nome_prof_turma_a)

nomes_alunos_turma_a = [aluno.get_nome () for aluno in turma_a.alunos]
print("Nomes dos alunos da Turma A: ", nomes_alunos_turma_a)

professores_curso_python = [turma.professor.get_nome() for turma in [turma_a, turma_b] if turma.professor]
print("Nomes dos professores do Curso de Python: ", professores_curso_python)

alunos_curso_python = [aluno.get_nome() for turma in [turma_a, turma_b] for aluno in turma.alunos]
print("Nomes dos alunos do Curso Python:", alunos_curso_python)

alunos_registrados = list(set(alunos_curso_python))
print("Nomes dos alunos registrados em curso:", alunos_registrados)

disciplinas_curso_python = [disciplina.nome for turma in [turma_a, turma_b] for disciplina in turma.disciplinas]
print("Disciplinas do Curso Python:", disciplinas_curso_python)

aluno_esta_na_turma = aluno_amanda in turma_a.alunos
print("Amanda está na Turma A?", aluno_esta_na_turma)

aluno_esta_no_curso = any(aluno in curso_python.alunos for aluno in [aluno_amanda, aluno_everton])
print("Amdanda ou Everton está no Curso Python?", aluno_esta_no_curso)

turma_esta_no_curso = turma_a in curso_python.turmas
print("Turma A está no Curso Python?", turma_esta_no_curso)

turma_a.remover_aluno(aluno_amanda)
print("Amanda removida da Turma A:", [aluno.get_nome() for aluno in turma_a.alunos])

curso_python.remover_turma(turma_a)
print("Turma A removida do Curso Python:", [turma.codigo for turma in curso_python.turmas])

curso_python.remover_aluno(aluno_everton)
print("Everton removido do Curso Python:", [aluno.get_nome() for aluno in curso_python.alunos])