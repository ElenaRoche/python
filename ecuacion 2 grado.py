def parabola():
    a=float(input("Valor de a: "))
    b=input("Valor de b: ")
    c=input("Valor de c: ")
    if a!= 0:
        raiz=(b**2-4*a*c)**(1/2)
        denominador=2*a
        sol1=(-b+raiz)/denominador
        sol2=(-b-raiz)/denominador
        print"Tiene dos soluciones y son: ",sol1,"y",sol2
    else:
        if b!=0:
            sol3=-c/b
            print"Tiene una solucion y es ",sol3
        else:
            if c!=0:
                print"La ecuacion no tiene soluciones"
            else:
                print"La ecuacion tiene infinitas soluciones"
parabola()
