#Nombre: listas.py
#Objetivo: muestra el funcionamiento de las listas en python
#Autor: Arroyo Chávez Brayan Alberto
#Fecha: 02/07/2019

lista=[]
#------------------------------
#metodo para agregar items a la lista 
#------------------------------
def agregarItem(dato):
    lista.append(dato)

#------------------------------
#metodo para mostrar items de la lista 
#------------------------------
def mostrarItem():
    j=1
    for i in  lista:
        print("item",j,"de la lista: ",i)
        j=j+1

#------------------------------
#metodo para eliminar items de la lista 
#------------------------------
def eliminarItem(dato):
    #buscamos item
    if (dato in lista):
        lista.remove(dato)
        print("Dato eliminado")
    else:
        print("Dato no existe en la lista")
def main():
    opc=0
    while(opc!=6):
        print("-----------------------------------------")
        print("1.-Agregar elementos a la lista")
        print("2.-Buscar un elemento en la lista")
        print("3.-Modificar un elemento de la lista")
        print("4.-Eliminar un elemento de la lista")
        print("5.-Imprimir los elementos de la lista")
        print("6.-Salir")
        print("-----------------------------------------")
        opc = int(input("Ingrese una opción entre 1 y 6: \n"))
        print("-----------------------------------------")
        if(opc==1):
            dato = input("Ingrese datos a la lista: \n")
            agregarItem(dato)
        elif(opc==2):
            print("buscar elemento")
        elif(opc==3):
            print("modificar elemento")
        elif(opc==4):
            eliminarItem(dato)
        elif(opc==5):
            mostrarItem()
        else:
            print("Opcion no valida ingrese una opción entre 1 y 6")

if __name__ == "__main__":
    main()