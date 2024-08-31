def list_materias() -> list[str]:
    """Permite ingresar materias hasta que el usuario ingrese 'LISTO'"""
    
    L_materias = []
    cnt = 0
    print("Ingresa 'LISTO' para el siguiente paso.")
    Nombre_Materia = input("Ingresa el nombre de las materias que quieras conocer el promedio ponderado: ")

    while Nombre_Materia != "LISTO":
        cnt += 1
        L_materias.append(f"Materia {cnt}: {Nombre_Materia}")
        Nombre_Materia = input("Ingresa el nombre de las materias que quieras conocer el promedio ponderado: ")
    else:
        return L_materias
    
def list_n_notas(materias:list) -> list[str]:
    """Pregunta al usuario el número de notas para cada materia, en orden de la lista de materias"""

    sorteado_materias_num_notas = []
    
    for materia in materias:
        try:
            sorteado_materias_num_notas.append(int(input(f"Ingresa el número de notas que hay en la materia '{materia}': ")))
        except:
            sorteado_materias_num_notas.append(0)
        
    return sorteado_materias_num_notas

def promediar_materia(n_notas:int, materia:str) -> float:
    """
    Función que dada una cantidad de notas de una materia, registra para cada una su ponderación y la calificación correspondiente.
    Devuelve el promedio ponderado a partir de dicha información.
    """

    total_ponderacion = 0
    suma_ponderada = 0

    ponderaciones_calificaciones = [(
        float(input(f"Ponderación de la nota {i + 1}, para '{materia}': ")),
        float(input(f"Del 0 al 100, ingresa la calificación obtenida en la nota {i + 1}, para '{materia}': "))
    ) for i in range(n_notas)]
    
    suma_ponderada = sum([(i[0]*i[1]) for i in ponderaciones_calificaciones])
    total_ponderacion = sum([(i[0]) for i in ponderaciones_calificaciones])

    promedio_ponderado = suma_ponderada / total_ponderacion
    return f"{promedio_ponderado:.2f}"


#Echando a andar la el código, probablemente agreguemos una interfaz tkinter después, para hacerlo intuitivo.
lista_De_Materias = list_materias()
lista_de_N_de_Notas = list_n_notas(lista_De_Materias)
for i in range(len(lista_de_N_de_Notas)):
    print(f"El promedio ponderado para la materia '{lista_De_Materias[i]}' es de {promediar_materia(n_notas=lista_de_N_de_Notas[i], materia=lista_De_Materias[i])}")
