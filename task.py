from datetime import date
import json

def expense(lista):
    nome = input("nome do produto: ")
    try:
        valor = float(input("valor: "))
        quantidade = int(input("quantidade: "))
    except ValueError:
        print("Erro: permitido apenas numeros ou use . ao invez de virgulas ex: 10.50")
        return

    if valor <= 0:
        print("valor negativo ou igual a 0 não é valido")
        return
    if quantidade <= 0:
        valor = 1
    else:
        soma = valor * quantidade
        dicionario = {
    "nome": nome,
    "total":soma,
    "data": date.today().isoformat()
    }
        lista.append(dicionario)


def profit(lista):
    try:
        quantia = float(input("quantia recebida : "))
    except ValueError:
        print("Erro: permitido apenas numeros ou use . ao invez de virgulas ex: 10.50")
        return
    dicionario = {"nome":"salario",
                  "total": quantia}
    lista.append(dicionario)


def reading(lista):
    if len(lista) == 0:
        print("lista vazia")
        return

    for numero,leitor in enumerate(lista,start=1):
        print(f"{'-'*25}\nnumero",numero)
        for chave,valor in leitor.items():
            print(chave,valor)
    print("-"*25)


def delet(lista):
    if len(lista) == 0:
        print("lista vazia")
        return
    reading(lista)

    try:
        numero = int(input("digite o numero onde esta localizado o produto para deletar"))
    except ValueError:
        print("erro permitido apenas numeros inteiros")
        return

    if numero <= 0:
        print("Erro: numeros negativos ou igual a 0 não se enquadra em um item da lista")
    elif numero > len(lista):
        print("Error,numero do produto não encontrado")
    else:
        lista.pop(numero-1)


def adding(lista):
    todo = 0
    for leitor in lista:
        todo +=  leitor["total"]
    print(todo)

def gasto_lucro(lista1,lista2):
    lucro = 0
    despesa = 0
    for l in lista1: # l = lucro
        lucro += l["total"]
    for d in lista1: # d = despesa
        despesa += d["total"]
    print(lucro - despesa)