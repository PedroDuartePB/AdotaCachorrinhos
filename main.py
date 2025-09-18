import interface  

rodando = True
while rodando:
   resultado = interface.interfacePrincipal()

   if resultado == 1:
      interface.interfaceCaes()
      continue
   elif resultado == 2:
      interface.interfaceAdocao()
      continue
   elif resultado == 3:
      interface.interfaceRemovercao()
      continue
   elif resultado == 4:
      interface.interfaceSaida()
      rodando = False
      
