def esLetra(frase):
    res = False
    acentos = frase in "áéíóúüñÁÉÍÓÚÜÑ"
    i=0
    while i<len(frase):
        if ((frase[i]>='a'and frase[i]<='z') or (frase[i]>='A' and frase[i]<='Z') or acentos  ):
            res = True
    return res

def carAMinu(frase):
    i=0
    res=""
    while i<len(frase):
        if frase[i]>='A' and frase[i]<='Z':
            frase2=chr(ord (frase[i])+32)
            res=res+frase2
            i+=1
        else:
            letra=frase[i]
            res=res+letra
            i+=1
    return res

def recorrerStr(frase):
    i=0
    res=""
    frase1=carAMinu(frase)
    while i<len(frase1):
        if esLetra(frase1[i])==True:
            res=res+frase1[i]
            i+=1
        else:
            i+=1
    return res
    
def fraseReves(frase):
    i=len(frase)-1
    res=""
    frase1=carAMinu(frase)
    while i!=-1:
        if frase1[i]==" " or esLetra(frase1[i])==False:
            i=i-1
        else:
            rta=frase1[i]
            res=res+rta
            i=i-1
    return res

def esPalindrola(frase):
    frase1=fraseReves(frase)
    frase2=recorrerStr(frase)
    if frase1==frase2:
        rta=True
    else:
        rta=False
    return rta

def main():
    frase=input("Ingrese una frase: ")
    res=esPalindrola(frase)
    if res==True:
        rta="La frase es palindrola!"
    else:
        rta="La frase no es palindrola"
    print(rta)
    
main()
