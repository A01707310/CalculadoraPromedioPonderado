def promediar_materia(NOTAS) -> float:

    """
    Función que dada una cantidad de notas de una materia, registra para cada una su ponderación y la calificación correspondiente.
    Devuelve el promedio ponderado a partir de dicha información.
    """

    total_ponderacion = 0
    suma_ponderada = 0

    for i in range(NOTAS):
        if not i == NOTAS-1:
            ponderacion = float(input(f"Porcentaje en decimales que representa la nota {i + 1}: "))
            while ponderacion < 0 or ponderacion >= 1.0: 
                ponderacion = float(input(f"Porcentaje en decimales que representa la nota {i + 1}: "))
            calificacion = float(input(f"Del 0 al 100, ingresa la calificación obtenida para la nota {i + 1}: "))
            while calificacion < 0 or calificacion > 100:
                calificacion = float(input(f"Del 0 al 100, ingresa la calificación obtenida para la nota {i + 1}: "))
        else:
            ponderacion = 1.0-total_ponderacion
            calificacion = float(input(f"Calificación obtenida para la nota restante: "))
            while calificacion < 0 or calificacion > 100:
                calificacion = float(input(f"Calificación obtenida para la nota restante: "))
        
        suma_ponderada += ponderacion * calificacion
        total_ponderacion += ponderacion

    promedio_ponderado = suma_ponderada / total_ponderacion
    return f"{promedio_ponderado:.2f}"

print(promediar_materia(2))
