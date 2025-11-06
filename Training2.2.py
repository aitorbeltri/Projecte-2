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