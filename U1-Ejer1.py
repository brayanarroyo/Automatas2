# Ejercicio 1: Realice un programa en Python que dado como dato el sueldo de un trabajador, 
# le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y del 12% en caso contrario. 
# Imprima el nuevo sueldo del trabajador.
def main():
    sueldo = float(input("Introduce sueldo: "))
    if(sueldo < 1000):
        sueldoF = sueldo*0.15 + sueldo
    else:
        sueldoF = sueldo*0.12 + sueldo
    
    print("Su sueldo final es de:",sueldoF )
    
if __name__ == "__main__":
    main()