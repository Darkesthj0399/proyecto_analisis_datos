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
    

def calculate_conversion_rate(df):
    """Compara clics en categoría 'sale' (4) vs categorías regulares."""
    sale_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'] == 4])
    regular_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'].isin([1, 2, 3])])
    return {"sale_clicks": sale_clicks, "regular_clicks": regular_clicks}


def analyze_price_elasticity(df):
    """Compara clics entre productos con precio superior al promedio (1) y el resto (2)."""
    return df['PRICE 2'].value_counts()