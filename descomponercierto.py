def descomponer():
    x=2
    numero=input("Dime un numero a descomponer")
    while (numero!=1):
        if (numero%x==0):
            print x
        else:
            x=x+1
        numero=numero/x
descomponer()
