from time import sleep
from modulos import *

tarefas = carregar()
while True:
    mostrar_menu()
    op = input('Escolha uma opção: ')
    linha()
    if op == '1':
        t = str(input('Digite a tarefa que deseja adicionar: '))
        tarefas.append(t)
        salvar(tarefas)
        print(f'Tarefa [{t}] adicionada com sucesso!')
    elif op == '2':
        if len(tarefas) == 0:
            print('Nenhum tarefa cadastrada.')
        else:
            for i, tarefa in enumerate(tarefas):
                print(f'{i+1}. {tarefa}')
                sleep(0.5)
    elif op == '3':
        if len(tarefas) == 0:
            print('Nenhum tarefa cadastrada.')
        else:
            for i, tarefa in enumerate(tarefas):
                print(f'{i+1}. {tarefa}')
                sleep(0.5)
            linha()
            while True:
                re = int(input('Qual tarefa você deseja remover?: '))
                if 0 < re <= len(tarefas):
                    removida = tarefas.pop(re-1)
                    salvar(tarefas)
                    print(f'Tarefa [{removida}] removida com sucesso!')
                    break
                else:
                    print('O número digitado é inválido!')
    elif op == '4':
        break
    else:
        print('Opção inválida!')
    sleep(1)
print('Todas as suas tarefas estão salvas para consultas futuras.')
print('Até logo!')
