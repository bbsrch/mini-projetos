from time import sleep

# cores
CABECALHO = "\033[7;36m"
OPCAO = "\033[33m"
RESET = "\033[m"
LINHA = "\033[35m" + "="*40 + RESET


def linha():
    print(LINHA)


def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")  # aceita vírgula como decimal
        try:
            return float(entrada)  # tenta converter para número decimal
        except ValueError:
            print("\033[31m❌ Entrada inválida! Digite apenas números.\033[m")


def menu():
    print(f"{CABECALHO}CONVERSOR DE UNIDADES{RESET}".center(40, "="))
    print(f"{OPCAO}1.{RESET} Comprimento")
    print(f"{OPCAO}2.{RESET} Peso")
    print(f"{OPCAO}3.{RESET} Temperatura")
    print(f"{OPCAO}4.{RESET} Sair")


def mostrar_unidades(lista):
    linha()
    for unidade in lista:
        print(unidade)
        sleep(0.4)
    linha()


def converter(valor, de, para, fatores):
    if de in fatores and para in fatores:
        return valor * fatores[de] / fatores[para]
    return None


def conv_comp(valor, de, para):
    fatores = {'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}
    return converter(valor, de, para, fatores)


def conv_peso(valor, de, para):
    fatores = {'t': 1000, 'kg': 1, 'g': 0.001, 'mg': 0.000001}
    return converter(valor, de, para, fatores)


def conv_temp(valor, de, para):
    # primeiro converte tudo para Celsius
    if de == 'C':
        c = valor
    elif de == 'F':
        c = (valor - 32) * 5/9
    elif de == 'K':
        c = valor - 273.15
    else:
        return None

    # converte de Celsius para a unidade desejada
    if para == 'C':
        return c
    elif para == 'F':
        return c * 9/5 + 32
    elif para == 'K':
        return c + 273.15
    return None
