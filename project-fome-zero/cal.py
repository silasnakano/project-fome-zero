# %%
import pandas as pd
import numpy as np

df = pd.read_csv('data/processed/zomato_processed.csv')

# %% 1
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Italian'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=False).reset_index()
group
 
# %% 2
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Italian'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=True).reset_index()
group
# %% 3
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'American'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=False).reset_index()
group

# %% 4
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'American'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=True).reset_index()
group
# %% 5
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Arabian'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=False).reset_index()
group

# %% 6
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Arabian'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=True).reset_index()
group
# %% 7
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Japanese'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=False).reset_index()
group
# %% 8
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Japanese'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=True).reset_index()
group
# %% 9
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Home-made'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=False).reset_index()
group

# %% 10
cols = ['restaurant_name', 'votes']
linhas_selecionadas = df['cuisines'] == 'Home-made'
group = df.loc[linhas_selecionadas, cols].groupby('restaurant_name').mean().sort_values('votes', ascending=True).reset_index()
group
# %% 11
cols = ['cuisines', 'average_cost_for_two']
group = df.loc[:, cols].groupby('cuisines').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
group

# %% 12
cols = ['cuisines', 'aggregate_rating']
group = df.loc[:, cols].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=False).reset_index()
group

# %% 13
cols = ['cuisines', 'restaurant_id', 'has_online_delivery', 'is_delivering_now']
group = df.loc[:, cols].groupby('cuisines').count().reset_index()

online = group.loc[group['has_online_delivery'] == 1, :]
delivery = group.loc[group['is_delivering_now'] == 1, :]

result = pd.concat([online, delivery]).reset_index(drop=True)
result
# %%

df.columns
# %%
df['has_online_delivery']
# %%
