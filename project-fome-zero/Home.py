# ======================== Bibliotecas & Page_config ===================
import pandas as pd
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title='Home',
    page_icon='🏠',
    layout='wide'
)

# =============================== Functions ==============================

def calcule_number(cols, op):
    if op == 'unique':
        result = df.loc[:, cols].nunique()
    elif op == 'sum':
        result = df.loc[:, cols].sum()
    
    return result

# ============================ Estrutura do Código ==========================

# Load dataset
df = pd.read_csv('data/processed/zomato_processed.csv')

# ------------------------------ Sidebar ----------------------------------

# Load Img
image = Image.open('logo.png')
st.sidebar.image(image, width=120)

# Título e Subtítulo
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown(' #### Best Marketplace')
st.sidebar.markdown("""---""")

# Filtros
st.sidebar.markdown('### Filtros')
country_options = st.sidebar.multiselect('Escolha um pais: ', df.loc[:, 'country'].unique().tolist(), default=['Brazil', 'Philippines', 'Qatar', 'United Arab Emirates'])
st.sidebar.markdown("""---""")

# Button Download
st.sidebar.markdown('### Dados Tratados')
st.sidebar.download_button(label='Download', data=df.to_csv(index=False, sep=";"), file_name='zomato_processed.csv', mime='text/csv')
st.sidebar.markdown("""---""")

st.sidebar.markdown('##### Powered by Silas Nakano')

# ------------------------------ Main Page ----------------------------------

st.write('# Fome Zero')

st.markdown(
    """
    Este Dashboard foi construído para facilitar o encontro e negociações de clientes e restaurantes.
    ### Como utilizar esse Dashboard:
    - Países: 
        - Indicadores de crescimento por países.
    - Cidades:
        - Métricas dos maiores restaurantes por cidade.
    - Restaurantes:
        - Indicadores dos maiores restaurantes.
    - Culinária:
        - Insights de tipos de culinária com os melhores restaurantes.
    ### Ask for help!
    - Time de Data Science no Discord
        - @silasnakano
    """
)
st.markdown("""---""")

with st.container():
    st.markdown('### Indicadores da nossa plataforma:')

    restaurant, country, city, votes, cuisines = st.columns(5, gap='large')

    with restaurant:
        # Quantidade de restaurantes únicos
        uniq_rest = calcule_number('restaurant_id', op='unique')
        restaurant.metric('Restaurantes', uniq_rest)

    with country:
        # Quantidade de países únicos
        uniq_country = calcule_number('country_code', op='unique')
        country.metric('Países', uniq_country)

    with city:
        # Quantidade de cidades únicas
        uniq_city = calcule_number('city', op='unique')
        city.metric('Cidades', uniq_city)

    with votes:
        # Total de avaliações feitas
        sum_votes = calcule_number('votes', op='sum')
        votes.metric('Votos Registrados', f"{sum_votes:,}".replace(",", "."))

    with cuisines:
        # Total de tipos de culinária
        uniq_cuis = calcule_number('cuisines', op='unique')
        cuisines.metric('Tipos de Culinária', uniq_cuis)
    
    st.markdown("""---""")

with st.container():
    # Vinculando o filtro com os dados
    linhas_selecionadas = df['country'].isin(country_options)
    df = df.loc[linhas_selecionadas, :]

    # Gerando o Mapa
    fig = folium.Figure(width=1920, height=1080)
    map = folium.Map(max_bounds=True).add_to(fig)
    marker_cluster = MarkerCluster().add_to(map)

    for _, line in df.iterrows():
        name = line['restaurant_name']
        cost_for_two = line['average_cost_for_two']
        cuisines = line['cuisines']
        currency = line['currency']
        ratings = line['aggregate_rating']
        color = f'{line['color_name']}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggregate Rating: {}/5.0"
        html = html.format(name, cost_for_two, cuisines, currency, ratings)

        popup = folium.Popup(folium.Html(html, script=True), max_width=500)

        folium.Marker([line['latitude'], line['longitude']], popup=popup, icon=folium.Icon(color=color, icon='home', prefix='fa')).add_to(marker_cluster)

    folium_static(map, width=1024, height=768)
