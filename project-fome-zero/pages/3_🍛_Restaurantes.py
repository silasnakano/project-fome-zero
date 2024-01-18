# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='Restaurantes', page_icon='🍛', layout='wide')

# =============================== Functions =====================================



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
st.markdown("# 🍛 Visão Restaurantes")
st.markdown("""---""")