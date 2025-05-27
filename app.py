import os

def exibir_nome_do_programa():
    print("""
███████████████████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█▄─▄███▄─▄█▄─█─▄█▄─▄▄─█▄─▄▄▀█▄─█─▄███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
██─██─██─▄█▀██─██▀██─███▄▀▄███─▄█▀██─▄─▄██▄─▄█████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      """)

def exibir_opçoes_do_programa():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')



def escolher_opcao():
    opcao_escolhida=int(input('Escolha uma opção: '))
    if opcao_escolhida==1:
        print('Restaurantes Cadastrados')
    elif opcao_escolhida==2:
        print('Listar Restaurante')
    elif opcao_escolhida==3:
        print('Ativar Restaurante')
    else:
        finalizar_app

def finalizar_app():
    os.system('cls')
    print('Finalizando operação')

def main():
    exibir_nome_do_programa()
    exibir_opçoes_do_programa()
    escolher_opcao()
    finalizar_app()
if __name__ == '__main__':
    main()