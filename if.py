def menu():
    print('-----------------------------')
    print('[1]- Ver estoques\n[2]- Adicionar aos estoques\n[3]- Remover dos estoques\n[0]- Sair')
    print('-----------------------------')







estoque_1 = []
estoque_2 = []



while True:
    menu()
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print('-----------------------------')
        print('Escolha qual estoque você deseja visualizar:\n[1]- Primeiro estoque\n[2]- Segundo estoque\n[0]- Voltar')
        print('-----------------------------')
        escolha_estoque = int(input('Escolha o estoque: '))
        if escolha_estoque == 1:
            print('-----------------------------')
            print('Seu primeiro estoque:')
            for i in estoque_1:
                print(i)
            print('-----------------------------')
        if escolha_estoque == 2:
            print('-----------------------------')
            print('Seu segundo estoque:')
            for a in estoque_2:
                print(a)
            print('-----------------------------')
        if escolha_estoque == 0:
            continue
    if escolha == 2:
        print('-----------------------------')
        print('Escolha qual estoque você deseja adicionar o produto:\n[1]- Primeiro estoque\n[2]- Segundo estoque\n[0]- Voltar')
        print('-----------------------------')
        escolha_add_estoque = int(input('Qual estoque você deseja adicionar o produto? '))
        if escolha_add_estoque == 1:
            add = input('Insira o produto que deseja adicionar: ').title().strip()
            if add in estoque_1:
                print('Esse produto já está em estoque.')
            else:
                estoque_1.append(add)
            print('-----------------------------')
            print('Produto adicionado.')
            print('-----------------------------')
        if escolha_add_estoque == 2:
            add_2 = input('Insira o produto que deseja adicionar: ').title().strip()
            if add_2 in estoque_2:
                print('Esse produto já está em estoque.')
            else:
                estoque_2.append(add_2)
            print('-----------------------------')
            print('Produto adicionado.')
            print('-----------------------------')
        if escolha_add_estoque == 0:
            continue
    if escolha == 3:
        print('-----------------------------')
        print('Escolha qual estoque você deseja remover o produto:\n[1]- Primeiro estoque\n[2]- Segundo estoque\n[0]- Voltar')
        print('-----------------------------')
        delete_escolha = int(input('Insira o estoque que você deseja remover o produto: '))
        if delete_escolha == 1:
            print('-----------------------------')
            for i in estoque_1:
                print(i)
            print('-----------------------------')
            deleted_item = input('Qual item você deseja remover: ').title().strip()
            if deleted_item in estoque_1:
                estoque_1.remove(deleted_item)
                print('Produto removido')
                print('-----------------------------')
            else:
                print('Produto inválido')
                print('-----------------------------')
        if delete_escolha == 2:
            print('-----------------------------')
            for a in estoque_2:
                print(a)
            print('-----------------------------')
            deleted_item = input('Qual item você deseja remover: ').title().strip()
            if deleted_item in estoque_2:
                estoque_2.remove(deleted_item)
                print('Produto removido')
                print('-----------------------------')
            else:
                print('Produto inválido')
                print('-----------------------------')
    if escolha < 0 or escolha > 3:
        print('-----------------------------')
        print('Escolha uma das opções disponiveis.')
        print('-----------------------------')
    if escolha == 0:
        break