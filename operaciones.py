#funciones
#muestra como trabajan los métodos o funciones en python
#ArroyoBrayan
#29/06/2019

#------------------------------
#función para sumar 2 enteros
#------------------------------
def suma (num1,num2):
   return num1+num2
#------------------------------
#función para restar 2 enteros
#------------------------------
def resta (num1,num2):
   return num1-num2
#------------------------------
#función para multiplicar 2 enteros
#------------------------------
def mul (num1,num2):
   return num1*num2
#------------------------------
#función para dividir 2 enteros
#------------------------------
def div (num1,num2):
   return num1/num2
#------------------------------
#función para comparar 2 enteros
#------------------------------
def comparar(num1,num2):
   if (num1 > num2):
       print("El numero mayor es:",num1)
   elif(num2>num1):
       print("El numero mayor es:",num2)
   elif(num1==num2):
       print("Los numeros son iguales")
#------------------------------
#función para hacer un ciclo con for
#------------------------------       
def cuenta(num1,num2):
    for i in range(num1,num2+1):
        print("valor de i:",i)
      
#función main
def main ():
    #variable para el while
    ciclo = True
    while(ciclo):
        print ( "---Operaciones básicas con enteros---")
        print ( "\n")
        n1 = int(input("Introduce primer número:"))
        n2 = int(input("Introduce segundo número:"))
   
        #invoca las funciones
        print ( "La suma es:", suma (n1,n2))
        print ( "La resta es:", resta (n1,n2))
        print ( "La multiplicación es:", mul (n1,n2))
        print ( "La división es:", div (n1,n2))
        print ( comparar(n1,n2))
        print ( cuenta(n1,n2))
        
        cad = input(" otro calculo (s/n)?")
        if (cad == "S" or cad== "s"):
            ciclo=True
        else:
            ciclo=False
            

if __name__ == "__main__":
   main ()