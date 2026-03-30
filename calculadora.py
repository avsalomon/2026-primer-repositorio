print ("calculadora")

while True:

    eleccion = int(input("Que accion queres hacer en la calculadora:\n1: Suma\n2: Resta\n3: Multiplicación\n4: División\n5: Salir\n>>> "))

    if eleccion == 1:
        suma = float(input("Ingresa el primer numero de la suma\n>> "))
        suma1 = float(input("Ingresa el segundo numero de la suma\n>> "))
        r = (suma+suma1)
        print (f"El resultado es: {r}")
    elif eleccion == 2:
        resta = float(input("Ingresa el primer numero de la resta\n>> "))
        resta1 = float(input("Ingresa el segundo numero de la resta\n>> "))
        r2 = (resta-resta1)
        print (f"El resultado es: {r2}")
    elif eleccion == 3:
        multiplicacion = float(input("Ingresa el primer numero de la multiplicacion\n>> "))
        multiplicacion1 = float(input("Ingresa el segundo numero de la multiplicacion\n>> "))
        r3 = (multiplicacion*multiplicacion1)
        print (f"El resultado es: {r3}")
    elif eleccion == 4:
        division = float(input("Ingresa el primer numero de la division\n>> "))
        division1 = float(input("Ingresa el segundo numero de la division\n>> "))
        r4 = (division/division1)
        if division == 0 or division1 == 0:
            print ("No se puede dividir por cero")
        else:
            print (f"El resultado es: {r4}")
    elif eleccion == 5:
        print ("Saliste de la calculadora")
    else: 
        print("Esa opción no esta disponible")
