# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Países', page_icon='🗺️', layout='wide')

# =============================== Functions =====================================

def rest_country(df):
    cols = ['country', 'restaurant_id']
    group = df.loc[:, cols].groupby('country').nunique().sort_values('restaurant_id', ascending=False).reset_index()

    fig = px.bar(group, x='country', y='restaurant_id', text='restaurant_id', labels={'country':'', 'restaurant_id':''})

    return fig

def city_country(df):
    cols = ['country', 'city']
    group = df.loc[:, cols].groupby('country').nunique().sort_values('city', ascending=False).reset_index()

    fig = px.bar(group, x='country', y='city', text='city', labels={'country':'', 'city':''})

    return fig

def votes_country(df):
    cols = ['country', 'votes']
    group = df.loc[:, cols].groupby('country').mean().sort_values('votes', ascending=False).reset_index()

    fig = px.bar(group, x='country', y='votes', text='votes', text_auto='.2f', labels={'country':'', 'votes':''})

    return fig

def price_two_country(df):
    cols = ['country', 'average_cost_for_two']
    group = df.loc[:, cols].groupby('country').mean().sort_values('average_cost_for_two', ascending=False).reset_index()

    fig = px.bar(group, x='country', y='average_cost_for_two', text='average_cost_for_two', text_auto='.2f', labels={'country':'', 'average_cost_for_two':''})

    return fig

def ratings_country(df):
    cols = ['country', 'aggregate_rating']
    group = df.loc[:, cols].groupby('country').mean().sort_values('aggregate_rating', ascending=False).reset_index()

    fig = px.bar(group, x='country', y='aggregate_rating', text='aggregate_rating', text_auto='.2f', labels={'country':'', 'aggregate_rating':''})

    return fig

# ============================ Estrutura do Código ===============================

# Load dataset
df = pd.read_csv('./data/processed/zomato_processed.csv')

# ----------------------------------- Sidebar --------------------------------------

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

st.sidebar.markdown('##### Powered by Silas Nakano')

# ---------------------------------- Main Page --------------------------------------
st.markdown("# 🗺️ Visão Países")
st.markdown("""---""")

with st.container():
    price_4, cuisines, ratings, delivery, booking = st.columns(5, gap='large')

    with price_4:
        # Restaurantes com o nível de preço igual a 4
        st.markdown('##### Nível de preço igual a 4')
        cols = ['country', 'restaurant_id']
        linhas_selecionadas = df['price_range'] == 4
        group = df.loc[linhas_selecionadas, cols].groupby('country').count().sort_values('restaurant_id', ascending=False).head(10)

        st.dataframe(group)

    with cuisines:
        # Culinária distintas
        st.markdown('##### Culinária distintas')
        cols = ['country', 'cuisines']
        group = df.loc[:, cols].groupby('country').nunique().sort_values('cuisines', ascending=False).head(10)

        st.dataframe(group)

    with ratings:
        # Restaurantes com avaliações feitas
        st.markdown('##### Avaliações feitas')
        cols = ['country', 'votes']
        group = df.loc[:, cols].groupby('country').sum().sort_values('votes', ascending=False).head(10)

        st.dataframe(group)

    with delivery:
        # Restaurantes que possuem entrega
        st.markdown('##### Restaurantes com entrega')
        cols = ['country', 'restaurant_id']
        linhas_selecionadas = df['is_delivering_now'] == 1
        group = df.loc[linhas_selecionadas, cols].groupby('country').count().sort_values('restaurant_id', ascending=False).head(10)

        st.dataframe(group)

    with booking:
        st.markdown('##### Restaurantes com reserva')
        # Restaurantes que possuem reserva
        cols = ['country', 'restaurant_id']
        linhas_selecionadas = df['has_table_booking'] == 1
        group = df.loc[linhas_selecionadas, cols].groupby('country').count().sort_values('restaurant_id', ascending=False).head(10)

        st.dataframe(group)

    st.markdown("""---""")

with st.container():
    # Vinculando o filtro com os dados
    linhas_selecionadas = df['country'].isin(country_options)
    df = df.loc[linhas_selecionadas, :]

    st.markdown("<h5 style='text-align: center'>Quantidade de Restaurantes por País</h5>", unsafe_allow_html=True)
    fig = rest_country(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Quantidade de Cidades por País</h5>", unsafe_allow_html=True)
    fig = city_country(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    ratings, cost = st.columns(2, gap='large')

    with ratings:
        st.markdown("##### Média de Avaliações feitas por País")
        fig = votes_country(df)
        st.plotly_chart(fig, use_container_width=True)
    
    with cost:
        st.markdown("##### Média de preço de um prato para 2 pessoas por País")
        fig = price_two_country(df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Notas Médias registradas por País</h5>", unsafe_allow_html=True)
    fig = ratings_country(df)
    st.plotly_chart(fig, use_container_width=True)
