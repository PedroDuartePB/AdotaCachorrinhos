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


def cadastraNewCachorro(newDog:dict):
    with open("perfis.txt", "a") as lista:
        lista.write(f"\n{generateId()};")
        for key in newDog:
            if key != "sexo":
                lista.write(f"{newDog[key]};")
            else:
                lista.write(f"{newDog[key]}")

def atualizarPerfil(id:int, dados:str):
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

cadastraNewCachorro({"nome":"Princesa", "raça":"pitbul", "idade":"2", "sexo":"F"})