def calificaciones():
    asig=input("introduzca el nombre de la asignatura:")
    print("introduce los cuatro calificaciones")
    while True:
        c1 = int(input("introduce el primer calificacion:"))
        if c1 <= 70:
            print("advertencia")
        elif c1>=70:
            print("aprobado")
        condicion = input("¿desea continuar? (S=si N=no):")
        c2 = int(input("introduce la segunda calificacion:"))
        if c2<=70:
            print("advertencia")
        elif c2>=70:
            print("aprobado")

        condicion = input("¿desea continuar? (S=si N=no):")
        c3 = int(input("introduce la tercera calificacion:"))
        if c3 <= 70:
            print("advertencia")
        elif c3>=70:
            print("aprobado")
        condicion = input("¿desea continuar? (S=si N=no):")
        c4 = int(input("introduce la cuarta calificacion:"))
        if c4 <= 70:
            print("advertencia")
        elif c4>=70:
            print("aprobado")
        prom = (c1 + c2 + c3 + c4) / 4
        if 70 <= prom <= 100:
            mensaje = "aprobado"

        elif prom <=70:
                mensaje="reprobado"

        print(f"nombre de la asignatura:{asig}, su promedio es={prom}, {mensaje}")
        condicion = input("¿desea continuar capturando las calificaciones de otro alumno? (S=si N=no):")
        if condicion == "n" or condicion == "N":
            break
calificaciones()