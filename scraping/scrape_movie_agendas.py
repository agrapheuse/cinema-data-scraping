from scraping.scrapers import *
import pandas as pd


def scrape_movie_agendas():
    movies = []
    movies.extend(scrape_de_cinema())
    movies.extend(scrape_lumieres())
    movies.extend(scrape_cartoons())
    movie_df = pd.DataFrame.from_records([m.to_dict() for m in movies])
    return movie_df
