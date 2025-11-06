try:
    num1 = float(input("Introdueix un nombre: "))
    if num1 < 0:
        print("El nombre és negatiu.")
    elif num1 >= 0:
        print("El nombre és positiu o zero.")

except ValueError:
    print("Si us plau, introdueix un valor numèric vàlid.")
