#variable 
lista_compras = []

#bucle para el menu

while True:
 

 #opciones del menu 


 print( "1. agrega los productos ")
 print("2. mostrar listas ")
 print("3. salir")


# eligir opciones
 opcion = input  (" seleciona una opcion (1,2,3): ")


# agregar productos 

 if opcion == "1":
   producto = input("escribe el producto que deseas agregar: ")
   lista_compras.append(producto)
   print(f' se agrego exitosamente: {producto}')



   #lista de los productos

 elif opcion == "2":
  print("la lista de los productos es :")
 for producto in lista_compras:
      print(F"- {producto}") 


# opcion para salir
 
 if opcion == "3":
   print(" vuelva pronto:")

 else:
       print ( "opcion no valida intentalo nuevamente:")  
