"""SUMA DE LOS PRIMEROS N NÚMEROS"""

N = int(input("Digite el valor de los N números que desea sumar: "))

i = 1
suma = 0

while i <= N:
    suma = suma + i
    i = i + 1

print("Lsuma de los " + str(N) + "primeros números es " + str(suma))