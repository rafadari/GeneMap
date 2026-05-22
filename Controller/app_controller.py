from Model.familia import Familia
from Model.membro import Membro
from Service.analisador import analisar_membro
from Utils.json_manger import carregar_dados, carregar_usuarios, salvar_dados, salvar_usuarios


class AppController:
    def __init__(self):
        self.familia = Familia.from_list(carregar_dados())

    def autenticar(self, usuario, senha):
        usuario = usuario.strip()
        senha = senha.strip()

        for conta in carregar_usuarios():
            if conta["usuario"] == usuario and conta["senha"] == senha:
                return True

        return False

    def cadastrar_usuario(self, usuario, senha):
        usuario = usuario.strip()
        senha = senha.strip()

        if not usuario or not senha:
            return False, "Informe usuário e senha."

        usuarios = carregar_usuarios()

        for conta in usuarios:
            if conta["usuario"] == usuario:
                return False, "Esse usuário já existe."

        usuarios.append({"usuario": usuario, "senha": senha})
        salvar_usuarios(usuarios)
        return True, "Usuário cadastrado com sucesso."

    def adicionar_membro(self, nome, idade, sexo, doencas, pai, mae, fumante, sedentario):
        if not nome.strip():
            return False, "Informe o nome do membro."

        if self.familia.buscar_por_nome(nome):
            return False, "Já existe um membro com esse nome."

        try:
            idade = int(idade)
        except ValueError:
            return False, "Idade precisa ser um número inteiro."

        if idade < 0:
            return False, "Idade não pode ser negativa."

        lista_doencas = [
            item.strip()
            for item in doencas.split(",")
            if item.strip()
        ]

        membro = Membro(
            nome=nome,
            idade=idade,
            sexo=sexo,
            doencas=lista_doencas,
            pai=pai,
            mae=mae,
            fumante=fumante,
            sedentario=sedentario
        )
        self.familia.adicionar_membro(membro)
        self.salvar_familia()
        return True, "Membro cadastrado com sucesso."

    def salvar_familia(self):
        salvar_dados(self.familia.to_list())

    def listar_membros(self):
        return self.familia.listar_nomes()

    def listar_dados_membros(self):
        return self.familia.to_list()

    def listar_doencas_conhecidas(self):
        doencas = set()

        for membro in self.familia.membros:
            for doenca in membro.doencas:
                doencas.add(doenca)

        if not doencas:
            return ["diabetes", "hipertensão", "câncer", "alzheimer", "cardiopatia"]

        return sorted(doencas)

    def analisar(self, nome_membro, doencas):
        lista_doencas = [
            item.strip()
            for item in doencas.split(",")
            if item.strip()
        ]

        if not lista_doencas:
            lista_doencas = self.listar_doencas_conhecidas()

        return analisar_membro(self.familia, nome_membro, lista_doencas)
