"""
**Situación problema**
Tienes tres clases: Matemáticas, Física y Química y quieres conocer el
promedio ponderado para cada una, usando esta calculadora de promedio
ponderado, deberás ingresar las notas de cada materia y las ponderaciones
correspondientes a dichas notas para obtener tu promedio ponderado de cada
materia, que podría guardarse en un registro.
"""

def obtener_materias() -> list[str]:
    """Permite ingresar materias hasta que el usuario ingrese 'LISTO'"""
    materias = []
    entrada = input("INGRESA el nombre de una materia para ponderar sus \
notas: ")
    while entrada != "LISTO":
        materias.append(entrada)
        entrada = input("INGRESA otra materia o avanzar ingresando 'LISTO': ")
    print("\n")
    return materias
    
def obtener_num_de_notas(materias: list) -> list[str]:
    """Pregunta al usuario el número de notas para cada materia, en orden de
    la lista de materias"""

    sorteado_materias_num_notas = []
    
    for materia in materias:
        n_notas = int(input(f'INGRESA el número de notas en "{materia}": '))
        sorteado_materias_num_notas.append(n_notas)
    print("\n")
    return sorteado_materias_num_notas

def promediar_materia(n_notas: int, materia: str) -> float:
    """Dada una cantidad de notas, registra una ponderación y una
    calificación correspondiente para cada una. Devuelve el
    promedio ponderado a partir de estos registros."""

    total_ponderacion = 0
    suma_ponderada = 0

    # Esta condicional evita que se haga una división por cero cuando se
    # especifica la cantidad de 0 notas para una materia
    if n_notas > 0:
        # Usamos listas en lugar de tuplas
        ponderaciones_calificaciones = [
            [float(input(f'INGRESA la ponderación decimal (0.0 - 1.0) de \
la nota {i+1} de {n_notas}, en la materia "{materia}": ')),
            float(input(f"INGRESA la calificación de 0 a 100, obtenida \
para esta nota: "))]
            for i in range(n_notas)]
        
        # Cálculo de la suma ponderada y el total de ponderaciones
        suma_ponderada = sum([nota[0] * nota[1] for nota in\
        ponderaciones_calificaciones])

        total_ponderacion = sum([nota[0] for nota in \
        ponderaciones_calificaciones])

        promedio_ponderado = suma_ponderada / total_ponderacion
        return f"{promedio_ponderado:.2f}"
    else:
        return 0.0

def guardar_promedios(materias: list, promedios: list):
    """Función que intenta registrar los promedios correspondientes
    a cada calificación en un archivo dentro de la misma carpeta,
    en caso de excepción, avisa dentro de la terminal"""
    try:
        with open('promedios.txt', 'w', encoding="utf-8") as archivo:
            suma = 0
            for i in promedios:
                suma += float(i)
            suma = suma / len(promedios)
            for materia, promedio in zip(materias, promedios):
                archivo.write(f'{materia}: {promedio}\n')
            archivo.write(f"Promedio General: {suma}")
        print("Promedios guardados en 'promedios.txt'")
        archivo.close()
    except:
        print("Hubo un error al registrar tu(s) promedio(s) dentro de un\
archivo.")

lista_materias = obtener_materias()
lista_n_notas = obtener_num_de_notas(lista_materias)
lista_promedios = []

#iteramos sobre la lista de número de notas por materia
for i in range(len(lista_n_notas)):
    promedio = promediar_materia(lista_n_notas[i],lista_materias[i])
    print(f'"{lista_materias[i]}", promedio ponderado de {promedio}\n')
    lista_promedios.append(promedio)
guardar_promedios(lista_materias, lista_promedios)
