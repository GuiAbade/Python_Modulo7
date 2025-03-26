class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

    def desligar(self):
        print('Estou desligando')

    def exibir_dados_do_computador(self):
        print(
            f'Computador {self.marca}, com {self.memoria_ram} e q ue usa a placa de video {self.placa_de_video}')


Computador1 = Computador('Asus', '8gb', 'NVIDIA')
Computador1.ligar()
Computador1.desligar()
Computador1.exibir_dados_do_computador()
