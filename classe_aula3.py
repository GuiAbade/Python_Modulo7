# Variáveis de uma classe
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

        def ligar(self):
            print('Estou ligando o compytador')


Computador.sistema_operacional = 'Linux'
computador = Computador('Dell', '8gb', 'NVIDIA')
computador.marca = 'Asus'
print(computador.marca)
print(computador.sistema_operacional)
Computador.sistema_operacional = 'Mac'
computador2 = Computador('Asus', '2gb', 'ATI')
print(computador2.sistema_operacional)
