# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Culinária', page_icon='🍳', layout='wide')

# =============================== Functions =====================================

def cuisines():

    cui = {'Italian':'', 'American':'', 'Arabian':'', 'Japanese':'', 'Home-made':''}
    cols = ['restaurant_id', 'restaurant_name', 'country', 'city', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'votes']

    for i in cui.keys():
        lines = df['cuisines'] == i

        cui[i] = (df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).iloc[0, :].to_dict())

    return cui

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
st.markdown("# 🍳 Visão Culinária")
st.markdown("""---""")

with st.container():
    st.markdown("<h4 style='text-align: center'>Melhores Restaurantes por Tipo de Culinária</h4>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

    cui = cuisines()

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

with st.container():
    st.markdown("""---""")

with st.container():
    st.markdown("""---""")
    