from veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,modelo,portas):
        super().__init__(marca,modelo)
        self.portas=portas
    
    def ligar(self):
        print(f'O carro {self.modelo} está ligado.')

    def __str__(self):
        return f'{super().__str__()} Portas: {str(self.portas).ljust(8)} |'