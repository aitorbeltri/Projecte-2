def hola_mon ():
    print("Hola Món!")

def calcular_area_quadrat ():
    def costat():
        try:
            costat = float(input("Introdueix el valor del costat del quadrat: "))
        except ValueError:
            print("Entrada no vàlida. Introdueix un nombre.")
            return

        if costat < 0:
            print("La mida no pot ser negativa.")
            return

        area = costat * costat
        print(f"L'àrea del quadrat és: {area}")

    if __name__ == "__main__":
        costat()

def calculadora_basica ():
    def numeros():
        num1 = int(input("Ingrese un número entero: "))
        num2 = int(input("Ingrese otro número entero: "))

        suma = num1 + num2
        resta = num1 - num2
        divisio = num1 / num2
        multiplicacio = num1 * num2

        print(f"La suma de es: {suma}")
        print(f"La resta de es: {resta}")
        print(f"La divisió de es: {divisio}")
        print(f"La multiplicació de es: {multiplicacio}")

    if __name__ == "__main__":
        numeros()

def crear_frase ():
    def paraula():
        p1 = input(f"Ingrese una paraula: ")
        p2 = input(f"Ingrese otra paraula: ")
        p3 = input(f"Ingrese otra paraula: ")

        print(f"La frase creada és: {p1} {p2} {p3}")

    if __name__ == "__main__":
        paraula()

def convertir_enter ():
    try:
        numero1 = float(input("Introdueix el primer numero decimal amb coma flotant: "))
        numero2 = float(input("Introdueix el segon numero decimal amb coma flotant: "))
        numero1_enter = int(numero1)
        numero2_enter = int(numero2)
        print("El primer nombre amb forma d'enter és:", numero1_enter)
        print("El segon nombre amb forma d'enter és:", numero2_enter)

    except ValueError:
        print("Si us plau, introdueix valors numèrics vàlids en coma flotant.")

def major_o_menor_edat ():
    try:
        edat = int(input("Perfavor, introdueix la teva edad: "))
        if edat < 18:
            print("Ets menor d'edat.")
        else:
            print("Ets major d'edat.")

    except ValueError:
        print("Perfavor, introdueix un valor numeric válid para a l'edat.")

def numero_mes_gran ():
    numero1 = input("Introdueix el primer numero: ")
    numero2 = input("Introdueix el segon numero: ")
    numero3 = input("Introdueix el tercer numero: ")
    if int(numero1) >= int(numero2) and int(numero1) >= int(numero3):
        print("El primer numero és el més gran:", numero1)
    elif int(numero2) >= int(numero1) and int(numero2) >= int(numero3):
        print("El segon numero és el més gran:", numero2)
    else:
        print("El tercer numero és el més gran:", numero3)

def positiu_o_negatiu ():
    try:
        num1 = float(input("Introdueix un nombre: "))
        if num1 < 0:
            print("El nombre és negatiu.")
        elif num1 >= 0:
            print("El nombre és positiu o zero.")

    except ValueError:
        print("Si us plau, introdueix un valor numèric vàlid.")

def imprimir_parells ():
    x = 0
    while x < 201:
        print(x)
        x += 2

def comprovar_deu ():
    te_deu = False
    while True:
        try:
            nota = int(input("Introdueix una nota (-1 per acabar): "))
            if nota == -1:
                break
            if nota < -1 or nota > 10:
                    print("La nota ha d'estar entre 0 i 10.")
                    continue
            if nota == 10:
                te_deu = True
        except ValueError:
            print("Introdueix un número vàlid.")

    if te_deu:
        print("Hi ha hagut alguna nota que té un 10.")
    else:
        print("No hi ha cap 10.")

def comprovar_negatius ():
    n_negatiu = False
    nombre = 0
    num_vegades = 0
    while num_vegades < 10:
        try:
            nombre = int(input("Introdueix un nombre: "))
            if nombre < 0:
                n_negatiu = True
            num_vegades += 1
        except ValueError:
            print("Introdueix un número vàlid.")
    if n_negatiu:
        print("S'ha introduït un nombre negatiu.")
    else:
        print("No hi ha cap negatiu.")

import time

while (True):
    print("Tria una opció:")
    print("1. Hola Món")
    print("2. Calcular àrea del quadrat")
    print("3. Calculadora bàsica")
    print("4. Crear frase")
    print("5. Convertir a enter")
    print("6. Major o menor d'edat")
    print("7. Número més gran")
    print("8. Positiu o negatiu")
    print("9. Imprimir nombres parells fins a 200")
    print("10. Comprovar si hi ha un 10 entre les notes")
    print("11. Comprovar si s'ha introduït un nombre negatiu")
    print("S. Sortir")

    x = input("Introdueix el número de l'opció desitjada: ")

    match x:
        case "1":
            hola_mon()
        case "2":
            calcular_area_quadrat()
        case "3":
            calculadora_basica()
        case "4":
            crear_frase()
        case "5":
            convertir_enter()
        case "6":
            major_o_menor_edat()
        case "7":
            numero_mes_gran()
        case "8":
            positiu_o_negatiu()
        case "9":
            imprimir_parells()
        case "10":
            comprovar_deu()
        case "11":
            comprovar_negatius()
        case "S":
            print("Apagant el programa.")
            break
        case _:
            print("Fica una opció disponible.")
    time.sleep(5)