# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Tome el ejercicio:
<condicionales_python / ejercicios_profundizacion / profundizacion_4>,
copielo a este ejercicio y modifíquelo para cumplir
el siguiente requerimiento

Realize un programa que corra indefinidamente en un bucle, al comienzo de la
iteración del bucle el programa consultará al usuario con el siguiente menú:
1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
3 - Salir del programa

En caso de presionar "3" el programa debe terminar e informar por
pantalla de que ha acabado,
en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
un mensaje de error y volver a comenzar el bucle
(vea en el apunte "Bucles - Sentencias" para encontrar
la sentencia que lo ayude a cumplir esa tarea)

Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
en donde en cada iteración se pedirá una palabra. La cantidad de iteración
(cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
condición esté dada por una variable (ej: palabras_deseadas = 4)
Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
Luego de tener las palabras deseadas almacenadas en una lista de palabras
se debe proceder a realizar las siguientes tareas:

Si se ingresa "1" por consola se debe obtener la palabra
más grande por orden alfabético
Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
se debe imprimir en pantalla cual era la palabra
más grande alfabeticamente.
Recuerde que debe inicializar primero su variable
donde irá almacenando la palabra que cumpla dicha condición.
¿Con qué valor debería ser inicializada dicha variable?

Si se ingresa "2" por consola se debe obtener la palabra
con mayor cantidad de letras
Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
se debe imprimir en pantalla cual era la palabra con
mayor cantidad de letras.
Recuerde que debe inicializar primero su variable
donde irá almacenando la palabra que cumpla dicha condición.
¿Con qué valor debería ser inicializada dicha variable?

NOTA: No se debe ordenar la lista de palabras, se debe obtener
el máximo utilizando el mismos métodos vistos durante la clase
(ejemplos_clase), tal como el ejercicio anterior. Ordenar una
lista representa un problema mucho más complejo que solo
buscar el máximo.

NOTA: Es recomendable que se organice con lápiz y papel para
hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
    que se deben ir guardando en una lista
3- Otro bucle interno que corre luego de que termine el bucle "2" que
    recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

while True:
    print ("operacion")
    operacion = int(input())

    if operacion > 3:
        print ("Ingrese un numero valido")
        continue

    if operacion == 3:
        print ("Finalizando Programa")
        break

    print ("palabra 1")
    palabra1 = str(input())



    print ("palabra 2")
    palabra2 = str(input())



    print ("palabra 3")
    palabra3 = str(input())





    palabras = [palabra1, palabra2, palabra3]

    palabra_mas_alta_alfabeticamente = None
    while operacion == 1:
        palabra_mas_alta_alfabeticamente = max(palabras)
        print (palabra_mas_alta_alfabeticamente)
        break    
    

    while operacion == 2:
        palabra_mas_larga = max(palabras), key=(len)
        print (palabra_mas_larga)

    '''
    while operacion == 2:
        lenpal1 = int(len(palabra1))
        lenpal2 = int(len(palabra2))
        lenpal3 = int(len(palabra3))
        
        if lenpal1 > lenpal2 and lenpal1 > lenpal3:
            print (palabra1)
        elif lenpal2 > lenpal1 and lenpal2 > lenpal3:
            print (palabra2)
        else:
            print (palabra3)
        
        break
    '''

    '''
    Tuve problemas con el while de la operacion 2 y ademas no sabia como usar el for y appendque nos dice como usar en la linea 42

    Me lo mencionaste en clase y ahora ya se como se hace, tengo screenshot.
    '''