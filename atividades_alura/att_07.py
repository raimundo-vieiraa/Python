class ContaBancaria:
    def __init__(self,titular,saldo):
        self._titular=titular
        self._saldo=saldo
        self._ativo=False
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return f'| Titular: {self._titular.ljust(12)} | Saldo: R${str(self._saldo).ljust(8)} | Status: {str(self._ativo).ljust(6)} |'
    
    def ativar_conta(self):
        self._ativo=True
titular1=ContaBancaria(titular='Geraldo',saldo=15000)
titular2=ContaBancaria(titular='Souza',saldo=35000)
print('Informações Iniciais:\n')
print(titular1)
print(titular2,'\n')
titular1.ativar_conta()
print('Informações após ativação:\n')
print(titular1)
print(titular2,'\n')
print('\nTitular da conta 1:',titular1.titular)
