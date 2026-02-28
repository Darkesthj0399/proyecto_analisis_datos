import pandas as pd

def cargar_datos(ruta_archivo):
    """Lee el dataset de e-shop clothing 2008.
    Argumentos: ruta_archivo (str)
    Retorna: DataFrame de pandas
    """
    try:
        # Ajustar el separador (sep) según el formato real del archivo
        df = pd.read_csv(ruta_archivo, sep=';')
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None