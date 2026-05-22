from Service.alertas import gerar_alertas
from Service.calculadora_risco import calcular_risco


def _tem_doenca(membro, doenca):
    doencas = [item.lower() for item in membro.doencas]
    return doenca.strip().lower() in doencas


def _parentes_com_doenca(familia, membro, doenca):
    pai = familia.buscar_por_nome(membro.pai) if membro.pai else None
    mae = familia.buscar_por_nome(membro.mae) if membro.mae else None

    pai_doente = pai is not None and _tem_doenca(pai, doenca)
    mae_doente = mae is not None and _tem_doenca(mae, doenca)
    avo_doente = False

    for responsavel in [pai, mae]:
        if not responsavel:
            continue

        avo_1 = familia.buscar_por_nome(responsavel.pai) if responsavel.pai else None
        avo_2 = familia.buscar_por_nome(responsavel.mae) if responsavel.mae else None

        if (avo_1 and _tem_doenca(avo_1, doenca)) or (avo_2 and _tem_doenca(avo_2, doenca)):
            avo_doente = True

    irmao_doente = False

    for outro in familia.membros:
        mesmo_pai = membro.pai and outro.pai == membro.pai
        mesma_mae = membro.mae and outro.mae == membro.mae

        if outro.nome != membro.nome and (mesmo_pai or mesma_mae) and _tem_doenca(outro, doenca):
            irmao_doente = True

    return pai_doente, mae_doente, avo_doente, irmao_doente


def analisar_membro(familia, nome_membro, lista_doencas):
    resultados = {}
    membro = familia.buscar_por_nome(nome_membro)

    if not membro:
        return resultados

    for doenca in lista_doencas:
        doenca = doenca.strip()

        if not doenca:
            continue

        pai_doente, mae_doente, avo_doente, irmao_doente = _parentes_com_doenca(
            familia,
            membro,
            doenca
        )
        ja_possui = _tem_doenca(membro, doenca)
        risco = calcular_risco(
            doenca,
            pai_doente=pai_doente,
            mae_doente=mae_doente,
            avo_doente=avo_doente,
            irmao_doente=irmao_doente,
            fumante=membro.fumante,
            sedentario=membro.sedentario,
            ja_possui=ja_possui
        )

        resultados[doenca] = {
            "risco": risco,
            "alerta": gerar_alertas(risco),
            "fatores": {
                "pai": pai_doente,
                "mae": mae_doente,
                "avos": avo_doente,
                "irmaos": irmao_doente,
                "fumante": membro.fumante,
                "sedentario": membro.sedentario,
                "ja_possui": ja_possui
            }
        }

    return resultados


def analisar_doencas(lista_doencas):
    resultados = {}

    for doenca in lista_doencas:
        doenca = doenca.strip()

        if not doenca:
            continue

        risco = calcular_risco(doenca)
        resultados[doenca] = {
            "risco": risco,
            "alerta": gerar_alertas(risco)
        }

    return resultados
