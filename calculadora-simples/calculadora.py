def linha():
    print('-'*30)


print('Calculadora simples'.center(30))
linha()
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Escolha o cálculo a ser feito: +, -, *, /")
    op = input("Digite a operação: ")
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Não há como dividir um número por zero!")
    else:
        print("Operação inválida!")
    linha()
    print(f'O resultado de {num1} {op} {num2} é {resultado}')
    linha()
    while op not in 'SN':
        op = str(input("Deseja continuar? [S/N]: ").upper().strip()[0])
    if op == "N":
        linha()
        break
print('Fim do programa! Até logo!')