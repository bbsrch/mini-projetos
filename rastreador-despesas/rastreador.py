from modulos import *
from time import sleep

despesas = carregar()

while True:
    print('\033[36m' + 'RASTREADOR DE DESPESAS'.center(40, '=') + '\033[0m')
    print('\033[33m1.\033[0m Adicionar despesa')
    print('\033[33m2.\033[0m Listar despesas')
    print('\033[33m3.\033[0m Mostrar gráfico de pizza')
    print('\033[33m4.\033[0m Mostrar gráfico de barras')
    print('\033[33m5.\033[0m Excluir despesa')
    print('\033[33m6.\033[0m Sair')
    op = input('\033[32mDigite uma opção: \033[0m')

    if op == '1':
        valor = float(input('\033[32mDigite o valor da despesa: \033[0m'))
        categoria = input('\033[32mCategoria da despesa (ex: transporte): \033[0m').capitalize()
        data = input('\033[32mData (dd/mm/aaaa): \033[0m')

        if not validar_data(data):
            print("\033[31m⚠️ Data inválida! Use o formato dd/mm/aaaa.\033[0m")
        else:
            despesas.append({'valor': valor, 'categoria': categoria, 'data': data})
            salvar(despesas)
            print('\033[32m✅ Despesa adicionada com sucesso!\033[0m')
            sleep(1)

    elif op == '2':
        if not despesas:
            print("\033[31mNenhuma despesa cadastrada.\033[0m")
        else:
            for d in despesas:
                print(f"{d['data']} - {d['categoria']} - {formatar_moeda(d['valor'])}")
                sleep(0.5)

    elif op == '3':
        mostrar_grafico(despesas)

    elif op == '4':
        mostrar_grafico_barras(despesas)

    elif op == '5':
        excluir_despesa(despesas)
        sleep(1)

    elif op == '6':
        break

    else:
        print('\033[31m⚠️ Opção inválida!\033[0m')

print('\033[35m👋 Programa finalizado com sucesso!\033[0m')
