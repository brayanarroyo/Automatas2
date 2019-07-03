#Nombre: factorial.py
#Objetivo: calcula el factorial
#Autor: Arroyo Brayan 
#Fecha: 01/07/2019

def factorial(n):
    resul = 1
    for i in range(1,n+1):
        resul = resul * i
    return resul

def main():
    num = int(input("Ingrese un numero"))
    print("El factoria de ",num," es: ",factorial(num))

if __name__ == "__main__":
    main()