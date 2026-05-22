class Membro:
    def __init__(
            self,
            nome,
            idade,
            sexo,
            doencas=None,
            pai="",
            mae="",
            fumante=False,
            sedentario=False
    ):
        self.nome = nome.strip()
        self.idade = int(idade)
        self.sexo = sexo.strip()
        self.doencas = doencas or []
        self.pai = pai.strip()
        self.mae = mae.strip()
        self.fumante = bool(fumante)
        self.sedentario = bool(sedentario)

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "sexo": self.sexo,
            "doencas": self.doencas,
            "pai": self.pai,
            "mae": self.mae,
            "fumante": self.fumante,
            "sedentario": self.sedentario
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            nome=dados.get("nome", ""),
            idade=dados.get("idade", 0),
            sexo=dados.get("sexo", ""),
            doencas=dados.get("doencas", []),
            pai=dados.get("pai", ""),
            mae=dados.get("mae", ""),
            fumante=dados.get("fumante", False),
            sedentario=dados.get("sedentario", False)
        )