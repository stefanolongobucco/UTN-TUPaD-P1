for i in range(0,101) :
    print(i)


#########################################################################################



numero = (input("ingresa un numero: "))

tamaño = len(numero)

print(f"El numero {numero} tiene {tamaño} digitos")




#########################################################################################


band = 0
suma = 0

while band == 0 :

    num1 = int(input("Ingresa el primer valor: "))
    num2 = int(input("Ingresa el segundo valor: "))

    if num2 != num1 :
        if (num1 > num2) :
            aux = num1
            num1 = num2
            num2 = aux
        band = 1

        for i in range (num1 + 1 ,num2) :
            suma  += i 
        print(f"La suma de los numero comprendidos es: {suma}")
    else :
        print("Los numero no puden ser iguales")
        



#########################################################################################


band = 0
suma = 0

while band == 0 :

    num1 = int(input("Ingrese un numero entero: "))
    suma += num1
    if num1 == 0 :
        band = 1


print(f"La suma de los numeros ingresados es: {suma}")

#########################################################################################

import random

numero_a_adivinar = random.randint(0, 9)
numero_elegido = 99999999
cont = 0



while numero_a_adivinar != numero_elegido :
    numero_elegido = int(input("ingrese un numero entero entre el 0 y el 9: "))
    
    if numero_elegido >= 0 and numero_elegido <= 9 :
      cont += 1
    else :
        print("El numero tiene que estar entre 0 y 9")


print(f"Felicidades el numero era el {numero_a_adivinar} tuvo {cont} intentos. ")





#########################################################################################




for i in range(100,-1,-2):
    print(i)




#########################################################################################




suma = 0
band = 0

while band == 0 :

    hasta = int(input("Ingrese un numero: "))
   
    if hasta > 0 :
        for i in range(0, hasta + 1):
            suma += i
        band = 1
    else :
        print("El numero debe ser mayor a 0")

print(f"La suma se los numeros comprendidos entre 0 y {hasta} es: {suma}")

#########################################################################################


desde = 0 
hasta = 100 
par = 0
imp = 0
pos = 0
neg = 0



for i in range(desde, hasta) :
    numero = int(input("ingrese un numero entero: "))

    if numero % 2 == 0 :
        par += 1
    else :
        imp += 1

    if numero >= 0 :
        pos += 1
    else :
        neg += 1



print(f"\n Pares = {par} \n Impares = {imp} \n Positivos = {pos} \n Negativos = {neg}")

#########################################################################################

desde = 0 
hasta = 100 
suma = 0



for i in range(desde, hasta) :
    numero = int(input("ingrese un numero entero: "))

    suma += numero

prom = suma / hasta



print(f"\nEl promedio es de = {prom}")

#########################################################################################


numero = (input("Ingrese un numero: "))
numero_invertido = ''

for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

print(f"Numero invertido: {numero_invertido}")
