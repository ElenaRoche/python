def pizza():
    x=input("dime el diametro de la pizza")
    radio=x/2
    pi=3.1416
    area=(radio*radio)*pi
    precio=input("dime cuanto vale la pizza")
    centrimetro=precio/area
    print centrimetro

pizza()
