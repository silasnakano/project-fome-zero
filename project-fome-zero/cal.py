# %%
import pandas as pd
import numpy as np

df = pd.read_csv('data/processed/zomato_processed.csv')

# %%
cols = ['city', 'restaurant_id']
group = df.loc[:, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
cols = ['city', 'restaurant_id']
linhas_selecionadas = df['aggregate_rating'] > 4
group = df.loc[linhas_selecionadas, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
cols = ['city', 'restaurant_id']
linhas_selecionadas = df['aggregate_rating'] < 2.5
group = df.loc[linhas_selecionadas, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
df.columns
# %%
cols = ['city', 'average_cost_for_two']
group = df.loc[:, cols].groupby('city').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
group
# %%
cols = ['city', 'cuisines']
group = df.loc[:, cols].groupby('city').nunique().sort_values('cuisines', ascending=False).reset_index()
group
# %%
df.columns
# %%
cols = ['city', 'restaurant_id']
linhas_selecionadas = df['has_table_booking'] == 1
group = df.loc[linhas_selecionadas, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
cols = ['city', 'restaurant_id']
linhas_selecionadas = df['is_delivering_now'] == 1
group = df.loc[linhas_selecionadas, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
cols = ['city', 'restaurant_id']
linhas_selecionadas = df['has_online_delivery'] == 1
group = df.loc[linhas_selecionadas, cols].groupby('city').nunique().sort_values('restaurant_id', ascending=False).reset_index()
group
# %%
