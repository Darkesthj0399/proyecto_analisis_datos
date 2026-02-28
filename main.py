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
def clean_currency_data(df):
    """Valida que los precios sean positivos y no nulos."""
    df = df.dropna(subset=['PRICE'])
    df = df[df['PRICE'] > 0]
    return df


def calculate_conversion_rate(df):
    """Compara clics en categoría 'sale' (4) vs categorías regulares."""
    sale_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'] == 4])
    regular_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'].isin([1, 2, 3])])
    return {"sale_clicks": sale_clicks, "regular_clicks": regular_clicks}


def analyze_price_elasticity(df):
    """Compara clics entre productos con precio superior al promedio (1) y el resto (2)."""
    return df['PRICE 2'].value_counts()


def sales_funnel_analysis(df):
    """Analiza la pérdida de usuarios entre las páginas 1 y 5 de la tienda."""
    return df['PAGE'].value_counts().sort_index()

def price_impact_by_location(df):
    """Relaciona la ubicación de la foto (1-6) con el interés en productos caros."""
    return pd.crosstab(df['LOCATION'], df['PRICE 2'])