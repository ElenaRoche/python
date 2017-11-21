def cambiadordevocales():
    texto=raw_input("Escribe un texto")
    for cont in range(0,len(texto),1):
        if texto[cont]=='A' or texto[cont]=='a'or texto[cont]=='E' or texto[cont]=='e' or texto[cont]=='I' or texto[cont]=='i' or texto[cont]=='O' or texto[cont]=='o':
          print'u', #Se ponen las comas para que todas la letras del nuevo texto se escriban en la misma linea
        else:
            print texto[cont], #Se ponen las comas para que todas la letras del nuevo texto se escriban en la misma linea
cambiadordevocales()
        
    
