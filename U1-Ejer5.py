# Ejercicio 5: Realice un programa en python que permita almacenar en un diccionario los datos
# generales de un alumno del ITC. Deberá poder imprimir cada uno de éstos datos a través de la 
# clave del diccinario y modificar al menos uno de los datos (ej. número telefónico).
def main():
    opc=0
    alumno={}
    while(opc!=4):
        print("-----------------------------------------")
        print("1.-Agregar Datos de alumno")
        print("2.-Mostrar diccionario")
        print("3.-Modificar datos")
        print("4.-Salir")
        print("-----------------------------------------")
        opc = int(input("Ingrese una opción entre 1 y 4: \n"))
        print("-----------------------------------------")
        if(opc==1):
            print("Ingrese datos generales del alumno")
            ciclo = True
            while(ciclo):
                clave = input("Ingrese el nombre del campo que quiere registrar: ")
                valor = input("Ingrese la información: ")
                alumno[clave]=valor
                resp = input("Desea capturar otra campo(s/n)")
                if(resp=="n" or resp =="N"):
                    ciclo = False
        elif(opc==2):
            print(alumno)
        elif(opc==3):
            ciclo = True
            while(ciclo):
                clave = input("Ingrese el nombre del campo que se quiere modificar: ")
                if (clave in alumno): 
                    valor = input("Ingrese la información: ")
                    alumno[clave]=valor
                else:
                    print("No existe el campo ingresado")
                resp = input("Desea modificar otra campo(s/n)")
                if(resp=="n" or resp =="N"):
                    ciclo = False
        elif(opc==4):
                print("Saliendo de la aplicación...")
        else:
            print("Opcion no valida ingrese una opción entre 1 y 4")

if __name__ == "__main__":
    main()
