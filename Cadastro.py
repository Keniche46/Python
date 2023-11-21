users_cadastrado = {}

def menu():
    print('-------------------------')
    print('[1]- Cadastrar-se\n[2]- Fazer login\n[0]- Sair')
    print('-------------------------\n')


def cadastro():
    print('-------------------------')
    defi_user = input('Insira seu nome: ').title()
    res_user = validaçao_user(defi_user)
    if res_user == False:
        print('-------------------------')
        print('Insira um nome com mais de 3 caracteres.')
        cadastro()
    else:
        cadastro_senha(defi_user)

def cadastro_senha(user):
    defi_senha = str(input('Defina uma senha: '))
    validaçao_senha(defi_senha)
    res_senha = validaçao_senha(defi_senha)
    if res_senha:
        print('-------------------------')
        print('Usuário cadastrado com sucesso!')
        users_cadastrado[user] = defi_senha
        return users_cadastrado
    else:
        print('-------------------------')
        print('Digite uma senha com 8 ou mais caracteres.')
        cadastro_senha(defi_user)


def validaçao_user(user):
    if len(user) >= 3:
        return True
    else:
        return False
    
def validaçao_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False
    

def login():
    user_atual = input('Insira seu nome de usuário: ').title()
    res = validaçao_login(user_atual)
    if res:
        senha_atual = users_cadastrado[user_atual]
        senha_inserida = str(input('Insira sua senha: '))
        if senha_inserida == senha_atual:
            print('-------------------------')
            print('Bem-vindo.')
            print('-------------------------')
        else:
            print('-------------------------')
            print('Acesso negado.')
            print('-------------------------')
    else:
        print('-------------------------')
        print('Nome de usuario incorreto.')


def validaçao_login(user_atual):
    if user_atual in users_cadastrado:
        return True
    else:
        return False


while True:
    menu()
    try:
        escolha1 = int(input('Escolha a opção desejada: '))
    
    except ValueError:
        print('-------------------------')
        print('Insira uma opção válida.')
    
    else:
        if escolha1 == 1:
            cadastro()
        elif escolha1 == 2:
            login()
        elif escolha1 == 0:
            print('-------------------------')
            print('Até logo!')
            print('-------------------------')
            break
        
        else:
            print('-------------------------')
            print('Escolha uma opção válida')
