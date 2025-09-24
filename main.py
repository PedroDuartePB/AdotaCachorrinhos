import interface  

rodando = True
while rodando:
   resultado = interface.interfacePrincipal()

   match resultado:
      case '1':
         interface.interfaceCaes()
         continue
      case '2':
         interface.interfaceAdocao()
         continue
      case '3':
         interface.interfaceRemoverCao()
         continue
      case '4':
         interface.interfaceSaida()
         rodando = False
      case '':
         interface.interfaceSaida()
         rodando = False
      case _:
         print("OPÇÂO INVALIDA TENTE NOVAMENTE")
         continue
