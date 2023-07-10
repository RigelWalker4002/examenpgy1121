from os import system

ocupados = []
dinerototal = 0


def mostrarlugares():
    system("cls")
    print("Lugares disponibles:\n")
    print("-----------------[ESCENARIO]-----------------")
    for i in range(1,101):
        silla = i
        for puesto in ocupados:
            if i in puesto:
                silla = "X"
        if i%10 == 0:
            print(silla,"\n")
        else:
            print(silla, end=" ")

def pausa():
    input("Presione enter para continuar...")



def comprarentradas():
    system("cls")
    entradas = ""
    while True:
        entradas = input("Cuántas entradas desea comprar?, el máximo de entradas son 3: ")
        if entradas.isnumeric():
            if int(entradas) < 1 and entradas > 3:
                print("Sólo se pueden comprar entre 1 y 3 entradas")
            else:
                break
    entradas = int(entradas)
    totalentradas = 0
    for i in range(entradas):
        mostrarlugares()
        print("""Seleccione el asiento que desea:

•Platinum (range(1,101) del 1 al 20): $120.000
•Gold (range(1,101) del 21 al 50): $80.000
•Silver (range(1,101) del 51 al 100): $50.000
""")
    
        while True:
            asiento = input(f"Ingrese el asiento N°{i+1}: ")
            if asiento.isnumeric:
                asiento = int(asiento)
                if asiento in range(1,101):
                    break
        ocupante = ""
        while not ocupante.isnumeric():
            ocupante = input("Ingrese el RUN del ocupante de este asiento sin puntos ni dv: ")
        ocupante = int(ocupante)
        ocupados.append([asiento, ocupante])

        if asiento >= 1 and asiento <= 20:
            totalentradas += 120000
        elif asiento >= 21 and asiento <= 50:
            totalentradas += 80000
        elif asiento >= 51 and asiento <= 100:
            totalentradas += 50000
        else:
            print("Error en la operación...")
            return 0
        print()

    print("Operación exitosa")
    print(f"Total: ${totalentradas}")
    return totalentradas

def mostrarasistentes():
    asistentes = []
    if len(ocupados) > 0:
        for i in ocupados:
            asistentes.append(i[1])
        print(asistentes)

        ordenado = False
        while ordenado == False:
            ordenado = True
            for i in range(len(asistentes)):
                if len(asistentes) > i+1:
                    if asistentes[i]>asistentes[i+1]:
                        ordenado = False
                        asistentes[i],asistentes[i+1] = asistentes[i+1],asistentes[i]
        print("Lisa de asistentes:")
        for i in asistentes:
            print(f"•{i}")

def gananciastotales():
    system("cls")
    print(f"Ganancias totales: ${dinerototal}")

while True:
    system("cls")
    print("""1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir""")

    op = input("Ingrese una opción: ")

    match op:
        case "1":
            dinero = comprarentradas()
            dinerototal += dinero
        case "2":
            mostrarlugares()
        case "3":
            mostrarasistentes()
        case "4":
            gananciastotales()
        case "5":
            system("cls")
            print("Saliendo del programa")
            break
        case other:
            system("cls")
            print("Opción no disponible")

    pausa()
