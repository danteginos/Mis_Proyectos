# ejercicio 1 :basico
for i in range(101):     # imprime todos los numero enteros de 0 a 100
      print (i)
print ("")

# ejercicio 2  : Multiplo de 2
for i in range(2, 501, 2):   #  impime todos los numeros multiplos de 2 entre 2 y 500  
      print(i)
print(" ")     

# ejercicio 3  : Contando Vanilla ice
for i in range(1, 101):   # imprime los numeros enteros de l al 100. si es divisible por 5 imprime "ice ice". si es divisibl por 10 imprime "baby"
      if (i % 5 == 0) or ( i % 10 == 0):
         if   (i % 5 == 0):  print("Ice ice")
         if   (i % 10 == 0): print("baby")
      else :
                   print(i)  
print(" ")                         

# ejercicio 4  : wow numero gigante a la vista
suma=0
for i in range(2, 501, 2):      # suma los numeros pares de 0 a 500, imprime la suma total
        suma = suma + i
        print(i)
print("suma : ",suma)       
print(" ") 

# ejercicio 5  : Regresame al 3
for i in range(2024, 0, -3):     # imprime los numeros positivos comenzando desde 2024, en cuenta regresiva de 3 en 3
    print(i)
print(" ")   

# ejercicio 6  : Contador dinamico
numInicial=2
numFinal=10
multiplo=2
for i in range(numInicial, numFinal, multiplo):  #  imprime los numeros enteros que sean multiplo de variable multiplo
       print(i)