def es_primo(num):
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i != 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return num

es_primo()


def descomposicion():
    x=input("Dime un numero que quieres descomponer")
    if (x%es_primo==0):
        print es_primo
        x=x/es_primo
    else:
        print x
descomposicion()
