import os
def dicionario_com_informacoes():
    #1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
    dicionario={'nome':'Raimundo','idade':18,'cidade':'Luziânia'}
    print('Antes da att: ',dicionario,'\n')
    #2 - Utilizando o dicionário criado no item 1:
    #Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    idade_nova=int(input('Digite a nova idade do usuário: '))
    nome=dicionario['nome']
    dicionario['idade']=idade_nova
    cidade=dicionario['cidade']
    print(f'{nome} - {idade_nova} - {cidade}')
    print('Att depois de mudar a idade: ',dicionario,'\n')
    #Adicione um campo de profissão para essa pessoa;
    profissao=input('Qual a sua profissão: ')
    dicionario['profissão']=profissao
    print(f'{nome} - {idade_nova} - {cidade} - {profissao}')
    print('Att depois de adicionar uma profissão: ',dicionario,'\n')
    #Remova um item do dicionário.
    #del dicionario['cidade']
    valor_removido=dicionario.pop('cidade')
    print(valor_removido)
    print(dicionario)

def dicionario_com_numeros():
    numeros=[]
    while True:
        try:
            number=int(input('\nDigite um número: '))
            print(f'Número {number} adicionado com sucesso.\n')
            number_add={'n':number}
            numeros.append(number_add)
            valor=int(input('Deseja adicionar mais um número: 1-Sim e 2-Não\n'))
            if valor==2:
                break
            elif valor!=1:
                os.system('cls')
                print('Valor inválido...')
        except:
            print('Valor inválido...')
    print('Cada um no quadrado!!:')
    for i in range(len(numeros)):
        print(f'Quadrado {i+1}: {numeros[i]["n"]}')

def chave_especifica():
    #4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
    chaves=['chave1','chave2','chave3','chave4']
    pergunta=input('Qual o nome da chave: ')
    if pergunta in chaves:
        print('Existe')
    else:
        print('Não existe')

def contar_frequência():
    #5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
    frequencia={}
    frase=input('Digite uma frase: ')
    palavra=frase.split()
    for i in palavra:
        if i not in frequencia:
            frequencia[i]=1
        else:
            frequencia[i]+=1
    for palavra, contagem in frequencia.items():
        print(f"A palavra '{palavra}' apareceu {contagem} vezes.")
def main():
    contar_frequência()

if __name__=='__main__':
    main()