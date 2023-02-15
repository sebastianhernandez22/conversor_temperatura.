# Programa para convertir una catidad dada de grados centigrados a s equivalente en Farenheit y kelvin

print("--------------------------------------")
print("------Valor de grados centigrados-----")
print("--------------------------------------")

# input
c = int(input("digite el valor de c:"))

# processing
F = ( c * 1.8 + 32 )
K = ( c + 273,15)

#output
print("--------------------------------------")
print("-------------RESULTADOS---------------")
print("--------------------------------------")
print("la conversion de farenheit es" + str(F))
print("la conversion de Kelvin es" + str(K))
