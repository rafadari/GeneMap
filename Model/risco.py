class Risco:
    def __init__(self, doenca, porcentagem, nivel):
        self.doenca = doenca
        self.porcentagem = porcentagem
        self.nivel = nivel

    def to_dict(self):
        return {
            "doenca": self.doenca,
            "porcentagem": self.porcentagem,
            "nivel": self.nivel
        }