import random

# Variables globales
eventos = []
participantes = {}
resultados = {}
medallero = {}

# Función para registrar eventos deportivos
def registrar_evento():
    evento = input("Introduce el nombre del evento deportivo: ")
    eventos.append(evento)
    print(f"Evento '{evento}' registrado exitosamente.")

# Función para registrar participantes
def registrar_participante():
    nombre = input("Introduce el nombre del participante: ")
    pais = input("Introduce el país del participante: ")

    if pais not in participantes:
        participantes[pais] = []

    participantes[pais].append(nombre)
    print(f"Participante '{nombre}' de {pais} registrado exitosamente.")

# Función para simular eventos
def simular_evento():
    if not eventos:
        print("No hay eventos registrados. Registra un evento primero.")
        return
    if len(participantes) < 3:
        print("Debe haber al menos 3 participantes registrados para simular un evento.")
        return
    
    evento = random.choice(eventos)
    print(f"\nSimulando el evento: {evento}")
    
    # Crear una lista de todos los participantes
    todos_participantes = [(pais, nombre) for pais in participantes for nombre in participantes[pais]]
    if len(todos_participantes) < 3:
        print("No hay suficientes participantes para este evento.")
        return
    
    # Seleccionar de forma aleatoria tres participantes para el evento
    random.shuffle(todos_participantes)
    competidores = todos_participantes[:3]

    # Asignar posiciones aleatorias
    random.shuffle(competidores)

    # Asignar medallas (oro, plata, bronce)
    ganadores = {
        "Oro": competidores[0],
        "Plata": competidores[1],
        "Bronce": competidores[2]
    }

    # Guardar resultados del evento
    resultados[evento] = ganadores

    # Actualizar el medallero
    for medalla, (pais, participante) in ganadores.items():
        if pais not in medallero:
            medallero[pais] = {"Oro": 0, "Plata": 0, "Bronce": 0}
        medallero[pais][medalla] += 1

    print("Resultados del evento:")
    for medalla, (pais, participante) in ganadores.items():
        print(f"{medalla}: {participante} de {pais}")

# Función para mostrar informes
def generar_informe():
    if not resultados:
        print("No hay resultados disponibles.")
        return

    print("\n--- Informe Final de los Juegos Olímpicos ---")
    for evento, ganadores in resultados.items():
        print(f"\nEvento: {evento}")
        for medalla, (pais, participante) in ganadores.items():
            print(f"  {medalla}: {participante} de {pais}")

    # Mostrar ranking de países
    print("\n--- Ranking de Países por Medallas ---")
    ranking = sorted(medallero.items(), key=lambda x: (x[1]["Oro"], x[1]["Plata"], x[1]["Bronce"]), reverse=True)
    
    for idx, (pais, medallas) in enumerate(ranking, start=1):
        print(f"{idx}. {pais} - Oro: {medallas['Oro']}, Plata: {medallas['Plata']}, Bronce: {medallas['Bronce']}")

# Menú principal
def menu():
    while True:
        print("\n--- Juegos Olímpicos París 2024 ---")
        print("1. Registro de eventos")
        print("2. Registro de participantes")
        print("3. Simulación de eventos")
        print("4. Creación de informes")
        print("5. Salir del programa")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            registrar_evento()
        elif opcion == '2':
            registrar_participante()
        elif opcion == '3':
            simular_evento()
        elif opcion == '4':
            generar_informe()
        elif opcion == '5':
            print("Saliendo del programa. ¡Gracias por participar en los Juegos Olímpicos!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
