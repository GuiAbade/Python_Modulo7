# Polimorfismo
class Carro:
    def ligar(self):
        print('Ligando o carro')


class Moto:
    def ligar(self):
        print('Ligando a moto')


def iniciar(veiculo):
    veiculo.ligar()


carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)
