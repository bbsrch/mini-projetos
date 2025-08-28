import json

def mostrar_menu():
    print('LISTA DE TAREFAS'.center(30,'-'))
    print('1. Adicionar tarefa')
    print('2. Ver tarefas')
    print('3. Remover tarefa')
    print('4. Sair')

def linha():
    print('-'*30)

def salvar(tarefas, nome_arquivo='tarefas.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def carregar(nome_arquivo='tarefas.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []