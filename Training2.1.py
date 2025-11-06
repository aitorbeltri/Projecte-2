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