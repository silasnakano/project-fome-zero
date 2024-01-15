import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon='🏠'
)

df = pd.read_csv('data/processed/zomato_processed.csv')

# %%
df['restaurant_id'].nunique()
# %%
df['country_code'].nunique()
# %%
df['city'].nunique()
# %%
df['votes'].sum()
# %%
df['cuisines'].nunique()
# %%
df.head()
