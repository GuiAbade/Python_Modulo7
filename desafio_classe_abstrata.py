from abc import ABC, abstractmethod


class Monitor(ABC):
    @abstractmethod  # Definindo que o método é abstrato
    def aumentar_claridade(self, valor):
        pass

    @abstractmethod  # Definindo que o método é abstrato
    def reduzir_claridade(self, valor):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade em {valor}')

    def reduzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos')


monitor = MonitorFullHD()
monitor.aumentar_claridade(10)
monitor.reduzir_claridade(44)
