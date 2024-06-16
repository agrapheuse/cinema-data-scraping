from db.database import run_query, run_insert_query
from db.queries import *
from scraping.scrape_movie_agendas import scrape_movie_agendas

# empty the table
run_query(empty_table_query)

# scrape the data
movies = scrape_movie_agendas()

# insert the data
for index, row in movies.iterrows():
    run_insert_query(insert_query, (row['name'], row['director'], row['category'], row['description'],
                                    row['cinema'], row['date_time'], row['image_url'], row['info_link'],
                                    row['ticket_link']))
print("Data inserted successfully!")


