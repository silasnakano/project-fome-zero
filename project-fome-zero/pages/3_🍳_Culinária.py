import pandas as pd
import streamlit as st

st.set_page_config(page_title='Culinária', page_icon='🍳', layout='wide')

df = pd.read_csv('./data/processed/zomato_processed.csv')
