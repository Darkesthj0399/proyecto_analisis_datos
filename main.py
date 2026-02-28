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
    
def get_country_name(df):
    """Mapea códigos numéricos a nombres de países según el diccionario."""
    mapping = {1: "Australia", 2: "Austria", 3: "Belgium", 12: "unidentified",
    29: "Poland", 41: "United Kingdom", 42: "USA", 44: "com"}
    # Se recomienda completar el diccionario con los 47 códigos del archivo
    df['COUNTRY_NAME'] = df['COUNTRY'].map(mapping)
    return df
