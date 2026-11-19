# Movie Data Web Scraper (Python)

A Python web scraping project built using **Requests**, **BeautifulSoup4**, and **Tabulate** [cite: 140, 141]. The script extracts structured movie details (Title, Release Year, Genre, and Description) from an HTML webpage and formats the output into a clean ASCII grid table in the terminal [cite: 139, 141, 142].

## Project Structure
```text
python-movie-web-scraper/
├── README.md
├── requirements.txt
├── scrape_movies.py
└── data.html
```

## Features
- **HTML Parsing:** Extracts movie metadata from nested HTML `<div>` elements using `BeautifulSoup` [cite: 141].
- **Dual Mode Support:** Supports scraping from a local server (`http://localhost/data/data.html`) as well as directly reading the bundled `data.html` file out of the box if no local server is running [cite: 142, 143].
- **Formatted Output:** Displays extracted data in a clean grid layout using the `tabulate` library [cite: 142].

## Setup & Usage

1. **Clone or extract the repository:**
   ```bash
   git clone https://github.com/<YOUR-USERNAME>/python-movie-web-scraper.git
   cd python-movie-web-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python scrape_movies.py
   ```
   *(Optional: If using XAMPP/WAMP, place `data.html` inside `htdocs/data/data.html` and start Apache to scrape via `http://localhost/data/data.html` [cite: 142]. Otherwise, the script automatically falls back to reading the local `data.html` file.)*
