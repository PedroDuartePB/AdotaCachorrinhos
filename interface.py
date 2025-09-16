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
    print("|[1] Cadastro do Cão                       |")
    print("|[2] Adote um Amigo                        |")
    print("|[3] Remover um Cão                        |")
    print("|[4] Sair                                  |")
    print("|                                          |")
    print("+------------------------------------------+")

    opcao = input("Digite o número da sua opção: ")
    return opcao


def interfaceCaes():
    print("+------------------------------------------+")
    print("|        ✍️ Adicionar Novo Cão ✍️         |")
    print("+------------------------------------------+")
    print("|                                          |")
    print("|  Adicione um novo amigo para adoção!     |")
    print("|                                          |")
    nome = input("|[1] Qual o nome do cachorro? >> ")
    raca = input("|[2] Qual a Raca?             >> ")
    idade = input("|[3] Qual a Idade             >> ")
    sexo = input("|[4] Qual o Sexo?             >> ")
    print("|                                          |")
    print("+------------------------------------------+")
    print("")
    tentativa = input("Você deseja rescrever os dados? S/N ")

    if tentativa.lower() in ["não", "n"]:
        print("Cão cadastado, voltando ao menu principal.")
        return [nome, raca, idade, sexo]
    else:
        interfaceCaes()

def interfaceSaida():
    print("+------------------------------------------+")
    print("|                                          |")
    print("|      🐾 Obrigado por nos visitar! 🐾     |")
    print("|                                          |")
    print("|    Esperamos que encontre seu novo       |")
    print("|      melhor amigo em breve.              |")
    print("|                                          |")
    print("+------------------------------------------+")