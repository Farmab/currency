import requests
from bs4 import BeautifulSoup

def get_bazar_exchange_rates():
    url = "https://example-bazar-rates.com/iraq"  # Replace with the actual website URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Example scraping logic (adjust based on the website structure)
        rates = {
            "USD": 1.0,  # Base currency
            "IQD": float(soup.find("span", id="usd-to-iqd").text.strip().replace(",", "")),  # Bazar rate
            "EUR": float(soup.find("span", id="usd-to-eur").text.strip().replace(",", "")),  # Optional additional rates
            "GBP": float(soup.find("span", id="usd-to-gbp").text.strip().replace(",", "")),  # Optional additional rates
        }
        return rates
    except Exception as e:
        print(f"Error fetching bazar exchange rates: {e}")
        return None
