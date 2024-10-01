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
#

