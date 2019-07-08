# Ejercicio 3: Realice un programa en Python que dado como datos los sueldos de 10 trabajadores 
# de una empresa, obtenga el total de nómina de la misma. Puede utilizar un ciclo for o un ciclo while.
def main():
    nomina = 0
    for i in range(1,11):
        sueldo = float(input("Ingrese el sueldo del trabajador: "))
        nomina= nomina + sueldo
    print("La nomina de la empresa es:",nomina)

if __name__ == "__main__":
    main()