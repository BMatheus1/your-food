import os

restaurantes = [{'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizzaria Johnson', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Fasano', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome_do_programa():

    '''Exibe o nome do programa personalidado
    '''


    print('''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░██████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█
███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░██████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░██████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
█████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░██████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█
███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          
''')
    
def exibir_opcoes():

    '''Exibe o menu de opções disponíveis para o usuário
    '''

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exobe a mensagem de finalizando do app
    '''
    exibir_subtitulo('Finalizando o app ')

def voltar_ao_menu_principal():
    '''Solicita a tecla para voltar ao menu principal
    
    output:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():

    '''Exibe mensagem de opção inválida e retorna ao
    menu principal

    output:
    - Retorna ao menu principal
    '''

    print('Opção inválida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo estilizado na tela
    
    input:
    - texto: str - o texto do subtítulo
    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes
    
    input:
    - Nome do restaurante
    -Categoria
    
    output: 
    -Adiciona um novo restaurante à lista de restaurantes

    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes ')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')

    voltar_ao_menu_principal()

def listar_restaurantes():
    
    '''Lista os restaurantes presentes na tela
    
    output:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes ')

    print(f' {'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    
    '''Altera o status do restaurante de True(ativado) para False(Desativado
    
    output:
    - Altera o status do restaurante
    - Exibe na tela se foi Ativado ou Desativado
    '''

    exibir_subtitulo('Alternado estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            
            restaurante_encontrado = True

            restaurante['ativo'] = not restaurante['ativo']

            mensagem = (f'O restaurante {nome_do_restaurante} foi ativado com sucesso'
            if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso')
            
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado ')


    voltar_ao_menu_principal()
   
def escolher_opcao():
    '''Responsável por pedir ao usuário a opção escolhida do menu principal
    
    input:
    - Solicita ao usuário a opção escolhida
    
    output:
    - Executa a uma função de acordo com a opção escolhida pelo usuário
    - Exibe na tela um resultado de acordo com a opção escolhida
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
    # opcao_escolhida = int(opcao_escolhida)
        print(f'''Você escolheu a opção {opcao_escolhida}
        ''')
        if opcao_escolhida == 1: 
            print('Cadastrar Restaurante')
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            print ('Listar Restaurantes')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa
    '''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()