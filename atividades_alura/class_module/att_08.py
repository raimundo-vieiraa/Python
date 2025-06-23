class ClienteBanco:
    clientes=[]
    def __init__(self,nome,idade,conta,cpf,email):
        self.nome=nome
        self.idade=idade
        self.conta=conta
        self.cpf=cpf
        self.email=email
        ClienteBanco.clientes.append(self) #Adicionar na lista da classe de forma automática.
    @classmethod
    def cliente_banco(cls):
        print(f'| {'Nome'.ljust(15)} | {'Idade'.ljust(5)} | {'Conta'.ljust(5)} | {'CPF'.ljust(14)} | {'E-mail'.ljust(20)} |')
        for cliente in cls.clientes:
            print(f'| {cliente.nome.ljust(15)} | {str(cliente.idade).ljust(5)} | {cliente.conta.ljust(5)} | {cliente.cpf.ljust(14)} | {cliente.email.ljust(20)} |')

cliente1=ClienteBanco(nome='Carlos Eduardo',idade='35',conta='112-3',cpf='987.654.321-99',email='carlos.e@exemplo.com')
cliente2=ClienteBanco(nome='Marina Oliveira',idade='22',conta='233-8',cpf='456.789.123-55',email='marina.o@exemplo.com')
cliente3=ClienteBanco(nome='Ana Beatriz',idade='28',conta='001-5',cpf='123.456.789-00',email='ana.b@exemplo.com')
ClienteBanco.cliente_banco()