import pandas as pd

# Cargamos los datos desde el archivo CSV
csv_file_path = r"D:\Prueba de ejecucion python\Act 2\transporte_masivo.csv"
df = pd.read_csv(csv_file_path)


# Definimos las reglas de prioridad para el tipo de transporte
def obtener_prioridad(row):
    if row["Transporte"] == "subway":
        return 1  # Subway es preferido
    elif row["Transporte"] == "bus":
        return 2  # Bus es la segunda opción
    else:
        return 3  # Otros medios de transporte, si los hubiese


# Calculamos la mejor ruta entre dos puntos
def encontrar_mejor_ruta(df, origen, destino):
    # Filtramos las rutas posibles entre el origen y el destino
    rutas_posibles = df[(df["Origen"] == origen) & (df["Destino"] == destino)]

    if rutas_posibles.empty:
        print(f"No hay rutas disponibles entre {origen} y {destino}.")
        return None

    # Aplicamos las reglas para encontrar la mejor ruta
    rutas_posibles["Prioridad"] = rutas_posibles.apply(obtener_prioridad, axis=1)

    # Ordenamos las rutas por prioridad y luego por menor demora
    mejor_ruta = rutas_posibles.sort_values(by=["Prioridad", "Demora"]).iloc[0]

    return mejor_ruta

origen = "A"
destino = "B"

mejor_ruta = encontrar_mejor_ruta(df, origen, destino)

if mejor_ruta is not None:
    print("Mejor ruta encontrada:")
    print(mejor_ruta)
else:
    print(f"No se encontró una ruta entre {origen} y {destino}.")
