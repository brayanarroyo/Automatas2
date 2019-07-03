#Nombre: fibonacci.py
#Objetivo: calcula la serie de fibonacci
#Autor: Arroyo Chávez Brayan Alberto
#Fecha: 01/07/2019

def fibonacci(n,f1,f2,b):
    if(b==1):
        print("1")
    if (n!=1):
        fn=f1 + f2
        f1=f2
        print(fn)
        fibonacci(n-1,f1,fn,0)


def main():
    num = int(input("Ingrese un numero"))
    fibonacci(num,0,1,1)

if __name__ == "__main__":
    main()