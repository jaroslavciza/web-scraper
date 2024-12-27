import httpx

from fastapi import FastAPI
from bs4 import BeautifulSoup


app = FastAPI() # je postavený na async def takže už ho nemusím na async volání používat zvlášť

@app.get("/api/btc")
async def scrape_google():
    # url = 'https://www.bitstamp.net/markets/btc/usd/'
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
   

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()  # Vyvolá chybu, pokud status code není 200
        except httpx.HTTPStatusError:
            return {"error": "Failed to fetch content from CoinMarketCap - HTTP error."}
        except httpx.RequestError:
            return {"error": "Failed to fetch content from CoinMarketCap - Request error."}

    data = {}
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        div = soup.find("div", {"id": "section-coin-overview"})
        priceElement = div.find("span", {"data-test": "text-cdp-price-display"})
        if priceElement:
            data["price"] = priceElement.text.strip()  # Extrahujeme cenu
        else:
            data["error"] = "Price element not found in HTML structure."
    except AttributeError:
        data["error"] = "Failed to parse the HTML correctly."
    
    return data