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

def getId():
    id = 0
    with open("perfis.txt", "r") as lista:
        for lines in lista:
            id += 1
    return id+1


def cadastraNewCachorro(newDog:list):
    t = ''
    if newDog:
        for dado in newDog:
            t = t + str(dado).strip()
        t = t.strip()

    with open("perfis.txt", "a") as lista:
        lista.write(f"\n{getId()}{t}")

cadastraNewCachorro(["marcio", "caramelo", "2", "M"])