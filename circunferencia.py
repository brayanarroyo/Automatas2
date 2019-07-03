#Nombre: circunferencia.py
#Objetivo: calcula el área y diametro de una circunferencia e import math
#Autor: Arroyo Chávez Brayan Alberto
#Fecha: 01/07/2019

import math as mat

#----------------------------------------
#Función para calcular area
#----------------------------------------
def calcularArea(r):
    area = mat.pi*(mat.pow(r,2))
    return area

#----------------------------------------
#Función para calcular area
#----------------------------------------
def caclulaDiametro(r):
    diam= r*2
    return diam


def main():
    ciclo = True
    while(ciclo): 
        print("-- Script para calculuar area de una circunferencia --")
        radio = float(input("Introduce el valor del radio:"))
        #invocar un método
        print("El área es: ",calcularArea(radio))
        print("El diametro es: ",caclulaDiametro(radio))

        resp = input("Desea hacer otro calculo(s/n)?")
        if (resp == "S" or resp == "s"):
            ciclo = True
        else:
            ciclo = False



if __name__ == "__main__":
    main()