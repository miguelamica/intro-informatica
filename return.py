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

# EJEMPLO DE RETURN CON FUNCIÓN CON PARÁMETRO

def sumar(num1,num2):
    suma=num1 + num2
    return suma

def ingresarInt(msj):
    print(msj, end="")
    ent=int(input())
    return ent

def main():
    a= ingresarInt("Ingresar numero a: ")
    b= ingresarInt("Ingresar numero b: ")
    
    misuma= sumar(a,b)
    print("La suma es ", misuma)
    
main()