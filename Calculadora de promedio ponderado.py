def list_materias() -> list[str]:
    """Permite ingresar materias hasta que el usuario ingrese 'LISTO'"""
    
    L_materias = []
    cnt = 0

    Nombre_Materia = input("Ingresa el nombre de una de las materias cuyo promedio ponderado deseas hallar: ")

    while Nombre_Materia not in ["LISTO", "listo", "Listo", "lISTO"]:
        cnt += 1
        L_materias.append(f"Materia {cnt}: {Nombre_Materia}")
        Nombre_Materia = input("Ingresar el nombre de otra materia o continuar al siguiente paso ingresando 'LISTO': ")
    else:
        return L_materias
    
def obtener_num_de_notas(materias:list) -> list[str]:
    """Pregunta al usuario el número de notas para cada materia, en orden de la lista de materias"""

    sorteado_materias_num_notas = []
    
    for materia in materias:
        n_notas = int(input(f"Ingresa el número de notas que hay en la materia '{materia}': "))
        sorteado_materias_num_notas.append(n_notas)
 
    return sorteado_materias_num_notas

def promediar_materia(n_notas:int, materia:str) -> float:
    """
    Función que dada una cantidad de notas de una materia, registra para cada una su ponderación y la calificación correspondiente.
    Devuelve el promedio ponderado a partir de dicha información.
    """

    total_ponderacion = 0
    suma_ponderada = 0

    #Esta condicional evita que se haga un división de cero cuando se especifica la cantidad de 0 notas para una materia
    if n_notas > 0:
        ponderaciones_calificaciones = [(
            float(input(f"Ponderación de la nota {i + 1}, para '{materia}': ")),
            float(input(f"Del 0 al 100, ingresa la calificación obtenida en la nota {i + 1}, para '{materia}': "))) for i in range(n_notas)]
        
        suma_ponderada = sum([(i[0]*i[1]) for i in ponderaciones_calificaciones])
        total_ponderacion = sum([(i[0]) for i in ponderaciones_calificaciones])

        promedio_ponderado = suma_ponderada / total_ponderacion
        return f"{promedio_ponderado:.2f}"
    else:
        return 0.0

#Echando a andar el código, probablemente agreguemos una interfaz tkinter después, para hacerlo más intuitivo.
lista_De_Materias = list_materias()
lista_de_N_de_Notas = obtener_num_de_notas(lista_De_Materias)
for i in range(len(lista_de_N_de_Notas)):
    print(f"El promedio ponderado para la materia '{lista_De_Materias[i]}' es de {promediar_materia(n_notas=lista_de_N_de_Notas[i], materia=lista_De_Materias[i])}")
