def cambiadordevocales():
    texto=raw_input("Dime un texto")
    for cont in range(0,len(texto),1):
        if texto[cont]=='A':
            print "U"
        elif texto[cont]=='a':
            print "u"
        elif texto[cont]=='E':
            print "U"
        elif texto[cont]=='e':
            print "u"
        elif texto[cont]=='I':
            print "U"
        elif texto[cont]=='i':
            print "u"
        elif texto[cont]=='O':
            print "U"
        elif texto[cont]=='o':
            print "u"
        else:
            print texto[cont]
cambiadordevocales()
