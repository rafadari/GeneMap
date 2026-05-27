class Risco:
    def __init__(self, doenca, porcentagem):
        self.doenca = doenca
        self.porcentagem = porcentagem
        self.nivel = self.definir_nivel()

    def definir_nivel(self):
        if self.porcentagem >= 70:
            return "ALTO"

        if self.porcentagem >= 40:
            return "MODERADO"

        if self.porcentagem >= 20:
            return "BAIXO"

        return "MINIMO"

    def to_dict(self):
        return {
            "doenca": self.doenca,
            "porcentagem": self.porcentagem,
            "nivel": self.nivel
        }
