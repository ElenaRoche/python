def reorganizacioncifras():
    n_cifras=0
    numero=input("Dime un numero")
    while numero>0:
        numero=numero/10
        n_cifras=n_cifras+1
    return n_cifras
    print n_cifras
reorganizacioncifras()
    
