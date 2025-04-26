# 1)
inicio = 1
fin = 100

for numero in range(inicio, fin + 1):
    if numero % 4 == 0:
        inicio = numero
        break


Lista = list(range(inicio,fin+1,4))

print(Lista)



#######################################################################
# 2)

Lista = ["apellido","nombre","edad","mail","direccion"]

cantidad = len(Lista)

print(Lista[cantidad-2])
print(Lista[-2])

#######################################################################
# 3)

Lista = []

nombre = input("Ingresa un nombre (Finaliza con 0): ")

while nombre != '0' :
    Lista.append(nombre)
    nombre = input("Ingresa un nombre: (Finaliza con 0): ")
print(Lista)


#######################################################################
# 4)

animales = ["perro", "gato", "conejo", "pez"]


animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#######################################################################
# 5)

# Este programa esta creando una lista con 5 numeros deshordenados. 
# Luego remueve el numero mas grande, 
# e imprime la lista nuevamente

#######################################################################
# 6)
lista = list(range(10,30+1,5))

print(lista[0:2])

#######################################################################
# 7)

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = 'corolla'
autos[2] = 'megane'

print(autos)

#######################################################################
# 8)

lista = []

for i in range(5,15+1,5) :
    lista.append(i*2)

print(lista)

#######################################################################
# 9)


compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

########################################################################
# 10)


lista_anidada = [15,True,[25.5,57.9,30.6],False]

print(lista_anidada[0])
print(lista_anidada[1])
print(lista_anidada[2][0])
print(lista_anidada[2][1])
print(lista_anidada[2][2])
print(lista_anidada[3])

#######################################################################