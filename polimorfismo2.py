class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)


pessoa = Pessoa()
pessoa.apresentar(nome='Amanda', idade=18, profissao='Programadora')
pessoa.apresentar(nome='Amanda', idade=18,)
pessoa.apresentar(nome='Amanda', profissao='Programadora')
pessoa.apresentar(nome='Amanda')
