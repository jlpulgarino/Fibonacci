# Entrada numero entero
numero = int(raw_input("Escriba su numero por favor "))
if numero > 1:
    secuencia = set()
    numAnerior = 0
    numActual = 1
    #Itera hasta que se alcance el valor digitado
    while (numActual + numAnerior) < numero:
        suma = numActual + numAnerior
        numAnerior = numActual
        numActual = suma
        secuencia.add(numActual)
    print secuencia