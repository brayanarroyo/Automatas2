# Ejercicio 4: Realice un programa en Python que permita capturar en una lista las calificaciones 
# de N alumnos y que le permita calcular e imprimir lo siguiente:

# El promedio general de los alumnos
# Numero de alumnos aprobados y número de alumnos reprobados (Si el alumno sacó una calificación menor a 70 se considera reprobado)
# Porcentaje de alumnos aprobados y reprobados.
# Número de alumnos cueya calificación fue mayor a 80lista = []
lista = []
def agregar():
    ciclo = True
    while(ciclo):
        cal = float(input("Ingrese la calificación del alumno"))
        lista.append(cal)
        resp = input("Desea capturar otra calificación(s/n)")
        if(resp=="n" or resp =="N"):
            ciclo = False

def promedio():
    total = 0.0
    for i in lista:
        total = total + i
    promedio = total/len(lista)
    print(promedio)
    
def NAR():
    a = 0
    r = 0
    for i in lista:
        if (i<70):
            r = r + 1
        else:
            a = a + 1
    print("Numero de aprobados:",a)
    print("Numero de reprobados:",r)

def PAR():
    a = 0
    r = 0
    for i in lista:
        if (i<70):
            r = r + 1
        else:
            a = a + 1
    print("Numero de aprobados:",((a*100)/len(lista)))
    print("Numero de reprobados:",((r*100)/len(lista)))
    
def NM80():
    m = 0
    for i in lista:
        if (i>80):
            m = m + 1

    print("Numero de alumnos con calificación mayor a 80:",m)

def main():
    opc=0
    while(opc!=6):
        print("-----------------------------------------")
        print("1.-Agregar calificaciones")
        print("2.-Promedio general")
        print("3.-Numero de alumnos aprobados y reprobados")
        print("4.-Porcentaje de alumnos aprobados y reprobados")
        print("5.-Numero de alumnos con calificación mayor a 80")
        print("6.-Salir")
        print("-----------------------------------------")
        opc = int(input("Ingrese una opción entre 1 y 6: \n"))
        print("-----------------------------------------")
        if(opc==1):
            agregar()
        elif(opc==2):
            promedio()
        elif(opc==3):
            NAR()
        elif(opc==4):
            PAR()
        elif(opc==5):
            NM80()
        elif(opc==6):
            print("Saliendo de la aplicación...")
        else:
            print("Opcion no valida ingrese una opción entre 1 y 6")
    
        

if __name__ == "__main__":
    main()