def gerar_alertas(risco):
    if risco >= 70:
        return "Risco alto. Recomendado procurar orientação médica e fazer acompanhamento preventivo."

    if risco >= 40:
        return "Risco moderado. Recomendado melhorar hábitos e manter exames em dia."

    if risco >= 20:
        return "Risco leve. Recomendado observar sintomas e histórico familiar."

    return "Baixo risco."
