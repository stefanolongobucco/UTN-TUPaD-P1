



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