class Veiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self._ligado=False
    def __str__(self):
        estado='Ligado' if self._ligado else 'Desligado'
        return f'| Marca: {self.marca.ljust(20)} | Modelo: {self.modelo.ljust(20)} | Estado: {estado.ljust(10)} |'