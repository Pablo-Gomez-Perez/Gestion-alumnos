#
#Crear un sistema de gestión de estudiantes de una escuela. El objetivo es almacenar y procesar información de varios estudiantes,
#como su nombre, materias y calificaciones.
#    
#Detalles del ejercicio:
#    1. Crear un diccionario anidado:
#        -> El Diccionario principal contendrá como claves lo nombres de los estudiantes.
#        -> Cada estudiante tendrá asociado otro diccionario con:
#            -> Sus materias (Como claves) y
#            -> Las calificaciones correspondientes (Como valores).
#                
#    2. Operaciones requeridas:
#        -> añadir un nuevo estudiante: Se deb poder añadir un nuevo estudiante con
#            sus materias y calificaciones.
#        -> Añadir una nueva materia a un estudiante existente: Poder agregar una nueva
#            materia para un estudiante ya registrado.
#        -> Actualizar la claificacion de una materia: Modificar la calificacion de un estudiante
#            en una materia específica
#        -> Eliminar un estudiante: Permitir eliminar a un estudiante del diccionario.
#        -> Calcular el promedio de calificaciones de un estudiante: Crear una función que reciba 
#            el nombre del estudiante y devualva su promedio de calificaciones.
#        -> Listar todos los estudiantes con sus calificaciones: Mostrar de forma clara todos
#            los estudiantes con sus respectivas materias y calificaciones.
#        
#    ejemplo
#        
#    estudiantes = {
#        
#        "Juan Perez": {
#            "matematicas":85,
#            "historia": 90,
#            "ciencias": 78
#        },
#        "Ana Gomez": {
#            "matematicas": 95,
#            "historia": 88,
#            "ciencias": 92,
#            "arte": 100
#        }
#        
#    }

# -*- coding: utf-8 -*-

from functools import reduce


def add_student(estudiantes, nombre, materias_calificaciones):
    return lambda: {**estudiantes(), nombre: materias_calificaciones()}


def add_subject(estudiantes, nombre, materia, calificacion):
    return lambda: (
        {**estudiantes(), nombre: {**estudiantes()[nombre], materia: calificacion}}
        if nombre in estudiantes() else estudiantes()
    )


def update_grade(estudiantes, nombre, materia, nueva_calificacion):
    return lambda: (
        {**estudiantes(), nombre: {**estudiantes()[nombre], materia: nueva_calificacion}}
        if nombre in estudiantes() and materia in estudiantes()[nombre] else estudiantes()
    )


def remove_student(estudiantes, nombre):
    return lambda: {k: v for k, v in estudiantes().items() if k != nombre}


def calculate_average(estudiantes, nombre):
    return lambda: (
        (lambda calificaciones: reduce(lambda acc, x: acc + x, calificaciones, 0) / len(calificaciones)
         if len(calificaciones) > 0 else 0)(list(estudiantes()[nombre].values()))
        if nombre in estudiantes() else 0
    )


def list_students(estudiantes):
    return lambda: "\n".join(map(lambda item: f"{item[0]}: {item[1]}", estudiantes().items()))


def get_input(prompt, callback):
    return callback(input(prompt))

def main_menu(estudiantes):
    print("\nSistema de Gestion de Estudiantes")
    print("1. Agregar un nuevo estudiante")
    print("2. Agregar una nueva materia a un estudiante existente")
    print("3. Actualizar la calificacion de una materia")
    print("4. Eliminar un estudiante")
    print("5. Calcular el promedio de calificaciones de un estudiante")
    print("6. Listar todos los estudiantes con sus calificaciones")
    print("7. Salir")

    get_input("Selecciona una opcion: ", lambda opcion: process_option(opcion, estudiantes))

def process_option(opcion, estudiantes):
    if opcion == "1":
        get_input("Introduce el nombre del estudiante: ", lambda nombre: 
            get_input("Introduce las materias y calificaciones (ej. matematicas:85, historia:90): ", 
                lambda materias: main_menu(
                    add_student(estudiantes, nombre, 
                        lambda: dict(map(lambda x: (x.split(":")[0].strip(), int(x.split(":")[1].strip())), materias.split(",")))
                    )
                )
            )
        )

    elif opcion == "2":
        get_input("Introduce el nombre del estudiante: ", lambda nombre:
            get_input("Introduce la nueva materia: ", lambda materia:
                get_input("Introduce la calificacion: ", lambda calificacion:
                    main_menu(add_subject(estudiantes, nombre, materia, int(calificacion)))
                )
            )
        )

    elif opcion == "3":
        get_input("Introduce el nombre del estudiante: ", lambda nombre:
            get_input("Introduce la materia a actualizar: ", lambda materia:
                get_input("Introduce la nueva calificacion: ", lambda nueva_calificacion:
                    main_menu(update_grade(estudiantes, nombre, materia, int(nueva_calificacion)))
                )
            )
        )

    elif opcion == "4":
        get_input("Introduce el nombre del estudiante a eliminar: ", lambda nombre:
            main_menu(remove_student(estudiantes, nombre))
        )

    elif opcion == "5":
        get_input("Introduce el nombre del estudiante: ", lambda nombre:
            (lambda promedio: print(f"El promedio de {nombre} es: {promedio()}"))(calculate_average(estudiantes, nombre))
            or main_menu(estudiantes)
        )

    elif opcion == "6":        
        (lambda lista: print("Lista de estudiantes y sus calificaciones:\n" + lista()))(list_students(estudiantes))        
        main_menu(estudiantes)


    elif opcion == "7":
        print("Saliendo del sistema...")

    else:
        print("Opcion no valida, intenta de nuevo.")
        main_menu(estudiantes)


# Iniciar el menú principal
main_menu(lambda : {})
