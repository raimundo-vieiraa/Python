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

def finalizar_app():
    os.system('cls')
    print('Finalizando operação')

def escolher_opcao():
    opcao_escolhida=int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Restaurantes Cadastrados')
        case 2:
            print('Listar Restaurante')
        case 3:
            print('Ativar Restaurante')
        case _:
            finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opçoes_do_programa()
    escolher_opcao()
if __name__ == '__main__':
    main()