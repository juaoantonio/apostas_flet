import random as r


def Times():  # Organiza os times que receberão os placares do apostador
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


def main(equipes=Times()):  # Recebe os palpites do apostador
    base = equipes
    with open(r"base", "w", encoding="utf-8") as f:
        for placares in base:
            novo = int(input())
            base[placares] = novo
    print(base)
    return base


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


def resultados(placares=times()):  # Sorteia o número de gols que cada time fará
    base = placares
    with open(r"placares", "w", encoding="utf-8"):
        for numero in base:
            a = r.randint(
                1, 10
            )  # Posso sortear um intervalo melhor de acordo com a qualidade dos times
            base[numero] = a
        print(base)
    return base


resultados()
