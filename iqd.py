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
        rate = soup.find("span", class_="DFlfde SwHCTb").text
        return float(rate.replace(",", ""))
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
        start = float(request.form['start'])
        end = float(request.form['end'])
        step = float(request.form['step'])

        conversion_results = []
        for amount in range(int(start), int(end + 1), int(step)):
            usd_to_iqd = amount * usd_to_iqd_rate
            iqd_to_usd = amount / usd_to_iqd_rate
            conversion_results.append({
                'amount': amount,
                'usd_to_iqd': round(usd_to_iqd, 2),
                'iqd_to_usd': round(iqd_to_usd, 2)
            })

        return render_template('results.html', conversion_results=conversion_results, rate=usd_to_iqd_rate)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
