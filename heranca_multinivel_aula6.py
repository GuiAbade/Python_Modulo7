# Heranca multinivel
class Usuarios:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

    def registrar_funcionario(self):
        print(f'Cadastrando usuário {self.nome}')


class Gestor(Usuarios):
    def __init__(self, nome, salario, profissao, setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel

    def definir_setor(self, setor):
        print(f'Defininfo setor para {setor}')


usuario1 = Usuarios('Camila', 5000, 'Analista de SoftWere')
gestor = Gestor('Rebeca', 7000, 'Gestora', 'Gestão de projetos')
