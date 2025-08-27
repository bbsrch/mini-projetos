import random
from time import sleep

forca = [
"""
         +---+
         |   |
             |
             |
             |
             |
================""",
"""
         +---+
         |   |
         O   |
             |
             |
             |
================""",
"""
         +---+
         |   |
         O   |
         |   |
             |
             |
================""",
"""
         +---+
         |   |
         O   |
        /|   |
             |
             |
================""",
"""
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
================""",
"""
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
================""",
"""
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
================"""
]

lista = ['CHOCOLATE', 'SAPATO', 'DINAMARCA', 'VIDEOGAME', 'LANTERNA', 'TORTA', 'ITAQUAQUECETUBA', 'LIQUIDIFICADOR']
palavra = random.choice(lista)
inicio = []
historico = []
tentativas = 6
print('JOGO DA FORCA'.center(40,'-'))
for letra in palavra:
    inicio.append('_')

while tentativas > 0:
    print('=' * 40)
    erros = 6 - tentativas
    print(forca[erros])
    for letra in inicio:
        print(letra, end=' ')
    adv = ''
    print(f'\n\033[36mVocê tem {tentativas} tentativa(s) restantes.\033[m')
    while not adv.isalpha():
        adv = str(input('Digite uma LETRA: ')).upper().strip()
        while adv in historico:
            print('\033[33mLetras já digitadas:', ", ".join(historico))
            adv = str(input('\033[mVocê já tentou essa letra, digite outra: ')).upper().strip()
    if adv not in palavra:
        print(f'\033[31m{adv} não está na palavra!\033[m')
        sleep(1)
        tentativas -= 1
    for e, letra in enumerate(palavra):
        if letra == adv:
            inicio[e] = letra
    historico.append(adv)
    if '_' not in inicio:
        break
if tentativas > 0:
    print(f'\n\033[33mParabéns! Você acertou a palavra: {palavra}')
else:
    erros = 6 - tentativas
    print(forca[erros])
    print(f'\n\033[31mVocê perdeu! A palavra era: {palavra}')