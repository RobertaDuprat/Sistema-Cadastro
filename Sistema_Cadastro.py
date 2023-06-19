#Sistema de cadastro de clientes 

clientes = []
enderecos = []


def cadastro():
    while True: 
        print('Forneça as informações do usuário:')


        dados = {} #Dicionário que será passado com todos os dados para a lista clientes
        dados['nome'] = input('Nome:')
        dados['senha'] = input('Senha:')

        #1) Cadastro de e-mail:
        dados['email'] = input('E-mail:')
        lista = {i['email']: i for i in clientes} #variavel usada como indice e laço 'for' verificam se o e-mail já está cadastrado.
        while dados['email'] in lista: 
            dados['email'] = input('E-mail já cadastrado, tente novamente! \n Insira o e-mail:')

        #2) Login do usuário:

        dados['login'] = input('Login:')
        lista = {i['login']: i for i in clientes}
        while dados['login'] in lista:
            dados['login'] = input('Login já em uso.\n Insira outro login:')
        
        #3) Cadastro de telefone:

        dados['telefone'] = input('Telefone: ')
        lista = {i['telefone']: i for i in clientes}
        while dados['telefone'] in lista:
            dados['telefone'] = input('Telefone já cadastrado!\n Insira outro número:')
        
        clientes.append(dados) #Adiciona os dados em 'clientes'

        print('Usuário Cadastrado!')
        opcao = input('Deseja cadastrar mais alguém? (S/N)').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def cadEndereco():
    while True: 

        print('Forneça um login de usuário!')
        pesquisa = input('Login: ')
        lista = {i['login']: i for i in clientes}
        
        if pesquisa in lista:
            destino= {} #dicionário contendo apenas informações de endereço do cliente
            destino['id'] = pesquisa 
            destino['estado'] = input('Estado:')
            destino['cidade'] = input('Cidade: ')
            destino['rua'] = input('Rua e número: ')
            destino['cep'] = input('CEP:')

            enderecos.append(destino)
        else: 
        
            print('Usuário não encontrado!')
        
        opcao = input('Deseja cadastrar um novo endereço? (S/N):').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarDados():
    while True:
        print('Forneça LOGIN para consultar os dados de um usuário:')

        pesquisa = input('Login: ')

        lista = {i['login']: i for i in clientes}
        lista2 = {i['login']: i for i in enderecos}

        if pesquisa in lista and pesquisa not in lista2:
            print(f'Dados do cliente [{pesquisa.upper()}]:{lista[pesquisa]}')
            print('Endereço não cadastrado!')
        
        elif pesquisa in lista and pesquisa in lista2:
            print(f'Dados do cliente [{pesquisa.upper()}]:{lista[pesquisa]}')
            print(f'Endereços do cliente [{pesquisa.upper()}]:')
            resultado = list(filter(lambda item: item['id'] == pesquisa, enderecos))
            for i in resultado:
                print(i)
        else:
            print('Usuário não encontrado!')
        
        opcao = input('Deseja consultar outro cliente? (S/N)? ').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def mostrarClientes():
    while True:
        print('Usuários Cadastrados:')

        for i in clientes: #variável 'i' passa na lista "clientes" buscando apenas as informações com indice 'login' e 'nome', logo após retornar o output dos dados.

            print('Nome:', i['nome'], 'Login:', i['login'])
        
        opcao = input('Deseja conferir novamente ? (S/N)').strip().lower()
        if(opcao == 'n'):
            menu()
            break

def menu():
    print (' INSIRA UMA OPÇÃO ABAIXO:')
    print ('1 - Cadastrar cliente')
    print ('2 - Cadastrar endereço do cliente')
    print ('3 - Consultar cliente')
    print ('4 - Consultar banco de dados')
    print (' 0 - sair')

menu()
while True:
    x = int(input(''))
    while x > 4 or x < 0 :              #Caso não seja inserida uma das opções, o usuário tem a chance de inserir novamente.
        x = int(input('Erro! Insira novamente a opção!'))

    if x == 1:
        cadastro()
    elif x == 2:
        cadEndereco()
    elif x == 3:
        mostrarDados()
    elif x == 4:
        mostrarClientes()
    else:
        print('Encerrado!')
        break
    

