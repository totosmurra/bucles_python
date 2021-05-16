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
Tome el ejercicio de "calificaciones":
<condicionales_python / ejercicios_practica / profundizacion_3.py>,
copielo a este ejercicio y modifíquelo para cumplir
el siguiente requerimiento

Las notas del estudinte se encuentran almacenadas en una
lista llamada "notas" que ya hemos definido al comienzo del archivo

Debe caluclar el promedio de todas las notas y luego transformar
la califiación en una letra según la escala establecida en el ejercicio
"calificaciones" <condicionales_python / ejercicios_practica / ejercicio_3.py>

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio
notas = [1, 5, -1, 6, 10, 2, -5]

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

for i in notas:
    if i >= 0:
        cantidad_notas +=1
    else:
        cantidad_ausentes += 1
    
print ("cantidad de notas", cantidad_notas)
print ("cantidad de asusentes", cantidad_ausentes)
# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria
for i in notas:
    sumatoria += i
print ("la sumatoria es", sumatoria)
# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas
promed = sumatoria / cantidad_notas
print ("el promedio es", promed)

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

print ("la nota promedio es una")

if promed >= 9:
    print ("A")
elif 9>promed>=8:
    print ("B")
elif 8>promed>=7:
    print ("C")
elif 7>promed>=6:
    print ("D")
elif promed<6:
    print ("F")

# Imprima en pantalla al cantidad de ausentes
