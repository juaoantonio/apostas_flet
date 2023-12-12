import random as r
import tela_confrontos as tc

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""
############################################# CRIA AS ODDS ###################################################
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


def criar_odds():
    # Cria as odds para cada confronto em porcentagem
    odds = []
    for i in range(10):
        odds.append(r.randint(120, 500) / 100)

    with open("odds.txt", "w") as arquivo:
        for odd in odds:
            arquivo.write(str(odd) + "\n")


def ler_odds():
    try:
        odds = []
        with open("odds.txt", "r") as arquivo:
            for linha in arquivo:
                odds.append(float(linha.strip()))

        return odds

    except FileNotFoundError:
        criar_odds()
        return ler_odds()


def ler_apostas():
    apostas = []
    with open("apostas.txt", "r") as arquivo:
        for linha in arquivo:
            apostas.append(linha.strip().split(","))

    lista_inteiros = []
    for i in range(len(apostas)):
        lista_inteiros.append([int(apostas[i][0]), int(apostas[i][1])])

    return lista_inteiros


def criar_resultados():
    resultados = []
    for i in range(10):
        resultados.append([r.randint(0, 3), r.randint(0, 3)])

    with open("resultados.txt", "w") as arquivo:
        for resultado in resultados:
            arquivo.write(str(resultado[0]) + "," + str(resultado[1]) + "\n")


def ler_resultados():
    resultados = []

    try:
        with open("resultados.txt", "r") as arquivo:
            for linha in arquivo:
                resultados.append(linha.strip().split(","))

        lista_inteiros = []
        for i in range(len(resultados)):
            lista_inteiros.append([int(resultados[i][0]), int(resultados[i][1])])

        return lista_inteiros

    except FileNotFoundError:
        criar_resultados()
        return ler_resultados()


def processar_ganhos(valor_apostado):
    valor_por_jogo = valor_apostado / 10
    ganhos = []
    vitorias = 0
    for aposta, resultado, odd in zip(ler_apostas(), ler_resultados(), ler_odds()):
        if aposta == resultado:
            vitorias += 1
            ganhos.append(valor_por_jogo * odd)

            continue

        ganhos.append(0)

    return ganhos, vitorias


def ler_confrontos():
    confrontos = []

    with open("confrontos.txt", "r") as arquivo:
        for linha in arquivo:
            confrontos.append(linha.strip().split(","))

    return confrontos


def mostrar_confrontos_placar_ganhos():
    confrontos = ler_confrontos()
    ganhos, vitorias = processar_ganhos(100)
    placares = ler_resultados()

    confrontos_e_ganhos = []

    for confronto, ganho, placar in zip(confrontos, ganhos, placares):
        confrontos_e_ganhos.append([confronto, placar, ganho])

    return confrontos_e_ganhos


print(mostrar_confrontos_placar_ganhos())
