#estou usando ; como separador nos aquivos 
#template de perfil dos dog:
#ID;Nome;Raça;Idade;Sexo
def cadastraNewCachorro(newDog:dict) -> None:
    """Adiciona um novo perfil de um cachorro na "base de dados", altera diretamente o texto"""
    with open("perfis.txt", "a") as lista:
        lista.write(f"{generateId()};")
        for key in newDog:
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
                    print(id)
                    busca.append(p)
            elif nome:
                if nome in p[1]:
                    busca.append(p)
            elif raça:
                if p[2] == raça:
                    busca.append(p)
            elif idade:
                if int(p[3]) <= int(idade):
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

def adotarCachorro(id:str=None) -> None:
    """Imprime os dados do cachorrinho a ser adotdo e remove ele da base de cachorros disponíveis para adoção."""

    adotado = getCachorroPerfil(None,None,None,None,id)[0]
    print(adotado)
    print("|--------Aproveite seu novo Amigo----------|")
    print(f"| Nome: {adotado[-4]}")
    print(f"| Raça: {adotado[-3]}")
    print(f"| Idade: {adotado[-2]}")
    print(f"| Sexo: {adotado[-1]}")
    print("|------------------------------------------|")

    deletaCadastro(adotado[0])


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



#talvez um dia seja possivel implementar isso aqui
def makeBackup() -> None:
        pass


def forceRollBack() -> None:
    pass

def atualizarPerfil(id:int):
    dados = {"nome": "", "raça": "", "idade": "", "sexo": ""}

    with open("perfis.txt", "w+") as lista:
        lista.write(f"\n{generateId()};")
        for key in dados:
            if key != "sexo":
                lista.write(f"{dados[key]};")
            else:
                lista.write(f"{dados[key]}")

