import requests

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Replace with a reliable API if needed
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract rates for the required currencies
        rates = {
            "USD": 1.0,  # Base currency
            "IQD": data["rates"].get("IQD", 0),  # Fetch IQD rate
            "EUR": data["rates"].get("EUR", 0),  # Fetch EUR rate
            "GBP": data["rates"].get("GBP", 0),  # Fetch GBP rate
        }
        return rates
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None
