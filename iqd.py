# Function to fetch exchange rate from Google
def get_exchange_rate():
    url = "https://www.google.com/search?q=usd+to+iqd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Check for common span classes or elements containing the rate
        rate_element = soup.find("span", class_="DFlfde SwHCTb")
        if rate_element:
            rate = rate_element.text
            return float(rate.replace(",", ""))
        else:
            # Debugging output for the page content
            print("Exchange rate element not found. Page content:")
            print(soup.prettify())
            return None
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None
