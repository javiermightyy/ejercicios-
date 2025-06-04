print("Bienvenido al sistema de venta de entradas.")

stock = 70
next_seat = 1  # Próxima silla disponible

while True:
    print("\nMenú de opciones:")
    print("1. Dar la bienvenida")
    print("2. Ver disponibilidad de sillas y cuáles son")
    print("3. Comprar entradas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == '1':
        print("\n¡Bienvenido al teatro! Esperamos que disfrute de la función.\n")
    
    elif opcion == '2':
        disponibles = stock - (next_seat - 1)
        if disponibles <= 0:
            print("\nNo hay entradas disponibles.\n")
        else:
            print(f"\nHay {disponibles} entradas disponibles.")
            print(f"Sillas disponibles: desde la número {next_seat} hasta la 70.\n")
    
    elif opcion == '3':
        while True:
            try:
                cantidad = int(input("\nIngrese el número de entradas a comprar: "))
                if cantidad <= 0:
                    print("Error: la cantidad debe ser positiva.")
                else:
                    disponibles = stock - (next_seat - 1)
                    if cantidad > disponibles:
                        print(f"Error: solo hay {disponibles} entradas disponibles.")
                    else:
                        inicio = next_seat
                        fin = next_seat + cantidad - 1
                        next_seat += cantidad
                        print(f"\n¡Compra exitosa! Entradas asignadas: sillas {inicio} a {fin}.\n")
                    break
            except ValueError:
                print("Error: ingrese un número válido.")
    
    elif opcion == '4':
        respuesta = input("\n¿Desea salir? (si/no): ").lower().strip()
        if respuesta == 'si':
            print("\nGracias por usar nuestro sistema. ¡Hasta luego!\n")
            break
        else:
            continue
    
    else:
        print("\nOpción no válida. Intente nuevamente.\n")
