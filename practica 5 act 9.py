def esLetra(c):
    if (c>="a" and c<="z") or (c>="A" and c<="Z"):
        res=True
    else:
        res=False
    return res

def verPal(frase):
    i=0                                                
    numPals=0
    while i<len(frase):
        while i<len(frase) and not esLetra(frase[i]):
            i+=1                                     
           
        pal=""       
        while i<len(frase) and esLetra(frase[i]):     
            pal = pal + frase[i]                      
            i+=1 
        if pal!="":
            numPals+=1     
    return numPals

def mayor(frase):
    mayor=""
    i=0
    while i<len(frase):
        while i<len(frase) and not esLetra(frase[i]):
            i+=1
            
        pal=""       
        while i<len(frase) and esLetra(frase[i]):     
            pal = pal + frase[i]                      
            i+=1
        
        if len(pal)>=len(mayor):
            mayor=pal
            
    return mayor

def menor(frase):
    i=0
    while i<len(frase):
        while i<len(frase) and not esLetra(frase[i]):
            i+=1
            
        pal=""       
        while i<len(frase) and esLetra(frase[i]):     
            pal = pal + frase[i]                      
            i+=1

            menor=pal
            if len(pal)<=len(menor) and menor!="":
                menor=pal
            
    return menor

def main():
    texto=input("Ingrese un texto: ")
    numPals=verPal(texto)
    may=mayor(texto)
    men=menor(texto)
    rta="El texto tiene {} palabras. La de mayor longitud es {} y la de menor longitud es {}".format(numPals,may,men)
    print(rta)
    
main()


        
        
    