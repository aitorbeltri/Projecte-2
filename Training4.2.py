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