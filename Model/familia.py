from Model.membro import Membro


class Familia:
    def __init__(self, membros=None):
        self.membros = membros or []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def buscar_por_nome(self, nome):
        nome_normalizado = nome.strip().lower()

        for membro in self.membros:
            if membro.nome.lower() == nome_normalizado:
                return membro

        return None

    def listar_nomes(self):
        return [membro.nome for membro in self.membros]

    def to_list(self):
        return [membro.to_dict() for membro in self.membros]

    @classmethod
    def from_list(cls, dados):
        return cls([Membro.from_dict(item) for item in dados])
