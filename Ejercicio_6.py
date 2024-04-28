
# CODE:14
# IMPORTANTE: NO borrar los comentarios

cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3
numero_1 = int(input('Ingrese el primero numero:'))
numero_2 = int(input('Ingrese el segundo numero:'))
numero_3 = int(input('Ingrese el tercer numero:'))

# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.
if numero_1 > 0:
    cantidad_numeros_positivos +=1
if numero_2 > 0:
    cantidad_numeros_positivos +=1
if numero_3 > 0:
    cantidad_numeros_positivos +=1
# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"


# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos
print(f'{cantidad_numeros_positivos}')
