# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Restaurantes', page_icon='🍛', layout='wide')

# =============================== Functions =====================================

def rest_votes(df):
    cols = ['restaurant_name', 'votes', 'country']
    group = df.loc[:, cols].groupby(['restaurant_name', 'country']).sum().sort_values(['votes', 'country'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(15), x='restaurant_name', y='votes', text_auto='votes', color='country', labels={'restaurant_name':'', 'votes':'', 'country':'País'})

    return fig

def rest_for_two(df):
    cols = ['restaurant_name', 'average_cost_for_two', 'country']
    group = df.loc[:, cols].groupby(['restaurant_name', 'country']).max().sort_values(['average_cost_for_two', 'country'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(5), x='restaurant_name', y='average_cost_for_two', text_auto='average_cost_for_two', color='country', labels={'restaurant_name':'', 'average_cost_for_two':'', 'country':'País'})

    return fig

def cuisi_for_two(df):
    cols = ['cuisines', 'average_cost_for_two', 'country']
    group = df.loc[:, cols].groupby(['cuisines', 'country']).mean().sort_values(['average_cost_for_two', 'country'], ascending=[False, True]).reset_index()

    fig = px.bar(group.head(5), x='cuisines', y='average_cost_for_two', text_auto='.2f', color='country', labels={'cuisines':'', 'average_cost_for_two':'', 'country':'País'})

    return fig

def rest_rating(df):
    cols = ['restaurant_name', 'aggregate_rating', 'country']
    group = df.loc[:, cols].groupby(['restaurant_name', 'country']).mean().sort_values(['aggregate_rating', 'country'], ascending=[False, True]).reset_index()
    
    fig = px.bar(group.head(15), x='restaurant_name', y='aggregate_rating', text_auto='aggregate_rating', color='country', labels={'restaurant_name':'', 'aggregate_rating':'', 'country':'País'})

    return fig

def rest_online(df):
    df['has_online_delivery'] = df['has_online_delivery'].apply(lambda x: 'Yes' if x == 1 else 'No')
    cols = ['votes', 'has_online_delivery']
    group = df.loc[:, cols].groupby('has_online_delivery').mean().reset_index()
    
    fig = px.pie(group, values='votes', names='has_online_delivery', labels={'votes':'Avaliações', 'has_online_delivery':'Possui Entrega'})

    return fig

def rest_booking(df):
    df['has_table_booking'] = df['has_table_booking'].apply(lambda x: 'Yes' if x == 1 else 'No')
    cols = ['average_cost_for_two', 'has_table_booking']
    group = df.loc[:, cols].groupby('has_table_booking').mean().reset_index()
    
    fig = px.pie(group, values='average_cost_for_two', names='has_table_booking', labels={'average_cost_for_two':'Preço', 'has_table_booking':'Possui Reserva'})

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
country_options = st.sidebar.multiselect('Escolha um país: ', df.loc[:, 'country'].unique().tolist(), default=['Brazil', 'Philippines', 'Qatar', 'United Arab Emirates'])
cuisines_options = st.sidebar.multiselect('Tipo de culinária: ', df.loc[:, 'cuisines'].unique().tolist(), default=['Italian', 'Japanese', 'BBQ', 'Indian'])
st.sidebar.markdown("""---""")

# Vinculando o filtro com os dados
linhas_selecionadas = df['country'].isin(country_options)
df = df.loc[linhas_selecionadas, :]

linhas_selecionadas = df['cuisines'].isin(cuisines_options)
df = df.loc[linhas_selecionadas, :]

st.sidebar.markdown('##### Powered by Silas Nakano')

# ---------------------------------- Main Page --------------------------------------
st.markdown("# 🍛 Visão Restaurantes")
st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Top 15 Restaurantes com maior registro de avaliação</h5>", unsafe_allow_html=True)
    fig = rest_votes(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    restaurant, cuisines = st.columns(2, gap='large')

    with restaurant:
        st.markdown("##### Top 5 Restaurantes com maior valor médio de um prato para 2")
        fig = rest_for_two(df)
        st.plotly_chart(fig, use_container_width=True)
    
    with cuisines:
        st.markdown("##### Top 5 Tipos de culinária com maior valor médio de um prato para 2")
        fig = cuisi_for_two(df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    st.markdown("<h5 style='text-align: center'>Top 15 Restaurantes com maior nota</h5>", unsafe_allow_html=True)
    fig = rest_rating(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    online, booking = st.columns(2, gap='large')

    with online:
        st.markdown("##### Avaliações registradas de acordo com a entrega online")
        fig = rest_online(df)
        st.plotly_chart(fig, use_container_width=True)

    with booking:
        st.markdown("##### Valor médio de um prato para 2 de acordo com reservas")
        fig = rest_booking(df)
        st.plotly_chart(fig, use_container_width=True)
