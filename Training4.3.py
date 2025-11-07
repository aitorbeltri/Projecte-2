def numeros(num):
    while True:
        try:
            return float(input(f"Escriu el nombre {num+1}/10: "))
        except ValueError:
            print("Entrada no vàlida. Torna-ho a intentar.")

def main():
    negatiu = False
    for i in range(10):
        n = numeros(i)
        if n < 0:
            negatiu = True
    if negatiu:
        print("hi havia almenys un nombre negatiu")
    else:
        print("no hi ha cap nombre negatiu")

if __name__ == "__main__":
    main()
