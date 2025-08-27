def existe(txt):
    try:
        arq = open(txt, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar(txt):
    try:
        arq = open(txt, 'wt+')
        arq.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo {txt} criado com sucesso.')

def cadastrar(txt, senha):
    try:
        arq = open(txt, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
            arq.write('{}\n'.format(senha))