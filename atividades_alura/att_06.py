"""
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
"""
class Pessoa:
    def __init__(self,nome='',idade=0,profissao=''):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
    
    def __str__(self): #Retorna uma string
        return f'| {self.nome.ljust(15)} | {str(self.idade).ljust(5)} | {self.profissao.ljust(15)} |'
    
    def aniversario(self):
        self.idade+=1
        return self.idade
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22) 
    
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()
pessoa1.aniversario()
pessoa3.aniversario()
print("Informações após aniversário:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)