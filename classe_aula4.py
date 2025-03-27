# Métodos comuns
# Métodos de Classe(Class Methods)    -  @classmethod
# Métodos estáticos (Static Methods)  -  @classmethod
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram,
              self.placa_de_video, self.sistema_operacional)

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de video - Baixo custo')

    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de video - Alto Nivel')

    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False


# Configuração p/ cliente de escritorio
computador1 = Computador.computador_escritorio('8gb')
# Configuração para clientes de trabalho pesados (jogos, videos, 3d)
computador2 = Computador.computador_configuracao_pesado('16gb')
computador1.exibir_dados_do_computador()
print('===========================')
computador2.exibir_dados_do_computador()


print(Computador.roda_programas_pesados(10))
