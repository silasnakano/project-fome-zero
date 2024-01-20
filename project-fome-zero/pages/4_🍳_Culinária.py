# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Culinária', page_icon='🍳', layout='wide')

# =============================== Functions =====================================

def cuisines_metric():

    cui = {'Italian':'', 'American':'', 'Arabian':'', 'Japanese':'', 'Home-made':''}
    cols = ['restaurant_id', 'restaurant_name', 'country', 'city', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'votes']

    for i in cui.keys():
        lines = df['cuisines'] == i

        cui[i] = (df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).iloc[0, :].to_dict())

    return cui

def tb_cuisines(df):
    df['has_online_delivery'] = df['has_online_delivery'].apply(lambda x: 'Yes' if x == 1 else 'No')
    df['has_table_booking'] = df['has_table_booking'].apply(lambda x: 'Yes' if x == 1 else 'No')
    df['is_delivering_now'] = df['is_delivering_now'].apply(lambda x: 'Yes' if x == 1 else 'No')

    cols = ['restaurant_id', 'restaurant_name', 'country', 'city', 'cuisines', 'average_cost_for_two', 'has_online_delivery', 'is_delivering_now', 'has_table_booking', 'aggregate_rating', 'votes']

    dataframe = df.loc[:, cols].sort_values(['aggregate_rating', 'votes'], ascending=[False, False]).reset_index(drop=True)

    return dataframe.head(top_n)

def top_cuisines(df):

    cols = ['cuisines', 'aggregate_rating']
    group = df.loc[:, cols].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=False).reset_index()
    
    fig = px.bar(group.head(top_n), x='cuisines', y='aggregate_rating', text='aggregate_rating', text_auto='.2f', labels={'cuisines':'', 'aggregate_rating':''})

    return fig

def online_rating(df):
    cols = ['cuisines', 'aggregate_rating']
    linhas_selecionadas = df['has_online_delivery'] == 'Yes'
    group = df.loc[linhas_selecionadas, cols].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=False).reset_index()
    
    fig = px.bar(group.head(top_n), x='cuisines', y='aggregate_rating', text='aggregate_rating', text_auto='.2f', labels={'cuisines':'', 'aggregate_rating':''})

    return fig

def online_votes(df):
    cols = ['cuisines', 'votes']
    linhas_selecionadas = df['has_online_delivery'] == 'No'
    group = df.loc[linhas_selecionadas, cols].groupby('cuisines').mean().sort_values('votes', ascending=False).reset_index()
    
    fig = px.bar(group.head(top_n), x='cuisines', y='votes', text='votes', text_auto='.2f', labels={'cuisines':'', 'votes':''})

    return fig

def delivery_rating(df):
    cols = ['cuisines', 'aggregate_rating']
    linhas_selecionadas = df['is_delivering_now'] == 'Yes'
    group = df.loc[linhas_selecionadas, cols].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=False).reset_index()

    fig = px.bar(group.head(top_n), x='cuisines', y='aggregate_rating', text='aggregate_rating', text_auto='.2f', labels={'cuisines':'', 'aggregate_rating':''})

    return fig

def delivery_votes(df):
    cols = ['cuisines', 'votes']
    linhas_selecionadas = df['is_delivering_now'] == 'No'
    group = df.loc[linhas_selecionadas, cols].groupby('cuisines').mean().sort_values('votes', ascending=False).reset_index()
    
    fig = px.bar(group.head(top_n), x='cuisines', y='votes', text='votes', text_auto='.2f', labels={'cuisines':'', 'votes':''})

    return fig

# ============================ Estrutura do Código ===============================

# Load dataset
df = pd.read_csv('project-fome-zero/data/processed/zomato_processed.csv')

# ----------------------------------- Sidebar --------------------------------------
# Load Img
image = Image.open('project-fome-zero/logo.png')
st.sidebar.image(image, width=120)

# Título e Subtítulo
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown(' #### Best Marketplace')
st.sidebar.markdown("""---""")

# Filtros
st.sidebar.markdown('### Filtros')
country_options = st.sidebar.multiselect('Escolha um pais: ', df.loc[:, 'country'].unique().tolist(), default=['Brazil', 'Philippines', 'Qatar', 'United Arab Emirates'])
cuisines_options = st.sidebar.multiselect('Tipo de culinária: ', df.loc[:, 'cuisines'].unique().tolist(), default=['Italian', 'Japanese', 'BBQ', 'Indian'])
top_n = st.sidebar.slider('Quantidade de Restaurantes:', 1, 15, 10)
st.sidebar.markdown("""---""")

st.sidebar.markdown('##### Powered by Silas Nakano')

# ---------------------------------- Main Page --------------------------------------
st.markdown("# 🍳 Visão Culinária")
st.markdown("""---""")

with st.container():
    st.markdown("<h4 style='text-align: center'>Melhores Restaurantes por Tipo de Culinária</h4>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

    cui = cuisines_metric()

    italian, american, arabian, japanese, homemade = st.columns(len(cui), gap='large')

    with italian:
        st.metric(label=f'Italiana: {cui['Italian']['restaurant_name']}', 
                  value=f'{cui['Italian']['aggregate_rating']}/5.0',
                  help=f"""
                  País: {cui['Italian']['country']}\n 
                  Cidade: {cui['Italian']['city']}\n 
                  Médio prato p/ dois: {cui['Italian']['average_cost_for_two']} ({cui['Italian']['currency']})
                  """,
                  )

    with american:
        st.metric(label=f'Americana: {cui['American']['restaurant_name']}',
                  value=f'{cui['American']['aggregate_rating']}/5.0',
                  help=f"""
                  País: {cui['American']['country']}\n
                  Cidade: {cui['American']['city']}\n
                  Média prato p/ dois: {cui['American']['average_cost_for_two']} ({cui['American']['currency']})
                  """,
                  )

    with arabian:
        st.metric(label=f'Árabe: {cui['Arabian']['restaurant_name']}',
                  value=f'{cui['Arabian']['aggregate_rating']}/5.0',
                  help=f"""
                  País: {cui['Arabian']['country']}\n
                  Cidade: {cui['Arabian']['city']}\n
                  Média prato p/ dois: {cui['Arabian']['average_cost_for_two']} ({cui['Arabian']['currency']})
                  """,
                  )

    with japanese:
        st.metric(label=f'Japonês: {cui['Japanese']['restaurant_name']}',
                  value=f'{cui['Japanese']['aggregate_rating']}/5.0',
                  help=f"""
                  País: {cui['Japanese']['country']}\n
                  Cidade: {cui['Japanese']['city']}\n
                  Média prato p/ dois: {cui['Japanese']['average_cost_for_two']} ({cui['Japanese']['currency']})
                  """,
                  )

    with homemade:
        st.metric(label=f'Caseira: {cui['Home-made']['restaurant_name']}',
                  value=f'{cui['Home-made']['aggregate_rating']}/5.0',
                  help=f"""
                  País: {cui['Home-made']['country']}\n
                  Cidade: {cui['Home-made']['city']}\n
                  Média prato p/ dois: {cui['Home-made']['average_cost_for_two']} ({cui['Home-made']['currency']})
                  """,
                  )

    st.markdown("""---""")

# Vinculando o filtro com os dados
linhas_selecionadas = df['country'].isin(country_options)
df = df.loc[linhas_selecionadas, :]

linhas_selecionadas = df['cuisines'].isin(cuisines_options)
df = df.loc[linhas_selecionadas, :]

with st.container():
    st.markdown(f"<h5 style='text-align: center'>Top {top_n} Restaurantes com maior média de nota</h5>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

    st.dataframe(tb_cuisines(df), use_container_width=True)

    st.markdown("""---""")

with st.container():
    st.markdown(f"<h5 style='text-align: center'>Top {top_n} Tipos de Culinária com maior média de nota</h5>", unsafe_allow_html=True)

    fig = top_cuisines(df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")

with st.container():
    ratings, votes = st.columns(2, gap='large')

    with ratings:
        st.markdown(f"##### Top {top_n} tipos de culinária com maior média de nota com pedidos online")

        fig = online_rating(df)
        st.plotly_chart(fig, use_container_width=True)

    with votes:
        st.markdown(f"##### Top {top_n} tipos de culinária com maior média de avaliações sem pedidos online")

        fig = online_votes(df)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""---""")
    
with st.container():
    ratings, votes = st.columns(2, gap='large')

    with ratings:
        st.markdown(f"##### Top {top_n} tipos de culinária com maior média de nota com entrega")

        fig = delivery_rating(df)
        st.plotly_chart(fig, use_container_width=True)

    with votes:
        st.markdown(f"##### Top {top_n} tipos de culinária com maior média de avaliações sem entrega")

        fig = delivery_votes(df)
        st.plotly_chart(fig, use_container_width=True)
