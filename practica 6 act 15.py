def agregar(di,a,b):
    di[a]=b

def agregarDicEle2():
    di={}
    clave=""
    while clave!=".":
        clave=input("Ingrese numero de documento (o un punto(.) para terminar): ")
        valor=cargarValor()
        agregar(di,clave,valor)
    di.pop(".")
    return di

def cargarValor():                    #<>
    lista=[]
    nombre=[]
    notas=[]
    n=""
    nom=input("Ingrese nombre (o un punto(.) para terminar) : ")
    nombre.append(nom)
    ape=input("Ingrese apellido (o un punto(.) para terminar): ")
    nombre.append(ape)
    lista.append(nombre)
    while n!=0:
        n=int(input("Ingrese notas del alumno, o cero (0) para terminar: "))
        notas.append(n)
    notas.pop(-1)
    lista.append(notas)
    
    return lista

def main():
    print(agregarDicEle2())
    
main()
