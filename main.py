import json
import task
import time
import os

local = os.path.dirname(os.path.abspath(__file__)) # local atual

date_past = os.path.join(local,"data") # criando diretorio.
os.makedirs(date_past, exist_ok=True) # fazendo o diretorio existir.

js_ga = os.path.join(date_past,"gasto.json")
js_lu = os.path.join(date_past,"lucro.json")

try:
    with open(js_lu,"r") as arquivo:
        lucro = json.load(arquivo)
except json.JSONDecodeError:
    lucro = []
    print("criando lista vazia de lucro")
except FileNotFoundError:
    lucro = []
    print("criando lista vazia de lucro")

try:
    with open(js_ga,"r") as arquivo:
        gasto = json.load(arquivo)
except json.JSONDecodeError:
    gasto = []
    print("criando lista vazia de gasto")
except FileNotFoundError:
    gasto = []
    print("criando lista vazia de lucro")

comando = 0

while comando != 6 :

    print("(1) adicionar")
    print("(2) ler")
    print("(3) deletar")
    print("(4) total")
    print("(5) lucro-gasto")
    print("(6) Quit")
    try:
        comando = int(input())
    except ValueError:
        print("permitido apenas numeros inteiros")
        continue

    match comando:
        case 1:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except ValueError:
                print("comando não conhecido")
                continue
            if pergunta == 1:
                task.expense(gasto)

            elif pergunta == 2:
                task.profit(lucro)
            else:
                print("comando não reconhecido")

        case 2:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except ValueError:
                print("comando não conhecido")
                continue
            if pergunta == 1:
                task.reading(gasto)
            elif pergunta == 2:
                task.reading(lucro)
            else:
                print("comando não reconhecido")

        case 3:
            if len(gasto) == 0:
                print("lista vazia")
                continue
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except ValueError:
                print("comando não conhecido")
                continue
            if pergunta == 1:
                task.delet(gasto)
            elif pergunta == 2:
                task.delet(lucro)
            else:
                print("comando não reconhecido")

        case 4:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except ValueError:
                print("comando não conhecido")
                continue
            if pergunta == 1:
                task.adding(gasto)
            elif pergunta == 2:
                task.adding(lucro)
            else:
                print("comando não reconhecido")

        case 5:
            try:
                task.gasto_lucro(lucro, gasto)
            except json.JSONDecodeError:
                print("erro, arquivo existe")
                continue
        case 6:
            print("saindo em ...")
            for tempo in range(5, 0, -1):
                print(tempo)
                time.sleep(0.3)
            break
        case _:
            print("comando não conhecido")

 #salvando todos os dados antes de fechar a pasta.
with open(js_lu, "w", encoding="utf-8") as arquivo:
    json.dump(lucro, arquivo, indent=4)
with open(js_ga, "w", encoding="utf-8") as arquivo:
    json.dump(gasto, arquivo, indent=4)
