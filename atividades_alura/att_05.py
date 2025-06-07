"""
Criar uma classe e colocar 3 exemplos.
"""
class Musica:
    nome=''
    artista=''
    duracao= int

musica_salve=Musica()
musica_salve.nome='Salve Jorge - Ao Vivo'
musica_salve.artista='Mc Hariel'
musica_salve.duracao=198

musica_eu_amo_voce=Musica()
musica_eu_amo_voce='Eu Amo Você'
musica_eu_amo_voce='Tim Maia'
musica_eu_amo_voce=243

musica_dias_de_luta=Musica()
musica_dias_de_luta='Dias de Luta, Dias de Gloria'
musica_dias_de_luta='Charlie Brown Jr.'
musica_dias_de_luta=145

"""
1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
"""
class Carro:
    carros=[]
    def __init__(self, modelo, cor, ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        Carro.carros.append(self)
    def __str__(self):
        return f'| Modelo: {self.modelo.ljust(15)} | Cor: {self.cor.ljust(15)} | Ano: {self.ano} |'

corsinha=Carro('Corsa VHC','Branco','2004')

class Cliente:
    clientes=[]
    def __init__(self, nome, idade, email, cpf):
        self.nome=nome
        self.idade=idade
        self.email=email
        self.cpf=cpf
        Cliente.clientes.append(self)
    def __str__(self):
        return f'| Nome: {self.nome.ljust(15)} | Idade: {self.idade.ljust(5)} | Email: {self.email.ljust(20)} | CPF: {self.cpf} |'
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'| Nome: {cliente.nome.ljust(15)} | Idade: {cliente.idade.ljust(5)} | Email: {cliente.email.ljust(20)} | CPF: {cliente.cpf} |')
cliente1=Cliente('Raimundo','18','raimundo61@gmail.com','593.213.213-23')
cliente2=Cliente('Guilherme','17','guigamatos@gmail.com','453.289.843-21')
cliente3=Cliente('Reinaldo','34','reivieiraa@gmail.com','321.845.623-25')

Cliente.listar_clientes()
