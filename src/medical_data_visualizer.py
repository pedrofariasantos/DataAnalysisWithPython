import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df['height']/100) ** 2)) > 25
df['overweight'] = df['overweight'].astype(int)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():

    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
        'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'
    ])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'] \
                   .count().reset_index(name='total')

    fig = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=df_cat, kind='bar'
    ).fig


    return fig

def draw_heat_map():

    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 12))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=.5,
        cbar_kws={'shrink': .5}
    )

    return fig
