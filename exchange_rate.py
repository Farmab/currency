import requests

def get_exchange_rates():
    """
    Fetches the latest exchange rates for USD, IQD, EUR, and GBP.
    Returns a dictionary of rates or None if an error occurs.
    """
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Replace with a reliable API if needed
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Extract rates for required currencies
        rates = {
            "USD": 1.0,  # Base currency
            "IQD": data["rates"].get("IQD", 0),  # IQD rate
            "EUR": data["rates"].get("EUR", 0),  # EUR rate
            "GBP": data["rates"].get("GBP", 0),  # GBP rate
        }
        return rates
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None
