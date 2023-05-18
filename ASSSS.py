def esLetra(frase):
    res = False
    acentos = frase in "áéíóúüñÁÉÍÓÚÜÑ"
    i=0
    while i<len(frase):
        if ((frase[i]>='a'and frase[i]<='z') or (frase[i]>='A' and frase[i]<='Z') or acentos  ):
            res = True
            i+=1
    return res

def verPal(frase):
    res = ""
    i=0                                                
    largoFrase = len(frase)                           
    while i<largoFrase :
        
        while i<largoFrase and not esLetra(frase[i]): 
            i+=1                                      
           
        pal=""       
        while i<largoFrase and esLetra(frase[i]):     
            pal = pal + frase[i]                      
            i+=1
           
        if pal!="": 
            #print(pal)
            res = res + pal + "\n"         
           
    return res

print(verPal("hola como estas "))