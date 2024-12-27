import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No Title'
    print(f"Title of the website: {title}")

if __name__ == "__main__":
    scrape_website('https://www.google.com')