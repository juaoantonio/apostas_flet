import random as r
import tela_confrontos as tc

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################# CRIA AS ODDS ###################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def odd():
    with open(
        r"odds_times.txt",
        "r",
        encoding="utf-8",
    ) as f:
        data = [linha.split(",") for linha in f]
        columns = data[0]
        db = dict()
        for id, column in enumerate(columns):
            db[column] = [item[id] for item in data[1:]]
        return db

def odds():
    base = odd()
    with open(r"odds_times.txt", "a", encoding = "utf-8") as f:
        for c in base:
            base[c] = (r.randint(1, 5) + r.randint(1, 99)/100)
    print(base)
    return base

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
################################## RECEBER OS PLACARES APOSTADOS ##########################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def equipes():  # Organiza os times que receberão os placares do apostador
    with open(
        r"Times.txt",
        "r",
        encoding="utf-8",
    ) as f:
        data = [linha.split(",") for linha in f]
        columns = data[0]
        db = dict()
        for id, column in enumerate(columns):
            db[column] = [item[id] for item in data[1:]]
        return db




def apostas():  # Recebe os palpites do apostador
    base = equipes()
    resultados = salvar()
    with open(r"base", "w", encoding="utf-8") as f:
        for a in base:
            for b in resultados:
                base[a] = b
    print(base)
    return base
apostas()                

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
######################################## GERA PLACARES ALEATÓRIOS############################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def times():  # Função que organiza os placares que serão sorteados
    with open(
        r"resultados_random.txt",
        "r",
        encoding="utf-8",
    ) as f:
        data = [linha.split(",") for linha in f]
        columns = data[0]
        db = dict()
        for id, column in enumerate(columns):
            db[column] = [
                item[id] for item in data[1:]
            ]  # Cada time recebe uma chave com o valor zerado
        return db


def resultados():  # Sorteia o número de gols que cada time fará
    base = times()
    with open(r"placares", "w", encoding="utf-8"):
        for numero in base:
            a = r.randint(1, 10)
            if a > 8:
                b = r.randint(5,10)
            else:
                b = r.randint(0,4)
            base[numero] = b
    
    return base

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
####################################### COMPARA APOSTA COM OS PLACARES ####################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def comparacao():
    apostas = apostas()
    resultados = resultados()
    win_loss = []
    for a, b in zip(apostas, resultados):
        if a != b:
            win_loss.append(0)
        else:
            win_loss.append(1)
    print(win_loss)
    return win_loss
