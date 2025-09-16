import interface
import cadastro

interface.interfacePrincipal()

def navegação_de_Paginas():
    resultado = interface.interfacePrincipal()

    while resultado >= 4 :
       if resultado == 1:
         cadastro.cadastraCachorro()
       elif resultado == 2:
           cadastro.getCachorroLista()
       elif resultado == 3:
          cadastro.delCachorro()
       elif resultado == 4:
          interface.interfaceSaida()
          break

   
        
      