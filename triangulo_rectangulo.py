def triangulo_rectangulo():
    a=input("Cuanto mide un cateto")
    b=input("cuanto mide el otro cateto")
    c=input("cuanto mide la hipotenusa")
    if (c*c==a*a+b*b):
        print ("Efectivamente, es un triangulo rectangulo")
    else:
        print ("No vas bien, no es un triangulo rectangulo")
triangulo_rectangulo()
