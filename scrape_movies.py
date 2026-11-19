import os
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def parse_movies(html_content):
    # Parse the HTML content of the page [cite: 141]
    soup = BeautifulSoup(html_content, 'html.parser')

    movie_list = []
    movies = soup.find_all('div', class_='movie')

    for movie in movies:
        title = movie.find('div', class_='title').text.strip()
        year = movie.find('div', class_='year').text.strip()
        genre = movie.find('div', class_='genre').text.strip()
        description = movie.find('div', class_='description').text.strip()

        # Create a list representing a movie entry [cite: 142]
        movie_info = [title, year, genre, description]
        movie_list.append(movie_info)

    return movie_list


def scrape_website(url, fallback_file="data.html"):
    try:
        # Send a GET request to the URL [cite: 141]
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return parse_movies(response.text)
    except requests.RequestException:
        pass

    # Fallback to local data.html if localhost server is not running
    if os.path.exists(fallback_file):
        with open(fallback_file, "r", encoding="utf-8") as file:
            return parse_movies(file.read())

    print("Failed to retrieve webpage and local fallback file was not found.")
    return None


if __name__ == "__main__":
    # URL of the webpage to scrape [cite: 142]
    url = "http://localhost/data/data.html"

    # Call the function to scrape the website [cite: 142]
    movies = scrape_website(url)

    # Print the extracted movie data in tabular format [cite: 142]
    if movies:
        headers = ["Title", "Year", "Genre", "Description"]
        print(tabulate(movies, headers=headers, tablefmt="grid", maxcolwidths=[25, 6, 20, 50]))
    else:
        print("No movie data retrieved.")
