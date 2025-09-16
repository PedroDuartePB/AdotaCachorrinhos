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

#estou usando ; como separador nos aquivos 
#template de perfil dos dog:
#Nome;ID;Raça;Idade;Sexo;Extra

def getCachorroLista():
    """Apresenta a lista completa dos cachorros disponiveis"""
    with open("perfis.txt", 'r') as lista:
        content = []
        for linha in lista:
            content.append(linha.strip().split(';'))
        print(content)


def getCachorroPerfil():
    """Busca o perfil de um cachorro pelo nome ou id do cadastro"""
    with open("perfis.txt", 'r' ) as lista:
        lista.readline()


def cadastraCachorro():
    """Adiciona um novo perfil a lista dos cachorros"""
    with open("perfis.txt", 'a' ) as insert:
        insert.write()


def delCachorro():
    """Exclui perfil da lista"""
    with open("perfis.txt", 'w+' ) as exclui:
        exclui.read()


def alteraPerfil():
    """Alteação de dados do cachorro."""
    with open("perfis.txt", 'r+' ) as data:
        data.read()

getCachorroLista()
=======
