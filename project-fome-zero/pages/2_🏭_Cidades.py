# =============================== Bibliotecas & Page_config =================================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Cidades', page_icon='🏭', layout='wide')

# ====================================== Functions ==========================================

def rest_city(df):
    cols = ['restaurant_id', 'country', 'city']
    group = df.loc[:, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(15), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

def price2_city(df):
    cols = ['city', 'country', 'average_cost_for_two']
    group = df.loc[:, cols].groupby(['city', 'country']).mean().sort_values(['average_cost_for_two', 'city'], ascending=[False, True]).reset_index()

    fig = px.bar(group.head(5), x='city', y='average_cost_for_two', text_auto='.2f', color='country', labels={'city':'', 'average_cost_for_two':'', 'country':'País'})

    return fig

def booking_city(df):
    cols = ['city', 'country', 'restaurant_id']
    linhas_selecionadas = df['has_table_booking'] == 1
    group = df.loc[linhas_selecionadas, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(5), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

def rating4_city(df):
    cols = ['city', 'country', 'restaurant_id']
    linhas_selecionadas = df['aggregate_rating'] >= 4
    group = df.loc[linhas_selecionadas, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(7), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

def rating2_city(df):
    cols = ['city', 'country', 'restaurant_id']
    linhas_selecionadas = df['aggregate_rating'] <= 2.5
    group = df.loc[linhas_selecionadas, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(7), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

def cuisines_city(df):
    cols = ['city', 'country', 'cuisines']
    group = df.loc[:, cols].groupby(['city', 'country']).nunique().sort_values(['cuisines', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(15), x='city', y='cuisines', text_auto='cuisines', color='country', labels={'city':'', 'cuisines':'', 'country':'País'})

    return fig

def delivery_city(df):
    cols = ['city', 'country', 'restaurant_id']
    linhas_selecionadas = df['is_delivering_now'] == 1
    group = df.loc[linhas_selecionadas, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(5), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

def online_city(df):
    cols = ['city', 'country', 'restaurant_id']
    linhas_selecionadas = df['has_online_delivery'] == 1
    group = df.loc[linhas_selecionadas, cols].groupby(['city', 'country']).nunique().sort_values(['restaurant_id', 'city'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(5), x='city', y='restaurant_id', text_auto='restaurant_id', color='country', labels={'city':'', 'restaurant_id':'', 'country':'País'})

    return fig

# ================================= Estrutura do Código ======================================

# Load dataset
df = pd.read_csv('./data/processed/zomato_processed.csv')

# ---------------------------------------- Sidebar --------------------------------------------
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

# Vinculando o filtro com os dados
linhas_selecionadas = df['country'].isin(country_options)
df = df.loc[linhas_selecionadas, :]

st.sidebar.markdown('##### Powered by Silas Nakano')

# ---------------------------------------- Main Page --------------------------------------------
st.markdown("# 🏭 Visão Cidades")
st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Top 15 Cidades com Restaurantes registrados</h5>", unsafe_allow_html=True)
    fig = rest_city(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    price_for_two, booking = st.columns(2, gap='large')

    with price_for_two:
        st.markdown('##### Top 5 Cidades com restaurantes com maior valor médio de um prato para 2')
        fig = price2_city(df)
        st.plotly_chart(fig, use_container_width=True)

    with booking:
        st.markdown('##### Top 5 Cidades com restaurantes que fazem reservas')
        fig = booking_city(df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    rating_4, rating_2 = st.columns(2, gap='large')

    with rating_4:
        st.markdown('##### Top 7 Cidades com Restaurantes com média de avaliação acima de 4')
        fig = rating4_city(df)
        st.plotly_chart(fig, use_container_width=True)

    with rating_2:
        st.markdown('##### Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5')
        fig = rating2_city(df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Top 15 Cidades com Restaurantes com mais tipos culinários</h5>", unsafe_allow_html=True)
    fig = cuisines_city(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    delivery, online_delivery = st.columns(2, gap='large')

    with delivery:
        st.markdown('##### Top 5 Cidades com Restaurantes que fazem entrega')
        fig = delivery_city(df)
        st.plotly_chart(fig, use_container_width=True)

    with online_delivery:
        st.markdown('##### Top 5 Cidades com Restaurantes que aceitam pedidos online')
        fig = online_city(df)
        st.plotly_chart(fig, use_container_width=True)
