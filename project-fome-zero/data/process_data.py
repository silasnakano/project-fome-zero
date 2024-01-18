import pandas as pd
import inflection

# Preenchimento do nome dos países
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]

# Criação do Tipo de categoria de Comida
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

# Criação do nome das Cores
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

def rename_columns(dataframe):
    df1 = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df1.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df1.columns = cols_new

    return df1

def clean_code(df1):

    # Renomear as colunas
    df1 = rename_columns(df1)

    # Remoção dos valores NA
    df1 = df1.dropna()

    # Criação de novas colunas
    df1['price_type'] = df1.loc[:, 'price_range'].apply(lambda x: create_price_tye(x))
    df1['country'] = df1.loc[:, 'country_code'].apply(lambda x: country_name(x))
    df1['color_name'] = df1.loc[:, 'rating_color'].apply(lambda x: color_name(x))
    
    # Categorizar tipo de culinária
    df1['cuisines'] = df1.loc[:, 'cuisines'].apply(lambda x: x.split(",")[0])

    # Remover dados duplicados
    df1 = df1.drop_duplicates()

    return df1

# Leitura dos dados
df = pd.read_csv('raw/zomato.csv')

# Limpeza dos dados
df1 = clean_code(df)

# Exportar dados processados para novo arquivo csv
df1.to_csv('processed/zomato_processed.csv', index=False)
