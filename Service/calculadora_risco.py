PESOS_DOENCAS = {
    "diabetes": 12,
    "hipertensao": 10,
    "hipertensão": 10,
    "cancer": 8,
    "câncer": 8,
    "alzheimer": 8,
    "cardiopatia": 10,
    "asma": 6,
    "depressao": 7,
    "depressão": 7
}


def calcular_risco(
        doenca,
        pai_doente=False,
        mae_doente=False,
        avo_doente=False,
        irmao_doente=False,
        fumante=False,
        sedentario=False,
        ja_possui=False
):
    if ja_possui:
        return 100

    doenca_normalizada = doenca.strip().lower()
    risco = PESOS_DOENCAS.get(doenca_normalizada, 5)

    if pai_doente:
        risco += 25

    if mae_doente:
        risco += 25

    if avo_doente:
        risco += 12

    if irmao_doente:
        risco += 10

    if fumante:
        risco += 10

    if sedentario:
        risco += 8

    return min(risco, 100)
