#estou usando alt+127 como separador nos aquivos ⌂
#template de perfil dos dog:
#Nome⌂ID⌂Raça⌂Idade⌂Sexo⌂Extra

def getCachorroLista():
    """Apresenta a lista completa dos cachorros disponiveis"""
    with open("perfis.txt", 'r' ) as lista:
        content = lista.read()
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