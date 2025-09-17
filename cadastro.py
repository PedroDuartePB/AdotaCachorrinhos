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

def atualizarPerfil(id:int):
    dados = {"nome": "", "raça": "", "idade": "", "sexo": ""}
    change = ''

    with open("perfis.txt", "r+") as lista:
        for i in range (0, id):
            perfil = lista.readline().split(';')
        
        dados["nome"] = perfil[-4]
        dados["raça"] = perfil[-3]
        dados["idade"] = perfil[-2]
        dados["sexo"] = perfil[-1]

        for key in dados:
            change = input(f"Gostaria de mudar {key}? \n")

            if change in ['s', 'sim', '1']:
                change = input(f"insira novo {key} >> ")
                dados[key] = change
        
