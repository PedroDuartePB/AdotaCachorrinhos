def interfacePrincipal():
    """
    Exibe o menu principal do programa de adoção.
    """
    print("+------------------------------------------+")
    print("|  🐾 Programa de Adoção de Cachorros 🐾   |")
    print("+------------------------------------------+")
    print("|                                          |")
    print("|  Seu novo melhor amigo espera por você!  |")
    print("|                                          |")
    print("|  [1] Cadastro do Cão                     |")
    print("|  [2] Adote um Amigo                      |")
    print("|  [3] Remover um Cão                      |")
    print("|  [4] Sair                                |")
    print("|                                          |")
    print("+------------------------------------------+")

    opcao = input("Digite o número da sua opção: ")
    return opcao


def interfaceCaes():
    return "oi"

def interfaceCadastro():
    return "oi"

def interfaceSaida():
    print("+------------------------------------------+")
    print("|                                          |")
    print("|      🐾 Obrigado por nos visitar! 🐾     |")
    print("|                                          |")
    print("|    Esperamos que encontre seu novo       |")
    print("|      melhor amigo em breve.              |")
    print("|                                          |")
    print("+------------------------------------------+")

interfacePrincipal()