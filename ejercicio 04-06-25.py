"""
elabore un sistema en python que les permita distribuir las calificaciones  del estudiante de las siguientes asignaturas matematica, castellano y base de datos 1 crea una ficha con la siguiente informacion del estudiante nombre, indique en que asignatura se encuentra el estudiante de las 3 dadas, numero de identifiacion, carrera generar un txt aparte que permita almacenar la informacion del estudiante 
"""

def main():
    # Solicitar  los datos del estudiante
    nombre = input("Nombre completo del estudiante: ")
    asignatura = input("Asignatura actual (Matemática/Castellano/Base de Datos 1): ").strip().title()
    identificacion = input("Número de identificación: ")
    carreraha = input("Carrera: ")

    # Validar asignatura dadas
    asignaturas_validas = ["Matemática", "Castellano", "Base De Datos 1"] #escribir bien la carrera poner asi tal cual de lo contrario no correra
    if asignatura not in asignaturas_validas:
        print("Error: Asignatura inválida. Debe ser Matemática, Castellano o Base de Datos 1.")
        return

    # Solicitar calificaciones de las asignaturas
    calificaciones = {}
    for asignatura_valida in asignaturas_validas:
        try:
            calificacion = float(input(f"Calificación de {asignatura_valida}: "))
            calificaciones[asignatura_valida] = calificacion
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
            return

    # archivo TXT
    nombre_archivo = f"ficha_{identificacion}.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("FICHA ACADÉMICA DEL ESTUDIANTE\n")
        archivo.write("=" * 40 + "\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Asignatura actual: {asignatura}\n")
        archivo.write(f"Identificación: {identificacion}\n")
        archivo.write(f"Carrera: {carrera}\n\n")
        archivo.write("CALIFICACIONES\n")
        archivo.write("-" * 40 + "\n")
        for asignatura_valida, nota in calificaciones.items():
            archivo.write(f"{asignatura_valida}: {nota:.1f}\n")

    print(f"Archivo '{nombre_archivo}' generado exitosamente.")

if __name__ == "__main__":
    main()