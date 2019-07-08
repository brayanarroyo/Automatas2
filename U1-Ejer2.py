# Ejercicio  2: Realice un programa en Python que dado como datos la categoría y el sueldo 
# de un trabajor, calcule el aumento correspondiente teniendo en cuenta la siguiente 
# información e imprima el nuevo sueldo del trabajador:

# Categoría 1 : Aumento 15%
# Categoría 2 : Aumento 10%
# Categoría 3 : Aumento 8%
# Categoría 4 : Aumento 7%
def main():
    cate = int(input("Ingrese la categoria: "))
    sueldo = float(input("Ingrese el sueldo: "))
    
    if(cate == 1):
        sueldoF=sueldo*.15+sueldo
    elif(cate == 2):
        sueldoF=sueldo*.10+sueldo
    elif(cate == 3):
        sueldoF=sueldo*.08+sueldo
    elif(cate == 4):
        sueldoF=sueldo*.07+sueldo
    else:
        print("Ingrese una categoria entre 1 y 4")
    
    print("Su sueldo final es de:",sueldoF )
if __name__ == "__main__":
    main()