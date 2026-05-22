import matplotlib.pyplot as plt


def gerar_grafico(resultados):

    doencas = []
    riscos = []

    for doenca, dados in resultados.items():

        doencas.append(doenca)
        riscos.append(dados["risco"])

    plt.bar(doencas, riscos)

    plt.xlabel("Doenças")
    plt.ylabel("Risco (%)")

    plt.title("Análise de Risco Genético")

    plt.show()
