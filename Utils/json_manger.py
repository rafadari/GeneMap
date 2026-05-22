import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_FAMILIAS = BASE_DIR / "Data" / "familias.json"
CAMINHO_USUARIOS = BASE_DIR / "Data" / "usuarios.json"


def carregar_json(caminho, padrao):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return padrao


def salvar_json(caminho, dados):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    return carregar_json(CAMINHO_FAMILIAS, [])


def salvar_dados(dados):
    salvar_json(CAMINHO_FAMILIAS, dados)


def carregar_usuarios():
    usuarios = carregar_json(CAMINHO_USUARIOS, [])

    if not usuarios:
        usuarios = [{"usuario": "admin", "senha": "admin"}]
        salvar_usuarios(usuarios)

    return usuarios


def salvar_usuarios(usuarios):
    salvar_json(CAMINHO_USUARIOS, usuarios)
