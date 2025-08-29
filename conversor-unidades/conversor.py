from modulos import *
from time import sleep

dic = {'C': '°C', 'F': '°F', 'K': 'K'}

while True:
    op = ''
    comp = ''
    menu()
    while not op.isnumeric():
        op = input('\033[33mDigite uma opção:\033[m ').strip()

    if op == '1':
        print("\n\033[7;36m CONVERSÃO DE COMPRIMENTO \033[m")
        comp = ler_numero('Digite um comprimento (ex: 1,75): ')
        mostrar_unidades(['km', 'm', 'cm', 'mm'])
        opc = str(input('\033[33mDe qual unidade? \033[m').lower().strip())
        opc2 = str(input('\033[33mPara qual unidade? \033[m').lower().strip())
        resultado = conv_comp(comp, opc, opc2)
        if resultado is not None:
            print(f'\n\033[32m✅ {comp:.2f}{opc} equivale a {resultado:.2f}{opc2}\033[m\n')
        else:
            print('\033[31m❌ Unidade inválida!\033[m')

    elif op == '2':
        print("\n\033[7;36m CONVERSÃO DE PESO \033[m")
        comp = ler_numero('Digite um peso (ex: 55,60): ')
        mostrar_unidades(['t', 'kg', 'g', 'mg'])
        opc = str(input('\033[33mDe qual unidade? \033[m').lower().strip())
        opc2 = str(input('\033[33mPara qual unidade? \033[m').lower().strip())
        resultado = conv_peso(comp, opc, opc2)
        if resultado is not None:
            print(f'\n\033[32m✅ {comp:.2f}{opc} equivale a {resultado:.2f}{opc2}\033[m\n')
        else:
            print('\033[31m❌ Unidade inválida!\033[m')

    elif op == '3':
        print("\n\033[7;36m CONVERSÃO DE TEMPERATURA \033[m")
        comp = ler_numero('Digite uma temperatura (ex:25,9): ')
        mostrar_unidades(['C', 'F', 'K'])
        opc = str(input('\033[33mDe qual unidade? \033[m').upper().strip())
        opc2 = str(input('\033[33mPara qual unidade? \033[m').upper().strip())
        resultado = conv_temp(comp, opc, opc2)
        if resultado is not None:
            print(f'\n\033[32m✅ {comp:.2f}{dic[opc]} equivale a {resultado:.2f}{dic[opc2]}\033[m\n')
        else:
            print('\033[31m❌ Unidade inválida!\033[m')

    elif op == '4':
        print("\033[36mAté mais! 👋\033[m".center(40, '-'))
        break
    else:
        print('\033[31m❌ Opção inválida!\033[m')

    sleep(1)
