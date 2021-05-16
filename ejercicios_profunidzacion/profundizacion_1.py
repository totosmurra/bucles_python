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
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

# inicio = ....
inicio = int(input('Ingrese el primero número de la secuencia\n'))



# fin = ....
fin = int(input('Ingrese el ultimo número de la secuencia\n'))
fin += 1



# cantidad_numeros ....
numeros = [inicio, fin]
cantdenum = 0
for i in numeros:
    cantdenum += 1
print ("la cantidad de numeros es", cantdenum)



# sumatoria ....
sumatoria = 0

for i in range(inicio, fin):
    sumatoria += i

print ("la sumatoria es", sumatoria)
# bucle.....

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros

promedio = sumatoria / cantdenum

print ("el promedio es", promedio)

# Imprimir resultado en pantalla