def cargarLista():                    #<>
    lista=[]
    num=""
    while num!=0:
        num=float(input("Ingrese numeros, o 0 (cero) para terminar:"))
        lista.append(int(num))
    lista.pop(-1)
    return lista

def ordenarLst(lst):
    i=0
    x=0
    y=0
    while i<len(lst):
        if lst[i]>=lst[x]:
            lst[y]=y
            i+=1
            y+=1
            x=0
        else:
            x+=1
            
        
def main():
    lst=cargarLista()
    ordenarLst(lst)
    print(lst)
    
main()