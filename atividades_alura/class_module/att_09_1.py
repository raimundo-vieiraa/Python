from att_09_0 import Livro
livro1=Livro(titulo='O Guia do Mochileiro das Galáxias', autor='Douglas Adams', ano_publicação=1979)
livro2=Livro(titulo='Jogador Nº 1', autor='Ernest Cline', ano_publicação=2011)
livro3=Livro(titulo='1984', autor='George Orwell', ano_publicação=1949)
livro4=Livro(titulo='Duna', autor='Frank Herbert', ano_publicação=1965)
livro5=Livro(titulo='Neuromancer', autor='William Gibson', ano_publicação=1984)
def main():
    print(livro1)
    Livro.verificar_disponibilidade()
if __name__=='__main__':
    main()