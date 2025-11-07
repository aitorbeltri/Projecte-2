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