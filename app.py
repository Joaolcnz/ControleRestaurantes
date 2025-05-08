import os

restaurantes = [{'nome' : 'Piratini', 'categoria' : 'Pizzaria', 'ativo' : False},
                {'nome' : 'Hanami', 'categoria' : 'Sushi Bar', 'ativo' : False},
                {'nome' : 'La chef', 'categoria' : 'Comida italiana', 'ativo' : False}]

def exibir_titulo():

    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def opcoes():

    print('''
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar restaurante
    4. Sair
    ''')

def finalizar_app():
    os.system('cls')
    print('Finalizando o aplicativo...\n')

def voltar_ao_menu():
    input('\nAperte [ENTER] para voltar ao menu! ')
    main()

def opcao_incorreta():
    print('Opção inválida!')
    voltar_ao_menu()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes!\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n->')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:\n->')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    restaurantes.append(dados_restaurante)
    print('\n', f'{nome_restaurante} foi cadastrado!')
    voltar_ao_menu()

def listar_restaurantes():
    os.system('cls')
    print(f'{'| Nome do Restaurante'.ljust(28)} {'| Categoria'.ljust(27)} {'| Status'}')
    for x in restaurantes:
        nome = x['nome']
        categoria = x['categoria']
        ativo = 'ativado' if x['ativo'] else 'desativado'
        print( f'-> {nome.ljust(25)} | {categoria.ljust(25)} | {ativo.ljust(25)}')
    voltar_ao_menu()

def alternar_estado_restaurante():
    print('Alternar estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar:\n->')
    restaurante_encontrado = False
    for c in restaurantes:
        if nome_restaurante == c['nome']:
            restaurante_encontrado = True
            c['ativo'] = not c['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado!' if c['ativo'] else f'O restaurante {nome_restaurante} foi desativado!'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante nao encontrado')

    voltar_ao_menu()

def opcao_escolhida():

    try:
        opcao_escolhida = int(input("Escolha uma opção:\n-> "))
        print('')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_incorreta()

    except:
        opcao_incorreta()

def main():
    os.system('cls')
    exibir_titulo()
    opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()