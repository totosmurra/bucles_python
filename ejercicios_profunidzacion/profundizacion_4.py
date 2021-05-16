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
<condicionales_python / ejercicios_profundizacion /ejercicio_5.py>,
copielo a este ejercicio y modifíquelo para cumplir el
siguiente requerimiento

En este ejercicio se lo provee de una lista de temperatuas,
esa lista de temperatuas corresponde a los valores de temperaturas
tomados durante una temperorada del año en Buenos Aires.
Ustede deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperatuas

Los resultados se deberán almacenar en las siguientes variables
que ya hemos preparado para usted.

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase)
'''
temp_dataloger = [22, 21, 28, 25, 19, 23, 26] #Estas temperaturas las elegi yo aleatoriamente ya que 
print("Mi primer pasito en data analytics")   #no encontre el ejercicio "<condicionales_python / ejercicios_profundizacion /ejercicio_5.py>"
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......

#-------------------------------------------
#NO ME SALIO
#-------------------------------------------


# Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp
temperatura_max = max(temp_dataloger) 
temperatura_min = min(temp_dataloger)
temperatura_sumatoria = sum(temp_dataloger)
temperatura_len = len(temp_dataloger) 
temperatura_promedio =  temperatura_sumatoria / temperatura_len

print ("temperatura_max", temperatura_max)
print ("temperatura_min", temperatura_min)
print ("temperatura_sumatoria", temperatura_sumatoria)
print ("temperatura_len", temperatura_len)
print ("temperatura_promedio", temperatura_promedio)

# Al finalizar el bucle debe calcular el promedio como:
# temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo

if (temperatura_max == 28) and (temperatura_min == 19):
    print ("Verano")
elif (temperatura_max == 11) and (temperatura_min == 20):
    print ("Otoño")
elif (temperatura_max == 8) and (temperatura_min == 14):
    print ("Invierno")
elif (temperatura_max == 10) and (temperatura_min == 24):
    print ("Primvera")

