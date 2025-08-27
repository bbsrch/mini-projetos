import random
import string
from time import sleep
import modulos

arq = 'senhas.txt'
if not modulos.existe(arq):
    modulos.criar(arq)

crc = string.ascii_letters
tam = int(input('Digite o tamanho da senha: '))
qtd = int(input('Digite a quantidade de senhas geradas: '))
dig = str(input('São permitidos números na senha? [S/N] ').upper().strip())
if dig == 'S':
    crc += string.digits
sim = str(input('São permitidos símbolos na senha? [S/N] ').upper().strip())
if sim == 'S':
    crc += string.punctuation

for q in range(0, qtd):
    senhaTexto = ''
    print(f'Senha {q + 1}:', end=' ')
    for i in range(0, tam):
        senha = random.choice(crc)
        print(senha, end='')
        senhaTexto += senha
        sleep(0.25)
    modulos.cadastrar(arq, senhaTexto)
    print()
print('Senhas geradas com sucesso e guardadas no arquivo "senhas.txt"')