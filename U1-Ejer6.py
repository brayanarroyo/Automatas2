#Nombre: punto.py
#Objetivo: muestra el manejo de clases de python
#Autor: Arroyo Brayan
#Fecha: 05/07/2019

import math as mat
class punto(object):
    
    #constructor de la clase
    def __init__(self, valorX, valorY):
        self.x=valorX
        self.y=valorY
    #metodos self
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    #metodos set
    def setX(self,valorX):
        self.x=valorX
    
    def setY(self,valorY):
        self.y=valorY
    
    def toString(self):
        return "El punto tiene las siguientes coordenadas: ", self.x, self.y
    

class circunferencia(punto):
    def __init__(self, valorRadio):
        self.radio = valorRadio

    def getRadio(self):
        return self.radio

    def getArea(self):
        return mat.pi * mat.pow(self.getRadio(),2)

    def setRadio(self,valorRadio):
        self.radio = valorRadio

    def toString(self):
        return "La circunferencia tiene como centro: ",self.getX(), self.getY(), self.getRadio(),"El area es: ", self.getArea()
    
class cilindro(circunferencia):
    def __init__(self,altura):
        self.h = altura
    
    def getAltura(self):
        return self.h
    
    def getVolumen(self):
        return self.getArea()*self.h
    
    def setAltura(self,altura):
        self.h=altura
    
    def toString(self):
        return "La circunferencia tiene como centro: ",self.getX(), self.getY(), self.getRadio(),"El area es: ", self.getArea(),"El volumen es:",self.getVolumen()
            
#Programa principal
def main():
    #creamos el objeto p1
    p1 = punto(2,3)
    print(p1.toString())
    
    #creamos el objeto p2
    p2 = punto(0,0)
    
    #invocamos a los metodos set
    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())
    
    #creamos el objeto p3
    p3 = circunferencia(12.34)
    p3.setX(10)
    p3.setY(12)
    print(p3.toString())
    
    #creamos el objeti p4
    
    p4 = cilindro(9.81)
    p4.setX(2)
    p4.setY(2)
    p4.setRadio(3.12)
    print(p4.toString())
    
if __name__ == "__main__":
    main()
    