# %%
import pandas as pd
import numpy as np

df = pd.read_csv('data/processed/zomato_processed.csv')


# %%
cols = ['country', 'city']
group = df.loc[:, cols].groupby('country').nunique().sort_values('city', ascending=False)

group.reset_index().head(1)

# %%
cols = ['country', 'restaurant_id']
group = df.loc[:, cols].groupby('country').nunique().sort_values('restaurant_id', ascending=False)

group.reset_index().head(10)

# %%
cols = ['country', 'restaurant_id']
linhas_selecionadas = df['price_range'] == 4
group = df.loc[linhas_selecionadas, cols].groupby('country').count().sort_values('restaurant_id', ascending=False)

group.reset_index().head(10)
# %%
cols = ['country', 'cuisines']
group = df.loc[:, cols].groupby('country').nunique().sort_values('cuisines', ascending=False)

group.reset_index().head(10)
# %%
cols = ['country', 'votes']
group = df.loc[:, cols].groupby('country').sum().sort_values('votes', ascending=False)

group.reset_index().head(10)
# %%
