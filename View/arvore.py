def mostrar_arvore(familia):

    print("\nÁRVORE GENEALÓGICA\n")

    for membro in familia:

        print(f"Nome: {membro['nome']}")

        print(f"Pai: {membro['pai']}")

        print(f"Mãe: {membro['mae']}")

        print("-------------------")