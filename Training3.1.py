try:
    edat = int(input("Perfavor, introdueix la teva edad: "))
    if edat < 18:
        print("Ets menor d'edat.")
    else:
        print("Ets major d'edat.")

except ValueError:
    print("Perfavor, introdueix un valor numeric válid para a l'edat.")