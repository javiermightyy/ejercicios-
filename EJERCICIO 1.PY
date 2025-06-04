print("Calculadora de áreas de triángulos")

# Solicitar el número de triángulos con validación
while True:
    try:
        n = int(input("Ingrese el número de triángulos a procesar: "))
        if n <= 0:
            print("Error: debe ingresar un número entero positivo.")
        else:
            break
    except ValueError:
        print("Error: ingrese un número entero válido.")

# Procesar cada triángulo
for i in range(n):
    print(f"\nTriángulo {i + 1}")
    # Validar base
    while True:
        try:
            base = float(input("Ingrese la base del triángulo: "))
            if base <= 0:
                print("La base debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Error: ingrese un número válido.")
    # Validar altura
    while True:
        try:
            altura = float(input("Ingrese la altura del triángulo: "))
            if altura <= 0:
                print("La altura debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Error: ingrese un número válido.")
    # Calcular y mostrar área
    area = (base * altura) / 2
    print(f"El área del triángulo {i + 1} es: {area:.2f}")
