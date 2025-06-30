from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self._ligado=False
    
    @abstractmethod
    def ligar(self):
        pass
    
    def __str__(self):
        estado='Ligado' if self._ligado else 'Desligado'
        return f'| Marca: {self.marca.ljust(20)} | Modelo: {self.modelo.ljust(20)} | Estado: {estado.ljust(10)} |'