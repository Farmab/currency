from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to fetch exchange rate from Google
def get_exchange_rate():
    url = "https://www.google.com/search?q=usd+to+iqd"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rate_element = soup.find("span", class_="DFlfde SwHCTb")
        if rate_element:
            rate = rate_element.text
            return float(rate.replace(",", ""))
        else:
            raise ValueError("Exchange rate element not found on the page.")
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None

@app.route('/')
def home():
    return render_template('converter.html')

@app.route('/convert', methods=['POST'])
def convert():
    usd_to_iqd_rate = get_exchange_rate()
    if usd_to_iqd_rate is None:
        return "Error fetching exchange rate. Please try again later."

    try:
        usd_amount = request.form.get('usd_amount')
        iqd_amount = request.form.get('iqd_amount')

        usd_to_iqd = None
        iqd_to_usd = None

        if usd_amount:
            usd_to_iqd = float(usd_amount) * usd_to_iqd_rate
        if iqd_amount:
            iqd_to_usd = float(iqd_amount) / usd_to_iqd_rate

        return render_template(
            'converter.html', 
            usd_amount=usd_amount, 
            iqd_amount=iqd_amount, 
            usd_to_iqd=usd_to_iqd, 
            iqd_to_usd=iqd_to_usd, 
            rate=usd_to_iqd_rate
        )
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
