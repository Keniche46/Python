def menu():
    print('---- CALCULADORA ----')
    print('Escolha a operação: ')
    print('[1]- Adição\n[2]- Subtração\n[3]- Multiplicação\n[4]- Divisão\n[0]- Sair')
    print('---------------------')






while True:
    import time
    menu()
    escolha = int(input('Escolha a operação desejada: '))
    if escolha == 1:
        print('--------ADIÇÃO---------')
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o segundo número: '))
        resultado = num1 + num2
        print(f'Resultado {resultado}')
        print('-----------------------')
        time.sleep(0.9)
    if escolha == 2:
        print('--------SUBTRAÇÃO---------')
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o segundo número: '))
        resultado = num1 - num2
        print(f'Resultado {resultado}')
        print('--------------------------')
        time.sleep(0.9)
    if escolha == 3:
        print('--------MULTIPLICAÇÃO---------')
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o segundo número: '))
        resultado = num1 * num2
        print(f'Resultado {resultado}')
        print('------------------------------')
        time.sleep(0.9)
    if escolha == 4:
        print('--------DIVISÃO---------')
        num1 = int(input('Insira o primeiro número: '))
        num2 = int(input('Insira o segundo número: '))
        resultado = num1 / num2
        print(f'Resultado {resultado}')
        print('------------------------')
        time.sleep(0.9)
    if escolha < 0 or escolha > 3:
        print('Escolha uma das opções disponiveis')
    if escolha == 0:
        print('Progama finalizado, até a próxima.')
        break