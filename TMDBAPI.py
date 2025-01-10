import requests
import os
from dotenv import load_dotenv

def getID(title):
    load_dotenv()

    tmdb_api_key = os.environ.get("TMDB_API_KEY", "no api key found")

    url = "https://api.themoviedb.org/3/search/movie?query=" + title

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + tmdb_api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        results = data.get("results", [])  # Get the results list

        if results:
            movie_id = results[0].get("id")
            return movie_id
        else:
            print("No results found.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def getConfig():
    load_dotenv()

    tmdb_api_key = os.environ.get("TMDB_API_KEY", "no api key found")
    config_url = "http://api.themoviedb.org/3/configuration"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + tmdb_api_key
    }

    config_res = requests.get(config_url, headers=headers)
    base_url = ""

    if config_res.status_code == 200:
        base_url = config_res.json().get("images").get("secure_base_url")
    return base_url + "w780"

def getImage(id, base_url):
    load_dotenv()

    tmdb_api_key = os.environ.get("TMDB_API_KEY", "no api key found")

    url = "https://api.themoviedb.org/3/movie/" + str(id) + "/images"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + tmdb_api_key
    }

    image_res = requests.get(url, headers=headers)

    if image_res.status_code == 200:
        data = image_res.json()
        backdrop = data.get("backdrops")[0].get("file_path")
        return base_url + backdrop
