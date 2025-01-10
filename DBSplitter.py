import uuid
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import select, insert
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, LONGTEXT, DATETIME
from sqlalchemy.orm import sessionmaker
import re

from TMDBAPI import getID, getImage, getConfig


def remove_parentheses_content(title):
    return re.sub(r'\s*\(.*?\)', '', title).strip()

metadata = MetaData()

raw_showing_data = Table(
    "RawMovieData",
    metadata,
    Column('uuid', CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column('title', VARCHAR(255)),
    Column('director', VARCHAR(255)),
    Column('category', VARCHAR(255)),
    Column('description', LONGTEXT),
    Column('cinema_id', VARCHAR(36)),
    Column('date_time', DATETIME()),
    Column('image_url', VARCHAR(255)),
    Column('info_link', VARCHAR(255)),
    Column('ticket_link', VARCHAR(255)),
)

movies = Table(
    "Movies",
    metadata,
    Column('uuid', CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column('title', VARCHAR(255)),
    Column('director', VARCHAR(255)),
    Column('category', VARCHAR(255)),
    Column('description', LONGTEXT),
    Column('image_url', VARCHAR(255)),
    Column('CinemaId', VARCHAR(36)),
)

showings = Table(
    "Showings",
    metadata,
    Column('uuid', CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4())),
    Column('MovieId', VARCHAR(36)),
    Column('date_time', DATETIME()),
    Column('info_link', VARCHAR(255)),
    Column('ticket_link', VARCHAR(255)),
)

# MySQL connection details
user = "user"
password = "password"
host = "localhost"
port = 3308
database = "movie_db"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", echo=True, future=True)
metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

try:
    # Step 1: Query all data from RawShowingInfo
    raw_data = session.execute(select(raw_showing_data)).fetchall()

    base_url = getConfig()

    # Step 3: Extract unique movies
    movies_data = {}
    for row in raw_data:
        title = row[1]
        director = row[2]
        category = row[3]
        description = row[4]
        image_url = row[7]
        cinema_id = row[5]

        movie_key = (title, director, cinema_id)
        if movie_key not in movies_data:
            movies_data[movie_key] = {
                "uuid": str(uuid.uuid4()),
                "title": title,
                "director": director,
                "category": category,
                "description": description,
                "image_url": image_url,
                "CinemaId": cinema_id,
            }

    # Insert unique movies into Movies table
    for movie in movies_data.values():
        if movie.get("image_url") == "poster":
            tmdb_id = getID(movie.get("title"))

            # Retry after cleaning the title if tmdb_id is None
            if tmdb_id is None:
                print(f"Checking title for parentheses: {movie.get('title')}")
                if '(' in movie.get("title") and ')' in movie.get("title"):
                    print("Parentheses detected, removing them...")
                    cleaned_title = remove_parentheses_content(movie.get("title"))
                    tmdb_id = getID(cleaned_title)
                    print(f"TMDB ID after cleaning: {tmdb_id}")

            # Fetch image URL if tmdb_id is available
            if tmdb_id is not None:
                image_url = getImage(tmdb_id, base_url)
                movie["image_url"] = image_url  # Update the movie's image_url
            else:
                print(f"Failed to fetch TMDB ID for title: {movie.get('title')}")

        # Insert the movie into the Movies table
        session.execute(insert(movies).values(**movie))
    session.commit()

    # Step 4: Insert data into Showings table
    for row in raw_data:
        title = row[1]
        director = row[2]
        cinema_id = row[5]
        date_time = row[6]
        info_link = row[7]
        ticket_link = row[8]

        movie_key = (title, director, cinema_id)
        movie_uuid = movies_data[movie_key]["uuid"]

        showing_data = {
            "uuid": str(uuid.uuid4()),
            "MovieId": movie_uuid,
            "date_time": date_time,
            "info_link": info_link,
            "ticket_link": ticket_link,
        }

        session.execute(insert(showings).values(**showing_data))
    session.commit()

    print("Data successfully divided and inserted!")
except Exception as e:
    session.rollback()
    print("An error occurred:", e)
finally:
    session.close()
