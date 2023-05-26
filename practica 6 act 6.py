def cargarLista():                    #<>
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        lista.append(int(num))
    lista.pop(-1)
    return lista

def mayor(lst):
    i=0
    mayor=lst[i]
    while i<len(lst):
        if lst[i]>mayor:
            mayor=lst[i]
        i+=1
    return mayor

def ordenarLst(lst):
    i=0
    x=0
    y=0
    mayor=mayor(lst)
    while i<len(lst):
        while lst[i]<=mayor:
            
            


            
        
def main():
    lst=cargarLista()
    ordenarLst(lst)
    print(lst)
    
main()
    