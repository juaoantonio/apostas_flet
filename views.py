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

    return odds


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

    return resultados


def processar_ganhos(valor_apostado):
    valor_por_jogo = valor_apostado / 10
    ganhos = []
    vitorias = 0
    for aposta, resultado, odd in zip(ler_apostas(), criar_resultados(), criar_odds()):
        if aposta == resultado:
            vitorias += 1
            ganhos.append(valor_por_jogo * odd)

            continue

        ganhos.append(0)

    return ganhos, vitorias
