#estou usando ; como separador nos aquivos 
#template de perfil dos dog:
#ID;Nome;Raça;Idade;Sexo


def getDadosCachorro():
    """Apresenta a lista completa dos cachorros disponiveis
    ordenando atraves de categorias"""
    with open("perfis.txt", 'r') as lista:
        content = []
        for linha in lista:
            content.append(linha.strip().split(';'))
        return content


def getCachorroPerfil():
    """Busca o perfil de um cachorro pelo nome ou id do cadastro"""
    with open("perfis.txt", 'r' ) as lista:
        lista.readline()

def generateId():
    id = 0
    with open("perfis.txt", "r") as lista:
        for lines in lista:
            id += 1
    return id+1


def cadastraNewCachorro(newDog:list):
    adicao = ''
    if newDog:
        for dado in newDog:
            if dado == newDog[-1]:
                t = t + str(dado).strip()
            else:
                t = t + str(dado).strip() + ";"
        t = t.strip()

    with open("perfis.txt", "a") as lista:
        lista.write(f"\n{generateId()};{adicao}")


def atualizarPerfil(id, dados):
    newData = ''
    with open("perfis.txt", "r+") as lista:
        perfil = lista.readline((id-1))
        for dado in perfil:
            change = input(f"Gostaria de alterar {dados}? [S/N] >> ")
            if change in ['s', 'sim', '1']:
                if dado == perfil[-1]:
                    newData = newData + str(dado).strip()
                else:
                    newData = newData + str(dado).strip() + ";"

        newData = newData.strip()
        lista[(id-1)].write(f"\n{generateId()};{newData}")
