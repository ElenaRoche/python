def suma(num1,num2):
    resp=num1+num2
    return resp
def resta(num1,num2):
    resp=num1-num2
    return resp
def multiplicacion(num1,num2):
    resp=num1*num2
    return resp
def division(num1,num2):
    resp=num1/num2
    return resp

def menu_operacion():
    seguir="Si" #Si variable interruptora para salir del bucle
    num1=input("Dime un numero")
    num2=input("Dime un numero")
    while(seguir=="Si"):
        print "Que deseas hacer con los numeros"
        print "1.Sumarlos"
        print "2.Restarlos"
        print "3.Multiplicarlos"
        print "4.Dividirlos"
        respuesta=input()
        if (respuesta==1):
            print num1,"+",num2,"=",suma(num1,num2)
        if (respuesta==2):
            print num1,"-",num2,"=",resta(num1,num2)
        if (respuesta==3):
            print num1,"*",num2,"=",multiplicacion(num1,num2)
        if (respuesta==4):
            print num1,"/",num2,"=",division(num1,num2)
        seguir=raw_input("quieres seguir")

menu_operacion()
