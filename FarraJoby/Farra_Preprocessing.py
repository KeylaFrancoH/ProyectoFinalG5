import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#-------Preprocesamiento--------
#---Funciones Personalizadas----
def format_info(text):
    if ':' in text:
        text = text.split(':')[-1]
    text = text.replace('\n','').replace('\r','')
    return text
#---Leemos el file generado por el scrapper de Ruby-----
games_df = pd.read_csv('../archivos/games.csv', names=["name", "genres", "year", "directors", "resume", "votes", "stars", "rating"])

games_df = games_df.astype(str)
games_df['genres'] = games_df.genres.apply(lambda x: x.strip())
games_df['resume'] = games_df.resume.apply(lambda x: x.strip())

games_df['directors'] = games_df.directors.apply(lambda x: format_info(x.strip()))
games_df['stars'] = games_df.stars.apply(lambda x: format_info(x.strip()))

games_df.rating = games_df.rating.astype(float)
games_df.votes = games_df.votes.astype(int)

#----- Primera Pregunta -----
top_rating = games_df.sort_values(by=['rating'], ascending=False, ignore_index=True)[:10]

#----- Segunda Pregunta -----
genres_2021 = sum(list(map(lambda x: x.split(','), games_df.genres[games_df.year == '2021'])), [])
genres_2022 = sum(list(map(lambda x: x.split(','), games_df.genres[games_df.year == '2022'])), [])

genres_2021_df = pd.DataFrame(data=genres_2021).value_counts().rename_axis('Genres').reset_index(name='counts')[:6]
genres_2022_df = pd.DataFrame(data=genres_2022).value_counts().rename_axis('Genres').reset_index(name='counts')[:6]

#----- Tercera Pregunta -----

genres_total = sum(list(map(lambda x: x.split(','), games_df.genres)), [])
genres_total_df = pd.DataFrame(data=genres_total).value_counts().rename_axis('Genres').reset_index(name='counts')[:6]

