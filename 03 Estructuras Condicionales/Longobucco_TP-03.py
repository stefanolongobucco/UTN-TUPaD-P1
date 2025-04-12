

Edad = int(input("Ingrese su Edad: "))


if Edad >= 18:
    print("Es mayor de edad")
else  :
    print("Es menor de edad")




########################################################################################    



Nota = int(input("Ingrese su Nota: "))


if Nota >= 6:
    print("Aprobado")
else  :
    print("desaprobado")




########################################################################################    




num = int(input("Ingrese un numero: "))


if  num % 2  == 0:
    print("Ha ingresado un número par")
else  :
    print("Por favor, ingrese un número par")



########################################################################################    


edad = int(input("Ingrese su edad: "))


if  edad  < 12:
    print("Niño/a")
elif  edad >= 12 and edad < 18:
     print("Adolecente")
elif edad >= 18 and edad < 30:
      print("Adulto/a joven")
else :
      print("Adulto/a")


########################################################################################    


id = len(input("Ingrese su contraseña: "))


if  id  >= 8 and id <= 14:
    print("Ha ingresado una contraseña correcta")
else : 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



########################################################################################    


from statistics import mode, median, mean
import random



numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = int(mean(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
moda = int(mode(numeros_aleatorios))


if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else :
    print("No cumple ninguna de las condiciones")




########################################################################################    


texto = input("Ingresá una frase o palabra: ")  


if texto[-1].lower() in "aeiou":
    texto += "!"


print(texto)





########################################################################################    


nombre = input("Ingresá tu nombre: ")  

opcion = int(input("\nIngresar la opcion que desea: (ingrese en numero) " 
"\nOpcion 1 - Si quiere su nombre en mayúsculas" \
"\nOpcion 2 - Si quiere su nombre en minúsculas" \
"\nOpcion 3 - Si quiere su nombre con la primera letra mayúscula \n\n"))

print("\n")

if opcion == 1 :
    print(nombre.upper() )
elif opcion == 2 :
    print(nombre.lower() )
elif opcion == 3 :   
    print(nombre.title() )
else :
    print("\nOpcion invalida") 

print("\n")




########################################################################################    


magnitud = int(input("Ingresá la magnitud del terremoto: ")  )



if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


    ########################################################################################    


hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿En qué mes estás? (1-12): "))
dia = int(input("¿Qué día del mes es hoy?: "))


fecha = mes * 100 + dia


if hemisferio == "N":
    if 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif hemisferio == "S":
    if 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = "Hemisferio inválido"


print("Estación del año: " + estacion)