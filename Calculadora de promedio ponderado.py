"""
**Situación problema**
Tienes cuatro clases: Matemáticas, Física, Química y Literatura. Cada una tiene diferentes ponderaciones (Matemáticas 40%, Física 30%, Química 20% y Literatura 10%).
Usando una calculadora de promedio ponderado, deberás ingresar tus calificaciones de cada materia y las ponderaciones correspondientes para obtener tu promedio final,
que se guardará en un registro.
"""

def list_materias() -> list[str]:
    """Permite ingresar materias hasta que el usuario ingrese 'LISTO'"""
    
    L_materias = []
    cnt = 0

    Nombre_Materia = input("Ingresa el nombre de una materia para ponderar sus notas: ")

    while Nombre_Materia not in ["LISTO", "listo", "Listo", "lISTO"]:
        cnt += 1
        L_materias.append(f"Materia {cnt}: {Nombre_Materia}")
        Nombre_Materia = input("Ingresar otra materia o avanzar ingresando 'LISTO': ")
    print("\n\n")
    return L_materias
    
def obtener_num_de_notas(materias:list) -> list[str]:
    """Pregunta al usuario el número de notas para cada materia, en orden de la lista de materias"""

    sorteado_materias_num_notas = []
    
    for materia in materias:
        n_notas = int(input(f'Ingresa el número de notas en "{materia}": '))
        print("\n")
        sorteado_materias_num_notas.append(n_notas)
 
    return sorteado_materias_num_notas

def promediar_materia(n_notas: int, materia: str) -> float:
    """
    Función que dada una cantidad de notas de una materia, registra para cada una su ponderación y la calificación correspondiente.
    Devuelve el promedio ponderado a partir de dicha información.
    """

    total_ponderacion = 0
    suma_ponderada = 0

    # Esta condicional evita que se haga una división por cero cuando se especifica la cantidad de 0 notas para una materia
    if n_notas > 0:
        # Usamos listas en lugar de tuplas
        ponderaciones_calificaciones = [
            [
                float(input(f'Ingresa la ponderación decimal de la nota {i + 1}, en la materia "{materia}"')),
                float(input(f"Ingresa la calificación de 0 a 100 que fue obtenida para esta nota: "))
            ] for i in range(n_notas)
        ]
        
        # Cálculo de la suma ponderada y el total de ponderaciones
        suma_ponderada = sum([nota[0] * nota[1] for nota in ponderaciones_calificaciones])
        total_ponderacion = sum([nota[0] for nota in ponderaciones_calificaciones])

        promedio_ponderado = suma_ponderada / total_ponderacion
        return f"{promedio_ponderado:.2f}"
    else:
        return 0.0

#Echando a andar el código, probablemente agreguemos una interfaz tkinter después, para hacerlo más intuitivo.
lista_De_Materias = list_materias()
lista_de_N_de_Notas = obtener_num_de_notas(lista_De_Materias)
for i in range(len(lista_de_N_de_Notas)):
    print(f'"{lista_De_Materias[i]}" tiene un promedio ponderado de {promediar_materia(n_notas=lista_de_N_de_Notas[i], materia=lista_De_Materias[i])}')
    print("\n")
