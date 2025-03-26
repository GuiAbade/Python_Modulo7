class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


Computador1 = Computador('Asus', '8gb', 'NVIDIA')
print(Computador1.marca)
print(Computador1.memoria_ram)
print(Computador1.placa_de_video)

Computador2 = Computador('Dell', '4gb', 'ATI')
print(Computador2.marca)
print(Computador2.memoria_ram)
print(Computador2.placa_de_video)
