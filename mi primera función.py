"""funciones"""

def miprimerafuncion():
    print("hola mundo!")
    
miprimerafuncion()

"""abajo de estas despues SI O SI tengo que hacer tengo que hacer una funcion que va a llamarse main() con el programa ppal"""
def main():
    nombre=(input("Hola! cual es tu nombre? "))
    print("Buenos días", nombre,"!")
main()


# FUNCIONES CON PARÁMETRO

def fun1(parametro1, parametro2):
    #aca se explica lo que va a hacer esta función, en este caso, suma de numeros
    sumatoria = parametro1 + parametro2
    return sumatoria

def funPpal():
    a = int(input("ingrese un num: "))
    b = int(input("ingrese otro num: "))
    rta = fun1(a,b)
    print(rta)
    

funPpal()

"""las funciones que vamos a utilizar son in (parametro de entrada de una función)
ej in: datos str, int, float, bool
Tambien existen los parametros out(de salida) e inout (entrada y salida)
ej: list e disc (out e inout)
out: el retorno de una función"""


"""return en una función
al hacer esto, la f retorna un valor.se implementa de esta manera
return y lo que se quiere retornar (sin igual ni parentesis nada)
se recomienda usar un solo return por función, de lo contrario, una vez que se ejecuta el return, la función termina automaticamente su ejecución
y retorna el control a quien la  haya llamado

Para capturar el valor de retorno de una función llamada, se necesitará hacer una asignación. A
la derecha del igual =, estará la función llamada (que retorna valor) y a la izquierda del igual = ,
estará la variable donde se almacenará el valor que retorna la función.

Una función retornará el valor (palabra reservada) None si la función no está preparada para
retornar valores. Esto puede ocurrir si:
● La función no contiene en su código la palabra reservada return,
● La función si contiene en su código la palabra reservada return, pero a su derecha no hay
ningún valor a retornar.

● Ejemplo: La función print no está preparada para retornar , por tanto su valor de retorno será
None"""

def sumar(num1,num2):
    suma=num1 + num2
    return suma

def ingresarInt(msj):
    print(msj, end="")
    ent=int(input())
    return ent

def main1():
    a= ingresarInt("Ingresar numero a: ")
    b= ingresarInt("Ingresar numero b: ")
    
    misuma= sumar(a,b)
    print("La suma es ", misuma)
    
#para ver ejecutada ir a return

"""import"""
#se utiliza para poder importar una biblioteca (archivo que contiene un conjunto de funciones. se llama de la sig manera:
#import nombreBiblioteca
import random

def aleatorio(inf,sup):
    numAle=random.randiant (inf,sup)
    return numAle

def main3():
    print(aleatorio(10,30))
    print(aleatorio(10,30))
    
#para ver ejecutada ir a import
    

"""from e import"""
#se puede importar solo una función específica de la biblioteca de la siguiente manera
#from nombreBiblioteca import nombreFuncion

