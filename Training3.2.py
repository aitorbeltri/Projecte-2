numero1 = input("Introdueix el primer numero: ")
numero2 = input("Introdueix el segon numero: ")
numero3 = input("Introdueix el tercer numero: ")
if int(numero1) >= int(numero2) and int(numero1) >= int(numero3):
    print("El primer numero és el més gran:", numero1)
elif int(numero2) >= int(numero1) and int(numero2) >= int(numero3):
    print("El segon numero és el més gran:", numero2)
else:
    print("El tercer numero és el més gran:", numero3)
