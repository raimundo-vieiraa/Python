class Livro:
    livros=[]
    def __init__(self,titulo,autor,ano_publicação):
        self._titulo=titulo
        self._autor=autor
        self._ano_publicação=ano_publicação
        self._disponivel=True
        Livro.livros.append(self)
    def __str__(self):
        return f'| Titulo: {self._titulo.ljust(35)} | Autor: {self._autor.ljust(25)} | Ano: {str(self._ano_publicação).ljust(7)} | Disponivél: {self.disponivel.ljust(2)} |'
    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❎'
    def emprestar(self):
        self._disponivel = not self._disponivel
    @classmethod
    def verificar_disponibilidade(cls):
        ano_do_livro=int(input('Qual o ano do livro:'))
        for i in Livro.livros:
            if ano_do_livro==i._ano_publicação:
                print(f'| Titulo: {i._titulo.ljust(35)} | Autor: {i._autor.ljust(25)} | Ano: {str(i._ano_publicação).ljust(7)} | Disponivél: {i.disponivel.ljust(2)} |')

