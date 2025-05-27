#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
number=int(input('Escolha um número e eu irei dizer se ele é par ou impar:'))
if number%2==0:
    print(f'Seu número é {number} e ele é par') #Usando o print(f'') para retorna a string
else:
    print('Seu número é',number, 'e ele é impar') #sem usar o print(f'') para retorna a string

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade=int(input('Quantos anos você tem:'))
if idade<=0:
    print('Você tem que nascer primeiro!')
if idade<=12:
    print('Você ainda é uma criança.')
elif 13<idade<18:
    print('Você ainda é um adolescente.')
else: 
    print('Parabéns você já é de maior.') 

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
usuario=('Rai')
senha='123456'
usuario_login=input('Digite o nome de usúario: ')
senha_login=input('Digite sua senha: ')
if (usuario==usuario_login)and( senha == senha_login ):
    print(f'Bem vindo {usuario}, em que posso ajuda-lo?')
else:
    print('Informações incorretas')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

x=int(input('Me diga a coordenada x:'))
y=int(input('Me diga a coordenada y:'))
if x > 0 and y > 0:
    print(f'O ponto está no primeiro quadrante: {x}x e {y}y')
elif x < 0 and y > 0:
    print(f'O ponto está no segundo quadrante: {x}x e {y}y')
elif x < 0 and y < 0:
    print(f'O ponto está no terceiro quadrante: {x}x e {y}y')
elif x > 0 and y < 0:
    print(f'O ponto está no quarto quadrante: {x}x e {y}y')
else:
    print(f'O ponto está localizado no eixo de origem: {x}x e {y}y')
        