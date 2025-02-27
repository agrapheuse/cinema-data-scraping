import requests
from bs4 import BeautifulSoup
from scraping.convert_to_datetime import convert_to_datetime
from model.MovieShowingRaw import MovieShowingRaw


def scrape_de_cinema():
    url = 'https://www.destudio.com/nl/programma/grid/all'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    movie_divs = soup.find_all("div", {"class": "view-grouping--level-2"})
    movies = []

    for div in movie_divs:
        date_time = div.find("div", {"class": "views-field views-field-field-datum-event"}).text
        date_time = date_time.split()[1:]

        day = date_time[0]
        month = date_time[1]
        hour = date_time[2].split("u")[0]
        minute = date_time[2].split("u")[1]

        date_time = convert_to_datetime(day, month, hour, minute)
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
        if category.lower() != "film":
            break
        ticket_div = div.find("div", {"class": "views-field views-field-field-ticket-link"})
        link = ""
        if ticket_div.find("a"):
            link = ticket_div.find("a")["href"]
        description = div.find("div", {"class": "views-field views-field-body"}).text

        movie = MovieShowingRaw(date_time, 'c9d4c053-49b6-410c-bc78-2d54a9991870', image_url, name, info_link, director,
                                category, link, description)
        
        movies.append(movie)

    print("de studio scraped successfully")
    return movies


def scrape_lumieres():
    url = 'https://www.lumiere-antwerpen.be/agenda-lumiere-antwerpen/'
    return scrape_lumieres_and_cartoons("a6479f2a-963b-490f-ba92-6bdb99eb1f04", url)


def scrape_cartoons():
    url = 'https://cinemacartoons.be/agenda-cinema-cartoons/'
    return scrape_lumieres_and_cartoons("8b659e03-0435-485b-8f77-9dff6e1f40e6", url)


def scrape_lumieres_and_cartoons(name, url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    day_divs = soup.find_all("h2", {"class": "mb-5 mt-4"})
    for day_div in day_divs:
        date = day_div.get_text().split(" ")[1:]
        day = date[0]
        month = date[1]
        movie_div = day_div.find_next("div", {"class": "row"})
        movie_div = movie_div.find_all("div", {"class": "show col-12 col-lg-6 mb-3"})

        formatted_url = url.split(".be/")[0] + '.be/'
        for movie in movie_div:
            images = movie.findAll("img")
            image_url = ""
            for i in images:
                if formatted_url in i["src"]:
                    image_url = i["src"]

            info_url = formatted_url + movie.find("a")['href']

            title = movie.find("h4").get_text()

            if "talkshow" in title.lower() or "q&a" in title.lower():
                continue

            button = movie.find("a", {"class": "btn btn-primary ticket-link px-3 py-1 mr-auto me-auto"})
            ticket_url = button['data-href']
            time = button.get_text()
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            date_time = convert_to_datetime(day, month, hour, minute)

            director, description = getMoreInfo(info_url)

            movie = MovieShowingRaw(date_time, name, image_url, title, info_url, director,
                          'No category found', ticket_url, description)

            movies.append(movie)

    print("cartoon or lumiere scraped successfully")
    return movies

def getMoreInfo(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    director_div = soup.find("div", {"class": "movie-meta my-3"})
    director = director_div.get_text(strip=True).replace('Regisseur:', '').strip()

    info_div = soup.find("div", {"class": "row"})
    central_div = info_div.find("div", {"class": "col-md-8"})
    p_elements = central_div.find_all("p")

    description = ""
    for p in p_elements: 
        description += p.get_text() + " "

    return director, description