import cadastro
from time import sleep

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
    opcao = int(input("Digite o número da sua opção: "))
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
    print("|[3] Qual a Idade em anos?              ")
    idade = input("|[Digite meses como uma fração x/12] >> ")
    sexo = input("|[4] Qual o Sexo?             >> ")
    print("|                                          |")
    print("+------------------------------------------+")
    print("")
    tentativa = input("Você confirma as alterações? S/N ")

    if tentativa.lower() in ["sim", "s"]:
        print("Cão cadastado, voltando ao menu principal.")
        cadastro.cadastraNewCachorro({"nome":nome, "raca":raca, "idade":idade, "sexo":sexo})
 
def interfaceAdocao(nome:str=None, raça:str=None, idade:str=None,\
                        sexo:str=None, id:str=None):
    matricula = 'start'
    lista = cadastro.getDadosCachorro()
    while matricula not in ["0", '']:
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
        print("| Digite o id [n] do cão:                  |")
        print("| Digite P para pesquisa inteligente       |")
        print("| [0] voltar ao menu                       |")
        print("+------------------------------------------+")

        matricula = input().strip()
        if matricula in ['0']:
            print(" ")
        elif matricula.lower() in ['p', 'pesquisa']:
            busca = {'nome':"", 'raça':"", 'idade':"", 'sexo':""}
            for key in busca:
                p = input(f"| Preferência de {key} [Enter para pular]:  |\n")
                if p == None:
                    busca[key] = None
                else:
                    busca[key] = p.lower()

            lista = cadastro.getCachorroPerfil(busca['nome'], busca['raça'],
                                               busca['idade'], busca['sexo'], None)
        
        else:
            cadastro.adotarCachorro(matricula)
            lista = cadastro.getDadosCachorro()

def interfaceRemoverCao():
    print("+------------------------------------------+")
    print("|  🗑️ Remover um Cão do Cadastro 🗑️       |")
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

    if opcao == "1":
        print("")
        id = input("Digite o ID do cão para o remover: ")
        cadastro.deletaCadastro(id.strip())
    elif opcao == "2":
        print("")
    else:
        print("Opção inválida, digite novamente")
        sleep(1)
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

