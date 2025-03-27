# Herança
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(
            f'Foto tirada com a camera {self.marca}, com a qualidade de {self.megapixels} megapixels')


class CameraCelular(Camera):
    def __init__(self, marca, megapixels, qtd_de_cameras):
        super().__init__(marca, megapixels)
        self.qtd_de_cameras = qtd_de_cameras

    def aplicar_filtros(self, filtro):
        print(f'Aplicando filtro {filtro}')

    def tirar_foto(self, camera_a_utilizar):
        print(
            f'Foto tirada com a camera {self.marca}, com a qualidade de {self.megapixels} megapixels, utilizando camera {camera_a_utilizar}')


class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, hrs_maximas_gravacao):
        super().__init__(marca, megapixels)
        self.hrs_maximas_gravacao = hrs_maximas_gravacao

    def rotacionar_camera(self, direcao):
        print(f' Rotacionando camera para {direcao}')


'''
camera_celular = CameraCelular('Sony', '16mp', 4)
camera_celular.aplicar_filtros('Azul')
camera_celular.tirar_foto(2)
'''

camera_seguranca = CameraSeguranca('Sony', 'SMP', 10)
camera_seguranca.rotacionar_camera('Direita')

# Como saber se uma classe é instância(subclasse) de outra
print(issubclass(CameraCelular, Camera))
print(issubclass(CameraSeguranca, Camera))
