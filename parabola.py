def parabola():
    import math
    a=float(input("Valor de a: "))
    b=float(input("Valor de b: "))
    c=float(input("Valor de c: "))
    if (a==0):
        sol1=(-c/b)
        print "La solucion es:x= ",sol1
    elif (b==0):
        sol2=(-c/a)**(1/2)
        print "La solucion es:x= ",sol2
    elif (c==0):
        sol3=0
        sol4=(-b/a)
        print "La solucion es:x= ",sol3,"y x= ",sol4
    else:
        raiz=(b**2-4*a*c)**(1/2)
        denominador=2*a
        sol5=(-b+raiz)/denominador
        sol6=(-b-raiz)/denominador
        print "La solucion es:x= ",sol5,"y x= ",sol6
parabola()





























        
