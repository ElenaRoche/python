def contadorpareseimpares():
    suma=0
    resto=0
    impares=0
    numero=input("Dime un numero")
    while(numero>0):
        resto=numero%10
        if resto%2==0:
            suma=suma+1
        if resto%2!=0:
            impares=impares+1
        numero=numero/10
    print "Tiene",suma,"cifras pares y tiene",impares,"cifras impares"
    
contadorpareseimpares()
