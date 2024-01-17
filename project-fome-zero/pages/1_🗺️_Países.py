# ======================== Bibliotecas & Page_config ============================
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Países', page_icon='🗺️', layout='wide')

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
country_options = st.sidebar.multiselect('Escolha um pais: ', df.loc[:, 'country'].unique().tolist(), default=['Brazil', 'United States of America', 'England', 'Qatar', 'Australia'])
st.sidebar.markdown("""---""")

st.sidebar.markdown('##### Powered by Silas Nakano')

# ---------------------------------- Main Page --------------------------------------
st.markdown("# :earth_americas: Visão Países")

with st.container():
    st.markdown("# :earth_americas: Visão Países")

with st.container():
    st.markdown("# :earth_americas: Visão Países")

with st.container():
    ratings, cost = st.columns(2, gap='large')

    with ratings:
        st.markdown("# :earth_americas: Visão Países")
    
    with cost:
        st.markdown("# :earth_americas: Visão Países")