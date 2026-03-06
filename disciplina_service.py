from repositories.disciplina_repository import DisciplinaRepository

class DisciplinaService:

    def __init__(self):
        self.repo = DisciplinaRepository()

    def criar_disciplina(self, nome, curso, dia):

        if nome == "":
            raise Exception("Nome obrigatório")

        return self.repo.criar_disciplina(nome, curso, dia)

    def listar_disciplinas(self):
        return self.repo.listar_disciplinas()

    def remover_disciplina(self, id_disciplina):
        return self.repo.remover_disciplina(id_disciplina)
