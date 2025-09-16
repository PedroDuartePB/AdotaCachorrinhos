#estou usando ; como separador nos aquivos 
#template de perfil dos dog:
#Nome;ID;Raça;Idade;Sexo

def getCachorroLista():
    """Apresenta a lista completa dos cachorros disponiveis
    ordenando atraves de categorias"""
    with open("perfis.txt", 'r') as lista:
        content = []
        for linha in lista:
            content.append(linha.strip().split(';'))
        print(content)

getCachorroLista()