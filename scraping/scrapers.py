import requests
from bs4 import BeautifulSoup
from scraping.convert_to_datetime import convert_to_datetime
from model.Movie import Movie


def scrape_de_cinema():
    url = 'https://www.destudio.com/nl/programma/grid/all'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    movie_divs = soup.find_all("div", {"class": "view-grouping--level-2"})
    movies = []

    for div in movie_divs:
        date_time = div.find("div", {"class": "views-field views-field-field-datum-event"}).text
        date_time = convert_to_datetime(date_time)
        image_url = "https://www.destudio.com" + div.find("img")['src']

        name_div = div.find("div", {"class": "views-field views-field-title"})
        name = name_div.text
        info_link = "https://www.destudio.com" + name_div.find("a")['href']

        director = div.find("div", {"class": "views-field views-field-field-subtitle"})

        if director:
            director = director.text
        else:
            director = "No director found"

        category = div.find("div", {"class": "views-field views-field-field-categorie"}).text
        ticket_link = div.find("div", {"class": "views-field views-field-field-ticket-link"}).text
        description = div.find("div", {"class": "views-field views-field-body"}).text

        movie = Movie(date_time, 'De Studio', image_url, name, info_link, director, category, ticket_link, description)

        movies.append(movie)

    return movies


def scrape_lumieres():
    return []


def scrape_cartoons():
    return []
