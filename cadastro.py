from time import sleep

#estou usando ; como separador nos aquivos 
#template de perfil dos dog:
#ID;Nome;Raça;Idade;Sexo
def cadastraNewCachorro(newDog:dict) -> None:
    """Adiciona um novo perfil de um cachorro na "base de dados", altera diretamente o texto"""
    with open("perfis.txt", "a") as lista:
        lista.write(f"{generateId()};")
        for key in newDog:
            newDog[key] = newDog[key].strip()
            newDog[key] = newDog[key].upper()
            if key != "sexo":
                lista.write(f"{newDog[key]};")
            else:
                lista.write(f"{newDog[key]}\n")


def getDadosCachorro() -> list:
    """Retorna a lista completa dos cachorros cadastrados pela ordem da matricula"""
    with open("perfis.txt", 'r') as lista:
        content = []
        for linha in lista:
            content.append(linha.strip().split(';'))        
        return content


def getCachorroPerfil(nome:str=None, raça:str=None, idade:str=None,\
                        sexo:str=None, id:str=None) -> list:
    """Retorna uma lista dos perfis de cachorros que atendem certos requisitos.
    \nParametros devem ser recebidos como string e o programa verifica se estes existem.
    \npesquisa nome ; possui raça ; possui idade até x ; possui sexo x ; possui id == x"""
    perfis = getDadosCachorro()
    busca = []

    if id == None and nome == None and raça == None and idade == None and sexo == None:
        busca = getDadosCachorro()
    else:
        for p in perfis:
            if id:
                if p[0] == id:
                    busca.append(p)
            elif nome:
                if nome in p[1]:
                    busca.append(p)
            elif raça:
                if p[2] == raça:
                    busca.append(p)
            elif idade:
                if genIdade(p[3]) <= genIdade(idade):
                    busca.append(p)
            elif sexo:
                if sexo == p[4]:
                    busca.append(p)

    if len(busca) == 0:
        busca.append("  << SEM RESULTADOS DISPONIVEIS >>  ")
        
    return busca


def generateId() -> int:
    id = 1
    with open("perfis.txt", "r") as lista:
        for lines in lista:
            id += 1
    return id

def genIdade(idade:str):
    try:
        newIdade = float(idade)
    except ValueError:
        match idade:
            case '1/12':
                newIdade = 0.08
            case '2/12':
                newIdade = 0.16
            case '3/12':
                newIdade = 0.25
            case '4/12':
                newIdade = 0.3
            case '5/12':
                newIdade = 0.4
            case '6/12':
                newIdade = 0.5
            case '7/12':
                newIdade = 0.58
            case '8/12':
                newIdade = 0.6
            case '9/12':
                newIdade = 0.75
            case '10/12':
                newIdade = 0.83
            case '11/12':
                newIdade = 0.9
            case _:
                newIdade = 0
    finally:
        return newIdade

def adotarCachorro(id:str=None) -> None:
    """Imprime os dados do cachorrinho a ser adotdo e remove ele da base de cachorros disponíveis para adoção."""

    adotado = getCachorroPerfil(None,None,None,None,id)[0]
    if adotado == "  << SEM RESULTADOS DISPONIVEIS >>  ":
        print(adotado)
        sleep(1)
    else:
        print("|         Aproveite seu novo Amigo         |")
        print(f"| Nome: {adotado[-4]}")
        print(f"| Raça: {adotado[-3]}")
        print(f"| Idade: {adotado[-2]}")
        print(f"| Sexo: {adotado[-1]}")

        deletaCadastro(adotado[0])
        sleep(2)


def deletaCadastro(id:str=None) -> None:
    """""Deleta um cadastro de acordo com o seu número de matricula (informado como str)"""
    backup = getDadosCachorro()
    newData = []


    for dados in backup:
        if int(dados[0]) < int(id):
            l = f"{dados[-5]};{dados[-4]};{dados[-3]};{dados[-2]};{dados[-1]}\n"
            newData.append(l)
        elif int(dados[0]) > int(id):
            l = f"{int(dados[-5])-1};{dados[-4]};{dados[-3]};{dados[-2]};{dados[-1]}\n"
            newData.append(l)

    with open("perfis.txt", "w") as lista:
        pass
   
    with open("perfis.txt", "w+") as lista:
        for perfil in newData:
            lista.write(perfil)

