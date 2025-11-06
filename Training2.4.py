try:
    numero1 = float(input("Introdueix el primer numero decimal amb coma flotant: "))
    numero2 = float(input("Introdueix el segon numero decimal amb coma flotant: "))
    numero1_enter = int(numero1)
    numero2_enter = int(numero2)
    print("El primer nombre amb forma d'enter és:", numero1_enter)
    print("El segon nombre amb forma d'enter és:", numero2_enter)

except ValueError:
    print("Si us plau, introdueix valors numèrics vàlids en coma flotant.")