from datetime import date

def adicionando_gasto(lista):
    nome = input("nome do produto: ")

    try:
        valor = float(input("valor: "))
        quantidade = float(input("quantidade: "))
    except (ValueError, UnboundLocalError):
        print("Erro: permitido apenas numeros ou use . ao invez de virgulas ex: 10.50")
        return
    soma = valor * quantidade
    if valor == 0:
        print("valor negativo ou igual a 0 não é valido")
        return
    else:
        dicionario = {
    "nome": nome,
    "valor":soma,
    "data": date.today().isoformat()
    }
        lista.append(dicionario)

def adicionando_lucro(lista):
    try:
        quantia = float(input("quantia recebida : "))
    except (ValueError , UnboundLocalError):
        print("Erro: permitido apenas numeros ou use . ao invez de virgulas ex: 10.50")
        return
    dicionario = {"nome":"salario",
                  "valor": quantia}
    lista.append(dicionario)

def leitura_gasto(lista):
    for numero,leitor in enumerate(lista,start=1):
        print(f"{'-'*25}\nnumero",numero)
        for chave,valor in leitor.items():
            print(chave,valor)
    print("-"*25)

def deletar_produto(lista):
    leitura_gasto(lista)
    try:
        numero = int(input("digite o numero onde esta localizado o produto para deletar"))
    except (ValueError, UnboundLocalError):
        print("erro permitido apenas numeros inteiros")
        return
    if len(lista) == 0:
        print("lista vazia")
    elif numero <= 0:
        print("Erro: numeros negativos ou igual a 0 não se enquadra em um item da lista")
    elif numero > len(lista):
        print("Error,numero do produto não encontrado")
    else:
        lista.pop(numero-1)

def total(lista):
    todo = 0
    for leitor in lista:
        todo +=  leitor["valor"]
    print(todo)

def gasto_lucro(lista,lista1):
    lucro = 0
    despesa = 0
    for l in lista: # l = lucro
        lucro += l["valor"]
    for d in lista1: # d = despesa
        despesa += d["valor"]
    return print(lucro-despesa)