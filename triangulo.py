#Nombre: triangulos.py
#Objetivo: determinar tipo de triangulo con su perimetro
#Autor: Arroyo Chávez Brayan Alberto
#Fecha: 01/07/2019

def determinarTipo(l1,l2,l3):
    if (l1 == l2 and l1 ==l3):
        return "Triangulo equilatero"
    elif  ((l1 == l2 and l3!= l1) or (l1 == l3 and l1 !=l2) or (l2 == l3 and l2!=l1)):
        return "Triangulo isósceles"
    elif (l1!=l2 and l1!=l3 and l2!=l3):
        return "Triangulo escaleno"
        

def main():
    lado1 = float(input("Ingrese el primer lado"))
    lado2 = float(input("Ingrese el segundo lado"))
    lado3 = float(input("Ingrese el tercer lado"))
    print("El tipo de traingulo ingresado es:", determinarTipo(lado1,lado2,lado3))

    perimetro = lado1+lado2+lado3

    print("Perimetro: ", perimetro)

if __name__ == "__main__":
    main()