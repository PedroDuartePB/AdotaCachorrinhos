import cadastro

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
        cadastro.cadastraNewCachorro({"nome":nome, "raca":raca, "idade":idade, "sexo":sexo})
    else:
        interfaceCaes()
 
def interfaceAdocao():
    lista = cadastro.getDadosCachorro()

    print("+------------------------------------------+")
    print("|          ❤️ Adotar um Amigo ❤️          |")
    print("+------------------------------------------+")
    print("|                                          |")
    print("|  Pronto para encontrar seu parceiro?     |")
    print("|  Qual cão você gostaria de adotar?       |")
    print("|                                          |")
    for item in lista:
        print(f"| [{item[0]}] Nome: {item[1]} Raça: {item[2]}\
              \n|     Idade: {item[3]} anos Sexo: {item[4]}")
        print("|                                          |")
    print("|                                          |")
    print("+------------------------------------------+")

    matricula = input("Digite o id [n] do cão: ")


    cadastro.adotarCachorro(matricula.strip())

def interfaceRemoverCao():
    print("+------------------------------------------+")
    print("|  🗑️ Remover um Cão do Cadastro 🗑️      |")
    print("+------------------------------------------+")
    print("|                                          |")
    print("|  Digite o nome do cão que deseja remover |")
    print("|  e confirme para deletá-lo do sistema.   |")
    print("|                                          |")
    print("|  [1] ID do cão a ser removido:           |")
    print("|                                          |")
    print("|  [2] Voltar ao menu principal            |")
    print("|                                          |")
    print("+------------------------------------------+")

    opcao = input("Digite sua opção: ")

    if opcao == "2":
        interfacePrincipal()
    elif opcao == "1":
        print("")
        id = input("Digite o ID do cão para o remover: ")
        cadastro.deletaCadastro(id.strip())
    else:
        print("Opção inválida, digite novamente")
        print("")
        interfaceRemoverCao()

def interfaceSaida():
    print("+------------------------------------------+")
    print("|                                          |")
    print("|      🐾 Obrigado por nos visitar! 🐾     |")
    print("|                                          |")
    print("|    Esperamos que encontre seu novo       |")
    print("|      melhor amigo em breve.              |")
    print("|                                          |")
    print("+------------------------------------------+")
