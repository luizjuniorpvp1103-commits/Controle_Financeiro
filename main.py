import json
import task
import time

# Salvando dados em json
try:
    with open("lucro.json","r") as lucro:
        lucro = json.load(lucro)
except FileNotFoundError:
    lucro = []
    print("criando lista vazia de lucro")
except FileNotFoundError:
    lucro = []
    print("criando lista vazia de lucro")

try:
    with open("gastos.json","r") as gasto:
        gasto = json.load(gasto)
except json.JSONDecodeError:
    gasto = []
    print("criando lista vazia de gasto")
except FileNotFoundError:
    gasto = []
    print("criando lista vazia de lucro")

comando = 0

while comando != 6 :

    try:
        print("(1) adicionar")
        print("(2) ler")
        print("(3) deletar")
        print("(4) total")
        print("(5) lucro-gasto")
        print("(6) Quit")
        comando = int(input())

    except (ValueError , UnboundLocalError):
        print("permitido apenas numeros inteiros")
        continue


    match comando:
        case 1:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except (ValueError ,UnboundLocalError):
                print("comando não conhecido")
                continue
            if pergunta == 1:
                task.adicionando_gasto(gasto)
                with open("gastos.json","w",encoding="utf-8") as arquivo:
                    json.dump(gasto,arquivo,indent=4)
            else:
                print("comando não reconhecido")

        case 2:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except (ValueError, UnboundLocalError):
                print("comando não conhecido")
            if pergunta == 1:
                task.leitura_gasto(gasto)
            elif pergunta == 2:
                task.leitura_gasto(lucro)
            else:
                print("comando não reconhecido")

        case 3:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except (ValueError, UnboundLocalError):
                print("comando não conhecido")
            if pergunta == 1:
                task.deletar_produto(gasto)
            elif pergunta == 2:
                task.deletar_produto(lucro)
            else:
                print("comando não reconhecido")

        case 4:
            try:
                pergunta = int(input("(1) gasto (2) lucro "))
            except (ValueError, UnboundLocalError):
                print("comando não conhecido")
            if pergunta == 1:
                task.total(gasto)
            elif pergunta == 2:
                task.total(lucro)
            else:
                print("comando não reconhecido")

        case 5:
            task.gasto_lucro(lucro, gasto)

        case 6:
            print("saindo em ...")
            for tempo in range(10, 0, -1):
                print(tempo)
                time.sleep(0.3)
            else:
                print("comando não reconhecido")
                continue
        case _:
            print("comando não conhecido")

