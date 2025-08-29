import json
import matplotlib.pyplot as plt
from datetime import datetime

# ---------- Funções de arquivo ----------
def salvar(dados, arquivo='despesas.json'):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar(arquivo='despesas.json'):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ---------- Funções auxiliares ----------
def formatar_moeda(valor: float) -> str:
    # Formata o valor no estilo brasileiro (R$ 1.234,56)
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def validar_data(data: str) -> bool:
    # Valida se a data está no formato dd/mm/aaaa
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# ---------- Operações ----------
def excluir_despesa(despesas):
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return

    print("\n--- Despesas ---")
    for i, d in enumerate(despesas, start=1):
        print(f"{i}. {d['data']} - {d['categoria']} - {formatar_moeda(d['valor'])}")

    try:
        indice = int(input("Digite o número da despesa que deseja excluir: "))
        if 1 <= indice <= len(despesas):
            removida = despesas.pop(indice - 1)
            salvar(despesas)  # atualiza o arquivo JSON
            print(f"✅ Despesa removida: {removida['data']} - {removida['categoria']} - {formatar_moeda(removida['valor'])}")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Entrada inválida, digite um número.")

def mostrar_grafico(despesas):
    categorias = {}
    for d in despesas:
        cat = d["categoria"]
        categorias[cat] = categorias.get(cat, 0) + d["valor"]

    if not categorias:
        print("Nenhuma despesa para mostrar.")
        return

    total = sum(categorias.values())
    print(f"💰 Total de despesas: {formatar_moeda(total)}")

    plt.figure(figsize=(6,6))
    plt.pie(categorias.values(), labels=categorias.keys(), autopct="%.1f%%")
    plt.title("Distribuição de Despesas por Categoria")
    plt.show()

def mostrar_grafico_barras(despesas):
    categorias = {}
    for d in despesas:
        cat = d["categoria"]
        categorias[cat] = categorias.get(cat, 0) + d["valor"]

    if not categorias:
        print("Nenhuma despesa para mostrar.")
        return

    total = sum(categorias.values())
    print(f"💰 Total de despesas: {formatar_moeda(total)}")

    plt.bar(categorias.keys(), categorias.values(), color='skyblue', edgecolor='black')
    plt.title("Despesas por Categoria")
    plt.ylabel("Valor (R$)")
    plt.show()
