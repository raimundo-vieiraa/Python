from class_module.att_10_0 import Banco

class Agencia(Banco):
    def __init__(self,nome,endereco,numero):
        super().__init__(nome,endereco)
        self._numero=numero