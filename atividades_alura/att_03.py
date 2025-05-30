import os
#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
lista_numeros=[1,2,3,4,5,6,7,8,9,10]
lista_nomes=['João','Maria','Pedro','Arthur']
lista_ano=[2006,2025]

def numeros_1_a_10():
    #2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
    for numero in lista_numeros:
        print('.',int(numero))

def numeros_impares_soma():
    #3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
    soma_impares=0
    for numero in lista_numeros:
        if numero%2==1:
            soma_impares += numero
    print('Soma dos números impares: ',soma_impares)
    #ou
    print()
    print('Números impares usando range:')
    for i in range(1,10,2):
        print('.',i)

def numeros_pares():
    print('Npumeros pares usando lista:')
    for numero in lista_numeros:
        if numero%2==0:
            print('.',numero)
    #ou
    print()
    soma_pares=0
    print('Números pares usando range:')
    for i in range(2,11,2):
        soma_pares += i
        print('.',soma_pares)

def numeros_10_a_0():
    #4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    for numero in reversed(lista_numeros):
        print('.',numero)

    for numero in range(len(lista_numeros)-1,-1,-1):
        print(numero)

def tabuada_1_a_10():
    #5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
    numero=int(input('Escolha um número para imprimir a sua tabuada de 1 a 10: '))
    for i in lista_numeros:
        if numero:
            tabuada=numero*i
        print('Tabuada: ',tabuada)
    print()
    #Com range:
    for r in range(1,11,1):
        if numero:
            tabuada2=numero*r
        print('Tabuada com range: ',tabuada2)

def soma_lista():
    #6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
    try:
        quantos_numeros_somar=int(input('Quando números você quer somar: '))
        lista_n=[]
        for i in range(quantos_numeros_somar):
            numero_escolhido=int(input(f'Digite o {i+1}o número: '))
            lista_n.append(numero_escolhido)
        soma=0
        for number in lista_n:
            if number:
                soma=soma+number
        print(soma)
    except:
        print('Por favor coloque números inteiro e válidos')

def media_dos_valores_da_lista():
    #7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
    lista_media=[]
    while True:
        while True:
            try:
                valores=float(input(f'Digite um valor: '))
                lista_media.append(valores)
                break 
            except:
                print('Por favor, coloque um valor válido...')
                continue
        while True:
            try:
                    deseja_continuar=int(input('Deseja adicionar mais um número? SIM -> 1 | NÃO -> 2: '))
                    if deseja_continuar==1:
                        break
                    elif deseja_continuar==2:
                        break
                    else:
                        os.system('cls')
                        print('Por favor, coloque um valor válido...')
            except:
                os.system('cls')
                print('Por favor, coloque um valor válido...')
        if deseja_continuar==2:
            break
    for i in lista_media:
        print(i)
    media=sum(lista_media)/len(lista_media)
    print(f'A média dos valores da lista é {media:.2f}')

def entender_range():
    for i in range(1,10,2):
        print(i)

def guarda_defs():
    numeros_1_a_10()
    numeros_impares_soma()
    numeros_pares()
    numeros_10_a_0()
    entender_range()
    tabuada_1_a_10()
    soma_lista()
    media_dos_valores_da_lista()

def main():
    media_dos_valores_da_lista()

if __name__ == '__main__':
    main()