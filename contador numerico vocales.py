def contador_numerico_vocales():
    palabra=raw_input("Dime una palabra")
    p=0
    q=0
    r=0
    s=0
    t=0
    
    for cont in range (0,len(palabra),1):
        if palabra[cont]=='A'or palabra[cont]=='a':
            p=p+1
        if palabra[cont]=='E'or palabra[cont]=='e':
            q=q+1
        if palabra[cont]=='I'or palabra[cont]=='i':
            r=r+1
        if palabra[cont]=='O'or palabra[cont]=='o':
            s=s+1
        if palabra[cont]=='U'or palabra[cont]=='u':
            t=t+1
    print"En la palabra", palabra,"hay",p,'aes',q,'es',r,'is',s,'os',t,'ues'
contador_numerico_vocales()
        
